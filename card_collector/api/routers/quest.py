from typing import List

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException

from card_collector.core.domains.quest import Quest, QuestIn
from card_collector.core.services.i_quest_service import IQuestService
from card_collector.container import Container
from card_collector.core.services.i_profile_service import IProfileService
from card_collector.core.services.i_card_service import ICardService

router = APIRouter()

@router.post("/create", response_model=Quest, status_code=201)
@inject
async def create_quest(
        quest: QuestIn,
        service: IQuestService = Depends(Provide[Container.quest_service]),
        profile_service: IProfileService = Depends(Provide[Container.profile_service]),
        card_service: ICardService = Depends(Provide[Container.card_service]),
) -> dict:
    """
    An endpoint for adding new quest.

    Args:
        quest (QuestIn): The quest data.
        service (IQuestService): The injected service dependency.
        profile_service (IProfileService): The injected profile service dependency.
        card_service (IProfileService): The injected card service dependency.

    Returns:
        dict: The new quest attributes.

    Raises:
        HTTPException: 400 if data is incorrect.
        HTTPException: 404 if data does not exist.
    """

    if await profile_service.get_by_id(quest.profile_id):
        if await card_service.get_by_id(quest.reward):
            if quest.cards_needed > 0:
                new_quest = await service.add_quest(quest)
                return new_quest.model_dump() if new_quest else {}
            raise HTTPException(status_code=400, detail="Cards needed need to be higher than 0")
        raise HTTPException(status_code=404, detail="Reward id not found")
    raise HTTPException(status_code=404, detail="Profile not found")

@router.get("/all", response_model=List[Quest], status_code=200)
@inject
async def get_all_quests(
        service: IQuestService = Depends(Provide[Container.quest_service]),
) -> List:
    """
    An endpoint for getting all quests.

    Args:
        service (IQuestService, optional): The injected service dependency.

    Returns:
        List: The quest attributes collection.
    """

    quests = await service.get_all()

    return quests

@router.get("/all/{profile_id}", response_model=List[Quest], status_code=200)
@inject
async def get_all_by_profile(
        profile_id: int,
        service: IQuestService = Depends(Provide[Container.quest_service]),
) -> List:
    """
    An endpoint for getting all quests by profile id.

    Args:
        profile_id (int): The id of the profile.
        service (ICardService): The injected service dependency.

    Returns:
        List: The card attributes collection.

    Raises:
        HTTPException: 404 if quests do not exist.
    """

    quests = await service.get_all_by_profile(profile_id)
    if quests:
        return quests
    raise HTTPException(status_code=404, detail="No quests found")

@router.get("/{quest_id}",response_model=Quest,status_code=200,)
@inject
async def get_quest_by_id(
        quest_id: int,
        service: IQuestService = Depends(Provide[Container.quest_service]),
) -> dict | None:
    """
    An endpoint for getting quest by id.

    Args:
        quest_id (int): The id of the quest.
        service (IQuestService, optional): The injected service dependency.

    Returns:
        dict | None: The quest details.
    """

    if quest := await service.get_by_id(quest_id):
        return quest.model_dump()

    raise HTTPException(status_code=404, detail="Quest not found")

@router.put("/{quest_id}", response_model=Quest, status_code=201)
@inject
async def update_quest(
        quest_id: int,
        updated_quest: QuestIn,
        service: IQuestService = Depends(Provide[Container.quest_service]),
        profile_service: IProfileService = Depends(Provide[Container.profile_service]),
        card_service: ICardService = Depends(Provide[Container.card_service]),
) -> dict:
    """
    An endpoint for updating quest data.

    Args:
        quest_id (int): The id of the quest.
        updated_quest (QuestIn): The updated quest details.
        service (IQuestService): The injected service dependency.
        profile_service (IProfileService): The injected profile service dependency.
        card_service (ICardService): The injected card service dependency.

    Returns:
        dict: The updated quest details.

    Raises:
        HTTPException: 400 if data is incorrect.
        HTTPException: 404 if quest does not exist.
    """

    if await service.get_by_id(quest_id=quest_id):
        if await profile_service.get_by_id(updated_quest.profile_id):
            if await card_service.get_by_id(updated_quest.reward):
                if updated_quest.cards_needed > 0:
                    await service.update_quest(
                        quest_id=quest_id,
                        data=updated_quest,
                    )
                    return {**updated_quest.model_dump(), "id": quest_id}
                raise HTTPException(status_code=400, detail="Cards needed need to be higher than 0")
            raise HTTPException(status_code=404, detail="Reward id not found")
        raise HTTPException(status_code=404, detail="Profile not found")
    raise HTTPException(status_code=404, detail="Quest not found")


@router.delete("/{quest_id}", status_code=204)
@inject
async def delete_quest(
        quest_id: int,
        service: IQuestService = Depends(Provide[Container.quest_service]),
) -> None:
    """
    An endpoint for deleting quests.

    Args:
        quest_id (int): The id of the quest.
        service (IQuestService): The injected service dependency.

    Raises:
        HTTPException: 404 if quest does not exist.
    """

    if await service.get_by_id(quest_id=quest_id):
        await service.delete_quest(quest_id)

        return

    raise HTTPException(status_code=404, detail="Quest not found")
