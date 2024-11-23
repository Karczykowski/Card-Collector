"""A module containing continent endpoints."""

from typing import Iterable
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException

from card_collector.container import Container
from card_collector.core.domains.card import Card, CardIn
from card_collector.core.services.i_card_service import ICardService

router = APIRouter()


@router.post("/create", response_model=Card, status_code=201)
@inject
async def create_card(
        card: CardIn,
        service: ICardService = Depends(Provide[Container.card_service]),
) -> dict:
    """An endpoint for adding new card.

    Args:
        card (CardIn): The card data.
        service (ICardService, optional): The injected service dependency.

    Returns:
        dict: The new card attributes.
    """

    new_card = await service.add_card(card)

    return new_card.model_dump() if new_card else {}


@router.get("/all", response_model=Iterable[Card], status_code=200)
@inject
async def get_all_cards(
        service: ICardService = Depends(Provide[Container.card_service]),
) -> Iterable:
    """An endpoint for getting all cards.

    Args:
        service (ICardService, optional): The injected service dependency.

    Returns:
        Iterable: The card attributes collection.
    """

    cards = await service.get_all()

    return cards



@router.get(
    "/{card_id}",
    response_model=Card,
    status_code=200,
)
@inject
async def get_card_by_id(
        card_id: int,
        service: ICardService = Depends(Provide[Container.card_service]),
) -> dict | None:
    """An endpoint for getting card by id.

    Args:
        card_id (int): The id of the card.
        service (ICardService, optional): The injected service dependency.

    Returns:
        dict | None: The card details.
    """

    if card := await service.get_by_id(card_id):
        return card.model_dump()

    raise HTTPException(status_code=404, detail="Card not found")


@router.get(
    "/user/{user_id}",
    response_model=Iterable[Card],
    status_code=200,
)
@inject
async def get_cards_by_user(
        user_id: int,
        service: ICardService = Depends(Provide[Container.card_service]),
) -> Iterable:
    """An endpoint for getting cards by user who added them.

    Args:
        user_id (int): The id of the user.
        service (ICardService, optional): The injected service dependency.

    Returns:
        Iterable: The card details collection.
    """

    cards = await service.get_by_user(user_id)

    return cards


@router.put("/{card_id}", response_model=Card, status_code=201)
@inject
async def update_card(
        card_id: int,
        updated_card: CardIn,
        service: ICardService = Depends(Provide[Container.card_service]),
) -> dict:
    """An endpoint for updating card data.

    Args:
        card_id (int): The id of the card.
        updated_card (CardIn): The updated card details.
        service (ICardtService, optional): The injected service dependency.

    Raises:
        HTTPException: 404 if card does not exist.

    Returns:
        dict: The updated card details.
    """

    if await service.get_by_id(card_id=card_id):
        await service.update_card(
            card_id=card_id,
            data=updated_card,
        )
        return {**updated_card.model_dump(), "id": card_id}

    raise HTTPException(status_code=404, detail="Card not found")


@router.delete("/{card_id}", status_code=204)
@inject
async def delete_card(
        card_id: int,
        service: ICardService = Depends(Provide[Container.card_service]),
) -> None:
    """An endpoint for deleting cards.

    Args:
        card_id (int): The id of the card.
        service (IcontinentService, optional): The injected service dependency.

    Raises:
        HTTPException: 404 if card does not exist.
    """

    if await service.get_by_id(card_id=card_id):
        await service.delete_card(card_id)

        return

    raise HTTPException(status_code=404, detail="Card not found")