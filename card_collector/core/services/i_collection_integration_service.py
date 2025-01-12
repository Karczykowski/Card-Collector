"""Module containing profile_collection service abstractions."""

from abc import ABC, abstractmethod
from typing import List

from card_collector.core.domains.trade_offer import TradeOffer, TradeOfferIn


class ICollectionIntegrationService(ABC):
    """A class representing profile_collection repository."""

    @abstractmethod
    async def add_trade_offer(self, data: TradeOfferIn) -> TradeOffer | None:
        """The method adding new trade_offer to the data storage.

        Args:
            data (TradeOfferIn): The details of the new trade_offer.

        Returns:
            TradeOffer | None: Full details of the newly added trade_offer.
        """