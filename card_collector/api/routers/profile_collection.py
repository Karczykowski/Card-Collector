"""A module containing continent endpoints."""

from typing import List
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException

from card_collector.container import Container
from card_collector.core.domains.profile_collection import ProfileCollection, ProfileCollectionIn
from card_collector.core.services.i_profile_collection_service import IProfileCollectionService
from card_collector.core.repositories.i_card_repository import ICardRepository
from card_collector.core.repositories.i_profile_repository import IProfileRepository

router = APIRouter()

@router.post("/create", response_model=ProfileCollection, status_code=201)
@inject
async def add_card_to_profile(
        profile_collection: ProfileCollectionIn,
        card_repository: ICardRepository = Depends(Provide[Container.card_repository]),
        profile_repository: IProfileRepository = Depends(Provide[Container.profile_repository]),
        service: IProfileCollectionService = Depends(Provide[Container.profile_collection_service]),
) -> dict:

    if await card_repository.get_by_id(profile_collection.card_id):
        if await profile_repository.get_by_id(profile_collection.profile_id):
            new_profile_collection = await service.add_card_to_profile_collection(profile_collection)

            return new_profile_collection.model_dump() if new_profile_collection else {}

        raise HTTPException(status_code=404, detail="Profile not found")
    raise HTTPException(status_code=404, detail="Card not found")


@router.get("/all", response_model=List[ProfileCollection], status_code=200)
@inject
async def get_all_profile_collections(
        service: IProfileCollectionService = Depends(Provide[Container.profile_collection_service]),
) -> List:

    profile_collections = await service.get_all()

    return profile_collections

@router.get("/all_by_profile_id", response_model=List[ProfileCollection], status_code=200)
@inject
async def get_profile_collection_by_profile_id(
        profile_id: int,
        service: IProfileCollectionService = Depends(Provide[Container.profile_collection_service]),
) -> List:

    profile_collections = await service.get_profile_collection_by_profile_id(profile_id)
    if profile_collections:
        return profile_collections

    raise HTTPException(status_code=404, detail="Profile not found")

@router.get("/all_by_prof_and_card_id", response_model=List[ProfileCollection], status_code=200)
@inject
async def get_profile_collection_by_profile_id_and_card_id(
        card_id: int,
        profile_id: int,
        card_repository: ICardRepository = Depends(Provide[Container.card_repository]),
        service: IProfileCollectionService = Depends(Provide[Container.profile_collection_service]),
        profile_repository: IProfileRepository = Depends(Provide[Container.profile_repository]),
) -> List:

    if await card_repository.get_by_id(card_id):
        if await profile_repository.get_by_id(profile_id):
            profile_collections = await service.get_profile_collection_by_profile_id_and_card_id(card_id, profile_id)
            return profile_collections
        raise HTTPException(status_code=404, detail="Profile not found")
    raise HTTPException(status_code=404, detail="Card not found")



@router.get("/{profile_collection_id}",response_model=ProfileCollection,status_code=200,)
@inject
async def get_profile_collection_by_id(
        profile_collection_id: int,
        service: IProfileCollectionService = Depends(Provide[Container.profile_collection_service]),
) -> dict | None:
    """An endpoint for getting profile_collection by id.

    Args:
        profile_collection_id (int): The id of the profile_collection.
        service (IProfileCollectionService, optional): The injected service dependency.

    Returns:
        dict | None: The profile_collection details.
    """

    if profile_collection := await service.get_by_id(profile_collection_id):
        return profile_collection.model_dump()

    raise HTTPException(status_code=404, detail="Profile Collection not found")

@router.put("/{profile_collection_id}", response_model=ProfileCollection, status_code=201)
@inject
async def update_profile_collection(
        profile_collection_id: int,
        updated_profile_collection: ProfileCollectionIn,
        card_repository: ICardRepository = Depends(Provide[Container.card_repository]),
        profile_repository: IProfileRepository = Depends(Provide[Container.profile_repository]),
        service: IProfileCollectionService = Depends(Provide[Container.profile_collection_service]),
) -> dict:

    if await card_repository.get_by_id(updated_profile_collection.card_id):
        if await profile_repository.get_by_id(updated_profile_collection.profile_id):
            if await service.get_by_id(profile_collection_id=profile_collection_id):
                await service.update_profile_collection(
                    profile_collection_id=profile_collection_id,
                    data=updated_profile_collection,
                )
                return {**updated_profile_collection.model_dump(), "id": profile_collection_id}

            raise HTTPException(status_code=404, detail="Profile Collection not found")
        raise HTTPException(status_code=404, detail="Profile not found")
    raise HTTPException(status_code=404, detail="Card not found")


@router.delete("/{profile_collection_id}", status_code=204)
@inject
async def delete_profile_collection(
        profile_collection_id: int,
        service: IProfileCollectionService = Depends(Provide[Container.profile_collection_service]),
) -> None:
    """An endpoint for deleting profile_collections.

    Args:
        profile_collection_id (int): The id of the profile_collection.
        service (IProfileCollectionService): The injected service dependency.

    Raises:
        HTTPException: 404 if profile_collection does not exist.
    """

    if await service.get_by_id(profile_collection_id=profile_collection_id):
        await service.delete_profile_collection(profile_collection_id)

        return

    raise HTTPException(status_code=404, detail="Profile Collection not found")
