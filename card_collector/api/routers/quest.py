"""A module containing continent endpoints."""

from typing import List
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException

from card_collector.container import Container
from card_collector.core.domains.quest import Quest, QuestIn
from card_collector.core.services.i_quest_service import IQuestService
from card_collector.container import Container
from card_collector.core.services.i_trade_offer_service import ITradeOfferService
from card_collector.core.repositories.i_profile_repository import IProfileRepository
from card_collector.core.repositories.i_card_repository import ICardRepository
from card_collector.core.repositories.i_profile_collection_repository import IProfileCollectionRepository
from card_collector.core.services.i_collection_integration_service import ICollectionIntegrationService

router = APIRouter()


@router.post("/create", response_model=Quest, status_code=201)
@inject
async def create_quest(
        quest: QuestIn,
        service: IQuestService = Depends(Provide[Container.quest_service]),
        profile_repository: IProfileRepository = Depends(Provide[Container.profile_repository]),
        card_repository: ICardRepository = Depends(Provide[Container.card_repository]),
        profile_collection_repository: IProfileCollectionRepository = Depends(Provide[Container.profile_collection_repository]),
        collection_integration_service: ICollectionIntegrationService = Depends(Provide[Container.collection_integration_service])
) -> dict:
    """An endpoint for adding new quest.

    Args:
        quest (QuestIn): The quest data.
        service (IQuestService, optional): The injected service dependency.

    Returns:
        dict: The new quest attributes.
    """

    if await profile_repository.get_by_id(quest.profile_id):
        if await card_repository.get_by_id(quest.reward):
            if await card_repository.get_all_by_rarity(quest.rarity_needed):
                if quest.cards_needed > 0:
                    new_quest = await service.add_quest(quest)
                    return new_quest.model_dump() if new_quest else {}
                raise HTTPException(status_code=404, detail="Cards needed need to be higher than 0")
            raise HTTPException(status_code=404, detail="Cards with given rarity not found")
        raise HTTPException(status_code=404, detail="Reward is not an existing card's id")
    raise HTTPException(status_code=404, detail="Profile not found")

@router.get("/all", response_model=List[Quest], status_code=200)
@inject
async def get_all_quests(
        service: IQuestService = Depends(Provide[Container.quest_service]),
) -> List:
    """An endpoint for getting all quests.

    Args:
        service (IQuestService, optional): The injected service dependency.

    Returns:
        List: The quest attributes collection.
    """

    quests = await service.get_all()

    return quests

@router.get("/{quest_id}",response_model=Quest,status_code=200,)
@inject
async def get_quest_by_id(
        quest_id: int,
        service: IQuestService = Depends(Provide[Container.quest_service]),
) -> dict | None:
    """An endpoint for getting quest by id.

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
        profile_repository: IProfileRepository = Depends(Provide[Container.profile_repository]),
        card_repository: ICardRepository = Depends(Provide[Container.card_repository]),
        profile_collection_repository: IProfileCollectionRepository = Depends(Provide[Container.profile_collection_repository]),
        collection_integration_service: ICollectionIntegrationService = Depends(Provide[Container.collection_integration_service])
) -> dict:
    """An endpoint for updating quest data.

    Args:
        quest_id (int): The id of the quest.
        updated_quest (QuestIn): The updated quest details.
        service (IQuesttService, optional): The injected service dependency.

    Raises:
        HTTPException: 404 if quest does not exist.

    Returns:
        dict: The updated quest details.
    if await profile_repository.get_by_id(quest.profile_id):
        if await card_repository.get_by_id(quest.reward):
            if await card_repository.get_all_by_rarity(quest.rarity_needed):
                if quest.cards_needed > 0:
                    new_quest = await service.add_quest(quest)
                    return new_quest.model_dump() if new_quest else {}
                raise HTTPException(status_code=404, detail="Cards needed need to be higher than 0")
            raise HTTPException(status_code=404, detail="Cards with given rarity not found")
        raise HTTPException(status_code=404, detail="Reward is not an existing card's id")
    raise HTTPException(status_code=404, detail="Profile not found")
    """

    if await service.get_by_id(quest_id=quest_id):
        if await profile_repository.get_by_id(updated_quest.profile_id):
            if await card_repository.get_by_id(updated_quest.reward):
                if await card_repository.get_all_by_rarity(updated_quest.rarity_needed):
                    if updated_quest.cards_needed > 0:
                        await service.update_quest(
                            quest_id=quest_id,
                            data=updated_quest,
                        )
                        return {**updated_quest.model_dump(), "id": quest_id}
                    raise HTTPException(status_code=404, detail="Cards needed need to be higher than 0")
                raise HTTPException(status_code=404, detail="Cards with given rarity not found")
            raise HTTPException(status_code=404, detail="Reward is not an existing card's id")
        raise HTTPException(status_code=404, detail="Profile not found")
    raise HTTPException(status_code=404, detail="Quest not found")


@router.delete("/{quest_id}", status_code=204)
@inject
async def delete_quest(
        quest_id: int,
        service: IQuestService = Depends(Provide[Container.quest_service]),
) -> None:
    """An endpoint for deleting quests.

    Args:
        quest_id (int): The id of the quest.
        service (IQuestService, optional): The injected service dependency.

    Raises:
        HTTPException: 404 if quest does not exist.
    """

    if await service.get_by_id(quest_id=quest_id):
        await service.delete_quest(quest_id)

        return

    raise HTTPException(status_code=404, detail="Quest not found")
