from typing import List

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException

from card_collector.container import Container
from card_collector.core.domains.trade_offer import TradeOffer, TradeOfferIn
from card_collector.core.services.i_trade_offer_service import ITradeOfferService
from card_collector.core.services.i_profile_service import IProfileService
from card_collector.core.services.i_card_service import ICardService
from card_collector.core.services.i_profile_collection_service import IProfileCollectionService
from card_collector.core.services.i_collection_integration_service import ICollectionIntegrationService

router = APIRouter()

@router.post("/create", response_model=TradeOffer, status_code=201)
@inject
async def create_trade_offer(
        trade_offer: TradeOfferIn,
        profile_service: IProfileService = Depends(Provide[Container.profile_service]),
        card_service: ICardService = Depends(Provide[Container.card_service]),
        profile_collection_service: IProfileCollectionService = Depends(Provide[Container.profile_collection_service]),
        collection_integration_service: ICollectionIntegrationService = Depends(Provide[Container.collection_integration_service])
) -> dict:
    """
    An endpoint for adding new trade offer.

    Args:
        trade_offer (TradeOfferIn): The trade_offer data.
        profile_service: The injected profile service dependency.
        card_service: The Injected card service dependency.
        profile_collection_service: The injected profile collection dependency.
        collection_integration_service (ICollectionIntegrationService): The injected collection integration service.

    Returns:
        dict: The new trade offer attributes.

    Raises:
        HTTPException: 404 if data does not exist.
    """

    if await profile_service.get_by_id(trade_offer.profile_posted):
        if await card_service.get_by_id(trade_offer.card_wanted):
            if await profile_collection_service.get_all_profile_collections_by_profile_id_and_card_id(
                    trade_offer.card_offered,
                    trade_offer.profile_posted):

                new_trade_offer = await collection_integration_service.add_trade_offer(trade_offer)
                return new_trade_offer.model_dump() if new_trade_offer else {}

            raise HTTPException(status_code=404, detail="Card offered not found")
        raise HTTPException(status_code=404, detail="Card wanted not found")
    raise HTTPException(status_code=404, detail="Profile not found")



@router.get("/all", response_model=List[TradeOffer], status_code=200)
@inject
async def get_all_trade_offers(
        service: ITradeOfferService = Depends(Provide[Container.trade_offer_service]),
) -> List:
    """
    An endpoint for getting all trade offers.

    Args:
        service (ITradeOfferService): The injected service dependency.

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
    """
    An endpoint for getting trade_offer by id.

    Args:
        trade_offer_id (int): The id of the trade_offer.
        service (ITradeOfferService): The injected service dependency.

    Returns:
        dict | None: The trade_offer details.

    Raises:
        HTTPException: 404 if trade offer does not exist.
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
        profile_service: IProfileService = Depends(Provide[Container.profile_service]),
        card_service: ICardService = Depends(Provide[Container.card_service]),
        profile_collection_service: IProfileCollectionService = Depends(Provide[Container.profile_collection_service]),
) -> dict:
    """
    An endpoint for updating trade offer.

    Args:
        trade_offer_id (int): The id of the trade_offer.
        updated_trade_offer (TradeOfferIn): The updated trade offer details.
        service (ITradeOfferService): The injected service dependency.
        profile_service (IProfileService): The injected profile service dependency.
        card_service (ICardService): The injected card service dependency.
        profile_collection_service (IProfileCollectionService): The injected profile collection dependency.

    Returns:
        dict: The updated trade offer details.

    Raises:
        HTTPException: 404 if data does not exist.
    """

    if await service.get_by_id(trade_offer_id=trade_offer_id):
        if await profile_service.get_by_id(updated_trade_offer.profile_posted):
            if await profile_collection_service.get_all_profile_collections_by_profile_id_and_card_id(
                    updated_trade_offer.card_offered,
                    updated_trade_offer.profile_posted):
                if await card_service.get_by_id(updated_trade_offer.card_wanted):
                    await service.update_trade_offer(
                        trade_offer_id=trade_offer_id,
                        data=updated_trade_offer,
                    )
                    return {**updated_trade_offer.model_dump(), "id": trade_offer_id}
                raise HTTPException(status_code=404, detail="Card wanted not found")
            raise HTTPException(status_code=404, detail="Card offered not found")
        raise HTTPException(status_code=404, detail="Profile not found")
    raise HTTPException(status_code=404, detail="Trade Offer not found")


@router.delete("/{trade_offer_id}", status_code=204)
@inject
async def delete_trade_offer(
        trade_offer_id: int,
        service: ITradeOfferService = Depends(Provide[Container.trade_offer_service]),
) -> None:
    """
    An endpoint for deleting trade offers.

    Args:
        trade_offer_id (int): The id of the trade_offer.
        service (ITradeOfferService): The injected service dependency.

    Raises:
        HTTPException: 404 if trade offer does not exist.
    """

    if await service.get_by_id(trade_offer_id=trade_offer_id):
        await service.delete_trade_offer(trade_offer_id)

        return

    raise HTTPException(status_code=404, detail="Trade Offer not found")
