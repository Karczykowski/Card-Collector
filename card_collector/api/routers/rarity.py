"""A module containing continent endpoints."""

from typing import Iterable
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException

from card_collector.container import Container
from card_collector.core.domains.rarity import Rarity, RarityIn
from card_collector.core.services.i_rarity_service import IRarityService

router = APIRouter()


@router.post("/create", response_model=Rarity, status_code=201)
@inject
async def create_rarity(
        rarity: RarityIn,
        service: IRarityService = Depends(Provide[Container.rarity_service]),
) -> dict:
    """An endpoint for adding new rarity.

    Args:
        rarity (RarityIn): The rarity data.
        service (IRarityService, optional): The injected service dependency.

    Returns:
        dict: The new rarity attributes.
    """

    new_rarity = await service.add_rarity(rarity)

    return new_rarity.model_dump() if new_rarity else {}

@router.get("/all", response_model=Iterable[Rarity], status_code=200)
@inject
async def get_all_rarities(
        service: IRarityService = Depends(Provide[Container.rarity_service]),
) -> Iterable:
    """An endpoint for getting all rarities.

    Args:
        service (IRarityService, optional): The injected service dependency.

    Returns:
        Iterable: The rarity attributes collection.
    """

    rarities = await service.get_all()

    return rarities



@router.get("/{rarity_id}",response_model=Rarity,status_code=200,)
@inject
async def get_rarity_by_id(
        rarity_id: int,
        service: IRarityService = Depends(Provide[Container.rarity_service]),
) -> dict | None:
    """An endpoint for getting rarity by id.

    Args:
        rarity_id (int): The id of the rarity.
        service (IRarityService, optional): The injected service dependency.

    Returns:
        dict | None: The rarity details.
    """

    if rarity := await service.get_by_id(rarity_id):
        return rarity.model_dump()

    raise HTTPException(status_code=404, detail="Rarity not found")


@router.get(
    "/user/{user_id}",
    response_model=Iterable[Rarity],
    status_code=200,
)
@inject
async def get_rarities_by_user(
        user_id: int,
        service: IRarityService = Depends(Provide[Container.rarity_service]),
) -> Iterable:
    """An endpoint for getting rarities by user who added them.

    Args:
        user_id (int): The id of the user.
        service (IRarityService, optional): The injected service dependency.

    Returns:
        Iterable: The rarity details collection.
    """

    rarities = await service.get_by_user(user_id)

    return rarities


@router.put("/{rarity_id}", response_model=Rarity, status_code=201)
@inject
async def update_rarity(
        rarity_id: int,
        updated_rarity: RarityIn,
        service: IRarityService = Depends(Provide[Container.rarity_service]),
) -> dict:
    """An endpoint for updating rarity data.

    Args:
        rarity_id (int): The id of the rarity.
        updated_rarity (RarityIn): The updated rarity details.
        service (IRaritytService, optional): The injected service dependency.

    Raises:
        HTTPException: 404 if rarity does not exist.

    Returns:
        dict: The updated rarity details.
    """

    if await service.get_by_id(rarity_id=rarity_id):
        await service.update_rarity(
            rarity_id=rarity_id,
            data=updated_rarity,
        )
        return {**updated_rarity.model_dump(), "id": rarity_id}

    raise HTTPException(status_code=404, detail="Rarity not found")


@router.delete("/{rarity_id}", status_code=204)
@inject
async def delete_rarity(
        rarity_id: int,
        service: IRarityService = Depends(Provide[Container.rarity_service]),
) -> None:
    """An endpoint for deleting raritys.

    Args:
        rarity_id (int): The id of the rarity.
        service (IcontinentService, optional): The injected service dependency.

    Raises:
        HTTPException: 404 if rarity does not exist.
    """

    if await service.get_by_id(rarity_id=rarity_id):
        await service.delete_rarity(rarity_id)

        return

    raise HTTPException(status_code=404, detail="Rarity not found")