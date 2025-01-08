"""Module containing trade_offer service abstractions."""

from abc import ABC, abstractmethod
from typing import Iterable, List

from card_collector.core.domains.trade_offer import TradeOffer, TradeOfferIn


class ITradeOfferService(ABC):
    """A class representing trade_offer repository."""

    @abstractmethod
    async def get_all(self) -> Iterable[TradeOffer]:
        """The method getting all trade_offers from the repository.

        Returns:
            Iterable[TradeOffer]: All trade_offers.
        """

    @abstractmethod
    async def get_by_id(self, trade_offer_id: int) -> TradeOffer | None:
        """The method getting trade_offer by provided id.

        Args:
            trade_offer_id (int): The id of the trade_offer.

        Returns:
            TradeOffer | None: The trade_offer details.
        """


    @abstractmethod
    async def add_trade_offer(self, data: TradeOfferIn) -> TradeOffer | None:
        """The method adding new trade_offer to the data storage.

        Args:
            data (TradeOfferIn): The details of the new trade_offer.

        Returns:
            TradeOffer | None: Full details of the newly added trade_offer.
        """

    @abstractmethod
    async def update_trade_offer(
            self,
            trade_offer_id: int,
            data: TradeOfferIn,
    ) -> TradeOffer | None:
        """The method updating trade_offer data in the data storage.

        Args:
            trade_offer_id (int): The id of the trade_offer.
            data (TradeOfferIn): The details of the updated trade_offer.

        Returns:
            TradeOffer | None: The updated trade_offer details.
        """

    @abstractmethod
    async def delete_trade_offer(self, trade_offer_id: int) -> bool:
        """The method updating removing trade_offer from the data storage.

        Args:
            trade_offer_id (int): The id of the trade_offer.

        Returns:
            bool: Success of the operation.
        """
