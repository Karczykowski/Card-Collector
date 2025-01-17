from abc import ABC, abstractmethod

from card_collector.core.domains.trade_offer import TradeOffer, TradeOfferIn

class ICollectionIntegrationService(ABC):

    @abstractmethod
    async def add_trade_offer(self, data: TradeOfferIn) -> TradeOffer | None:
        """
        The method adding new trade offer to the data storage, and completing it if its required.

        Args:
            data (TradeOfferIn): The details of the new trade offer.

        Returns:
            TradeOffer | None: Details of the newly added trade offer.
        """
