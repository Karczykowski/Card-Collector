from typing import List

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException

from card_collector.container import Container
from card_collector.core.domains.profile_collection import ProfileCollection, ProfileCollectionIn
from card_collector.core.services.i_profile_collection_service import IProfileCollectionService
from card_collector.core.services.i_card_service import ICardService
from card_collector.core.services.i_profile_service import IProfileService

router = APIRouter()

@router.post("/create", response_model=ProfileCollection, status_code=201)
@inject
async def add_card_to_profile(
        profile_collection: ProfileCollectionIn,
        service: IProfileCollectionService = Depends(Provide[Container.profile_collection_service]),
        card_service: ICardService = Depends(Provide[Container.card_service]),
        profile_service: IProfileService = Depends(Provide[Container.profile_service]),
) -> dict:
    """
    An endpoint for adding cards to profile, therefore making a profile collection.

    Args:
        profile_collection (ProfileCollectionIn): The profile_collection details.
        service (IProfileCollectionService): The injected service dependency.
        card_service (ICardService): The injected card service dependency.
        profile_service (IProfileService): The injected profile service dependency.

    Returns:
        dict: The profile_collection details.

    Raises:
        HTTPException: 404 if data does not exist.
    """

    if await card_service.get_by_id(profile_collection.card_id):
        if await profile_service.get_by_id(profile_collection.profile_id):
            new_profile_collection = await service.add_profile_collection(profile_collection)

            return new_profile_collection.model_dump() if new_profile_collection else {}

        raise HTTPException(status_code=404, detail="Profile not found")
    raise HTTPException(status_code=404, detail="Card not found")


@router.get("/all", response_model=List[ProfileCollection], status_code=200)
@inject
async def get_all_profile_collections(
        service: IProfileCollectionService = Depends(Provide[Container.profile_collection_service]),
) -> List:
    """
    An endpoint for getting all profile collections.

    Args:
        service (IProfileCollectionService): The injected service dependency.

    Returns:
        List: The profile_collection details.
    """
    profile_collections = await service.get_all()

    return profile_collections

@router.get("/all_by_profile_id", response_model=List[ProfileCollection], status_code=200)
@inject
async def get_all_profile_collections_by_profile_id(
        profile_id: int,
        service: IProfileCollectionService = Depends(Provide[Container.profile_collection_service]),
        profile_service: IProfileService = Depends(Provide[Container.profile_service])
) -> List:
    """
    An endpoint for getting profile collections by profile id.

    Args:
        profile_id (int): The id of the profile.
        service (IProfileCollectionService): The injected service dependency.
        profile_service (IProfileService): The injected profile service dependency.

    Returns:
        List: The profile details.

    Raises:
        HTTPException: 404 if profile does not exist.
    """

    profile = await profile_service.get_by_id(profile_id)
    profile_collections = await service.get_all_profile_collections_by_profile_id(profile_id)

    if profile:
        return profile_collections

    raise HTTPException(status_code=404, detail="Profile not found")

@router.get("/{profile_collection_id}",response_model=ProfileCollection,status_code=200,)
@inject
async def get_profile_collection_by_id(
        profile_collection_id: int,
        service: IProfileCollectionService = Depends(Provide[Container.profile_collection_service]),
) -> dict | None:
    """
    An endpoint for getting profile_collection by id.

    Args:
        profile_collection_id (int): The id of the profile_collection.
        service (IProfileCollectionService): The injected service dependency.

    Returns:
        dict | None: The profile_collection details.

    Raises:
        HTTPException: 404 if profile does not exist.
    """

    if profile_collection := await service.get_by_id(profile_collection_id):
        return profile_collection.model_dump()

    raise HTTPException(status_code=404, detail="Profile Collection not found")

@router.delete("/{profile_collection_id}", status_code=204)
@inject
async def delete_profile_collection(
        profile_collection_id: int,
        service: IProfileCollectionService = Depends(Provide[Container.profile_collection_service]),
) -> None:
    """
    An endpoint for deleting profile_collections.

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
