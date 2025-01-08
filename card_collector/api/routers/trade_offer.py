"""A module containing continent endpoints."""

from typing import Iterable
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException

from card_collector.container import Container
from card_collector.core.domains.trade_offer import TradeOffer, TradeOfferIn
from card_collector.core.services.i_trade_offer_service import ITradeOfferService

router = APIRouter()


@router.post("/create", response_model=TradeOffer, status_code=201)
@inject
async def create_trade_offer(
        trade_offer: TradeOfferIn,
        service: ITradeOfferService = Depends(Provide[Container.trade_offer_service]),
) -> dict:
    """An endpoint for adding new trade_offer.

    Args:
        trade_offer (TradeOfferIn): The trade_offer data.
        service (ITradeOfferService, optional): The injected service dependency.

    Returns:
        dict: The new trade_offer attributes.
    """

    new_trade_offer = await service.add_trade_offer(trade_offer)

    return new_trade_offer.model_dump() if new_trade_offer else {}

@router.get("/all", response_model=Iterable[TradeOffer], status_code=200)
@inject
async def get_all_trade_offers(
        service: ITradeOfferService = Depends(Provide[Container.trade_offer_service]),
) -> Iterable:
    """An endpoint for getting all trade_offers.

    Args:
        service (ITradeOfferService, optional): The injected service dependency.

    Returns:
        Iterable: The trade_offer attributes collection.
    """

    trade_offers = await service.get_all()

    return trade_offers

@router.get("/{trade_offer_id}",response_model=TradeOffer,status_code=200,)
@inject
async def get_trade_offer_by_id(
        trade_offer_id: int,
        service: ITradeOfferService = Depends(Provide[Container.trade_offer_service]),
) -> dict | None:
    """An endpoint for getting trade_offer by id.

    Args:
        trade_offer_id (int): The id of the trade_offer.
        service (ITradeOfferService, optional): The injected service dependency.

    Returns:
        dict | None: The trade_offer details.
    """

    if trade_offer := await service.get_by_id(trade_offer_id):
        return trade_offer.model_dump()

    raise HTTPException(status_code=404, detail="TradeOffer not found")

@router.put("/{trade_offer_id}", response_model=TradeOffer, status_code=201)
@inject
async def update_trade_offer(
        trade_offer_id: int,
        updated_trade_offer: TradeOfferIn,
        service: ITradeOfferService = Depends(Provide[Container.trade_offer_service]),
) -> dict:
    """An endpoint for updating trade_offer data.

    Args:
        trade_offer_id (int): The id of the trade_offer.
        updated_trade_offer (TradeOfferIn): The updated trade_offer details.
        service (ITradeOffertService, optional): The injected service dependency.

    Raises:
        HTTPException: 404 if trade_offer does not exist.

    Returns:
        dict: The updated trade_offer details.
    """

    if await service.get_by_id(trade_offer_id=trade_offer_id):
        await service.update_trade_offer(
            trade_offer_id=trade_offer_id,
            data=updated_trade_offer,
        )
        return {**updated_trade_offer.model_dump(), "id": trade_offer_id}

    raise HTTPException(status_code=404, detail="TradeOffer not found")


@router.delete("/{trade_offer_id}", status_code=204)
@inject
async def delete_trade_offer(
        trade_offer_id: int,
        service: ITradeOfferService = Depends(Provide[Container.trade_offer_service]),
) -> None:
    """An endpoint for deleting trade_offers.

    Args:
        trade_offer_id (int): The id of the trade_offer.
        service (ITradeOfferService, optional): The injected service dependency.

    Raises:
        HTTPException: 404 if trade_offer does not exist.
    """

    if await service.get_by_id(trade_offer_id=trade_offer_id):
        await service.delete_trade_offer(trade_offer_id)

        return

    raise HTTPException(status_code=404, detail="TradeOffer not found")
