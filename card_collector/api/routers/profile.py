"""A module containing continent endpoints."""

from typing import Iterable
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException

from card_collector.container import Container
from card_collector.core.domains.profile import Profile, ProfileIn
from card_collector.core.services.i_profile_service import IProfileService

router = APIRouter()


@router.post("/create", response_model=Profile, status_code=201)
@inject
async def create_profile(
        profile: ProfileIn,
        service: IProfileService = Depends(Provide[Container.profile_service]),
) -> dict:
    """An endpoint for adding new profile.

    Args:
        profile (ProfileIn): The profile data.
        service (IProfileService, optional): The injected service dependency.

    Returns:
        dict: The new profile attributes.
    """

    new_profile = await service.add_profile(profile)

    return new_profile.model_dump() if new_profile else {}

@router.get("/all", response_model=Iterable[Profile], status_code=200)
@inject
async def get_all_profiles(
        service: IProfileService = Depends(Provide[Container.profile_service]),
) -> Iterable:
    """An endpoint for getting all profiles.

    Args:
        service (IProfileService, optional): The injected service dependency.

    Returns:
        Iterable: The profile attributes collection.
    """

    profiles = await service.get_all()

    return profiles



@router.get("/{profile_id}",response_model=Profile,status_code=200,)
@inject
async def get_profile_by_id(
        profile_id: int,
        service: IProfileService = Depends(Provide[Container.profile_service]),
) -> dict | None:
    """An endpoint for getting profile by id.

    Args:
        profile_id (int): The id of the profile.
        service (IProfileService, optional): The injected service dependency.

    Returns:
        dict | None: The profile details.
    """

    if profile := await service.get_by_id(profile_id):
        return profile.model_dump()

    raise HTTPException(status_code=404, detail="Profile not found")


@router.put("/{profile_id}", response_model=Profile, status_code=201)
@inject
async def update_profile(
        profile_id: int,
        updated_profile: ProfileIn,
        service: IProfileService = Depends(Provide[Container.profile_service]),
) -> dict:
    """An endpoint for updating profile data.

    Args:
        profile_id (int): The id of the profile.
        updated_profile (ProfileIn): The updated profile details.
        service (IProfiletService, optional): The injected service dependency.

    Raises:
        HTTPException: 404 if profile does not exist.

    Returns:
        dict: The updated profile details.
    """

    if await service.get_by_id(profile_id=profile_id):
        await service.update_profile(
            profile_id=profile_id,
            data=updated_profile,
        )
        return {**updated_profile.model_dump(), "id": profile_id}

    raise HTTPException(status_code=404, detail="Profile not found")


@router.delete("/{profile_id}", status_code=204)
@inject
async def delete_profile(
        profile_id: int,
        service: IProfileService = Depends(Provide[Container.profile_service]),
) -> None:
    """An endpoint for deleting profiles.

    Args:
        profile_id (int): The id of the profile.
        service (IProfileService): The injected service dependency.

    Raises:
        HTTPException: 404 if profile does not exist.
    """

    if await service.get_by_id(profile_id=profile_id):
        await service.delete_profile(profile_id)

        return

    raise HTTPException(status_code=404, detail="Profile not found")