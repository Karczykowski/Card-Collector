from card_collector.core.domains.trade_offer import TradeOffer, TradeOfferIn
from card_collector.core.domains.profile_collection import ProfileCollectionIn
from card_collector.core.services.i_collection_integration_service import ICollectionIntegrationService
from card_collector.core.services.i_profile_collection_service import IProfileCollectionService
from card_collector.core.services.i_trade_offer_service import ITradeOfferService

class CollectionIntegrationService(ICollectionIntegrationService):

    _profile_collection_service: IProfileCollectionService
    _trade_offer_service: ITradeOfferService

    def __init__(
            self,
            profile_collection_service: IProfileCollectionService,
            trade_offer_service: ITradeOfferService
    ) -> None:
        """
        The initializer of the profile_collection service.

        Args:
            profile_collection_service (IProfileCollectionService): The reference to the profile collection service.
            trade_offer_service (ITradeOfferService): The reference to the trade offer service.
        """
        self._profile_collection_service = profile_collection_service
        self._trade_offer_service =  trade_offer_service

    async def add_trade_offer(self, data: TradeOfferIn) -> TradeOffer | None:
        """
        The method adding new trade offer to the data storage, and completing it if its required.

        Args:
            data (TradeOfferIn): The details of the new trade offer.

        Returns:
            TradeOffer | None: Full details of the newly added trade offer.
        """
        trade_offer = await self._trade_offer_service.get_by_offer(data.card_wanted, data.card_offered)

        if trade_offer:
            profile_collection_original_poster =\
                await self._profile_collection_service.get_all_profile_collections_by_profile_id_and_card_id(
                    trade_offer.profile_posted,
                    trade_offer.card_offered)
            profile_collection_new_poster =\
                await self._profile_collection_service.get_all_profile_collections_by_profile_id_and_card_id(
                    data.profile_posted,
                    data.card_offered)

            await self._trade_offer_service.delete_trade_offer(trade_offer.id)

            await self._profile_collection_service.delete_profile_collection(profile_collection_original_poster[0].id)
            await self._profile_collection_service.delete_profile_collection(profile_collection_new_poster[0].id)

            await self._profile_collection_service.add_profile_collection(ProfileCollectionIn(
                profile_id=data.profile_posted,
                card_id=trade_offer.card_offered))
            await self._profile_collection_service.add_profile_collection(ProfileCollectionIn(
                profile_id=trade_offer.profile_posted,
                card_id=data.card_offered))
            return trade_offer
        else:
            return await self._trade_offer_service.add_trade_offer(data)
