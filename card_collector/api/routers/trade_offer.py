"""A module containing continent endpoints."""

from typing import List
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException

from card_collector.container import Container
from card_collector.core.domains.trade_offer import TradeOffer, TradeOfferIn
from card_collector.core.services.i_trade_offer_service import ITradeOfferService
from card_collector.core.repositories.i_profile_repository import IProfileRepository
from card_collector.core.repositories.i_card_repository import ICardRepository
from card_collector.core.repositories.i_profile_collection_repository import IProfileCollectionRepository

router = APIRouter()


@router.post("/create", response_model=TradeOffer, status_code=201)
@inject
async def create_trade_offer(
        trade_offer: TradeOfferIn,
        service: ITradeOfferService = Depends(Provide[Container.trade_offer_service]),
        profile_repository: IProfileRepository = Depends(Provide[Container.profile_repository]),
        card_repository: ICardRepository = Depends(Provide[Container.card_repository]),
        profile_collection_repository: IProfileCollectionRepository = Depends(Provide[Container.profile_collection_repository])
) -> dict:
    """An endpoint for adding new trade_offer.

    Args:
        trade_offer (TradeOfferIn): The trade_offer data.
        service (ITradeOfferService, optional): The injected service dependency.
        profile_repository: The injected profile_repository.
        card_repository: The Injected card_repository.
        profile_collection_repository: The injected profile_collection

    Returns:
        dict: The new trade_offer attributes.
    """
    if await profile_repository.get_by_id(trade_offer.profile_posted):
        if await card_repository.get_by_id(trade_offer.card_wanted):
            if await profile_collection_repository.get_profile_collection_by_profile_id_and_card_id(trade_offer.card_offered, trade_offer.profile_posted):

                new_trade_offer = await service.add_trade_offer(trade_offer)
                return new_trade_offer.model_dump() if new_trade_offer else {}

            raise HTTPException(status_code=404, detail="Couldn't find specified card in profile collection")
        raise HTTPException(status_code=404, detail="Card wanted not found in card data base")
    raise HTTPException(status_code=404, detail="Profile not found")



@router.get("/all", response_model=List[TradeOffer], status_code=200)
@inject
async def get_all_trade_offers(
        service: ITradeOfferService = Depends(Provide[Container.trade_offer_service]),
) -> List:
    """An endpoint for getting all trade_offers.

    Args:
        service (ITradeOfferService, optional): The injected service dependency.

    Returns:
        List: The trade_offer attributes collection.
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

    raise HTTPException(status_code=404, detail="Trade Offer not found")

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

    raise HTTPException(status_code=404, detail="Trade Offer not found")


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

    raise HTTPException(status_code=404, detail="Trade Offer not found")
