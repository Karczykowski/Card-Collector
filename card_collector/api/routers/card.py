"""A module containing continent endpoints."""

from typing import List
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

@router.get("/all", response_model=List[Card], status_code=200)
@inject
async def get_all_cards(
        service: ICardService = Depends(Provide[Container.card_service]),
) -> List:
    """An endpoint for getting all cards.

    Args:
        service (ICardService, optional): The injected service dependency.

    Returns:
        List: The card attributes collection.
    """

    cards = await service.get_all()

    return cards

@router.get("/all/{rarity_id}", response_model=List[Card], status_code=200)
@inject
async def get_all_by_rarity(
        rarity_id: int,
        service: ICardService = Depends(Provide[Container.card_service]),
) -> List:
    """An endpoint for getting all cards by a given rarity.

    Args:
        rarity_id (int): The id of the rarity
        service (ICardService, optional): The injected service dependency.

    Returns:
        List: The card attributes collection.
    """

    cards = await service.get_all_by_rarity(rarity_id)

    return cards


@router.get("/{card_id}",response_model=Card,status_code=200,)
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
        service (ICardService, optional): The injected service dependency.

    Raises:
        HTTPException: 404 if card does not exist.
    """

    if await service.get_by_id(card_id=card_id):
        await service.delete_card(card_id)

        return

    raise HTTPException(status_code=404, detail="Card not found")

@router.get("/random/{rarity_id}",response_model=List[Card],status_code=200,)
@inject
async def get_random_cards_by_rarity(
        amount: int,
        rarity_id: int,
        service: ICardService = Depends(Provide[Container.card_service]),
) -> List | None:
    """An endpoint for getting random card by rarity id.

    Args:
        amount: amount of cards to generate
        rarity_id (int): The id of the rarity.
        service (ICardService, optional): The injected service dependency.

    Returns:
        dict | None: The card details.
    """
    if await get_all_by_rarity(rarity_id):
        return await service.get_random_cards_by_rarity(amount, rarity_id)

    raise HTTPException(status_code=404, detail="Rarity not found")

@router.get("/random/",response_model=List[Card],status_code=200,)
@inject
async def get_random_cards(
        amount: int,
        service: ICardService = Depends(Provide[Container.card_service]),
) -> List | None:
    """An endpoint for getting random card.

    Args:
        amount: amount of cards to generate
        service (ICardService, optional): The injected service dependency.

    Returns:
        Card | None: The card details.
    """
    return await service.get_random_cards(amount)
