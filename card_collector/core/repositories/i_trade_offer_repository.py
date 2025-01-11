"""Module containing trade_offer repository abstractions."""

from abc import ABC, abstractmethod
from typing import Any, List

from card_collector.core.domains.trade_offer import TradeOfferIn


class ITradeOfferRepository(ABC):
    """An abstract class representing protocol of continent repository."""

    @abstractmethod
    async def get_all_trade_offers(self) -> List[Any]:
        """The abstract getting all trade_offers from the data storage.

        Returns:
            List[Any]: TradeOffers in the data storage.
        """
    @abstractmethod
    async def get_all_by_card_offered(self, card_offered: int) -> List[Any]:
        """The abstract getting all trade_offers from the data storage.

        Args:
            card_offered (int): the id of card_offered.

        Returns:
            List[Any]: TradeOffers in the data storage.
        """

    @abstractmethod
    async def get_all_by_card_wanted(self, card_wanted: int) -> List[Any]:
        """The abstract getting all trade_offers from the data storage.

        Args:
            card_wanted (int): the id of card_wanted.

        Returns:
            List[Any]: TradeOffers in the data storage.
        """

    @abstractmethod
    async def get_by_profile_id_and_card_offered_id(self, profile_id: int, card_offered_id: int) -> Any | None:
        """The abstract getting trade_offer by provided id.

        Args:
            profile_id (int): the id of profile.
            card_offered_id (int): the id of card_offered.

        Returns:
            Any | None: The trade_offer details.
        """

    @abstractmethod
    async def get_by_id(self, trade_offer_id: int) -> Any | None:
        """The abstract getting trade_offer by provided id.

        Args:
            trade_offer_id (int): The id of the trade_offer.

        Returns:
            Any | None: The trade_offer details.
        """

    @abstractmethod
    async def add_trade_offer(self, data: TradeOfferIn) -> Any | None:
        """The abstract adding new trade_offer to the data storage.

        Args:
            data (TradeOfferIn): The details of the new trade_offer.

        Returns:
            Any | None: The newly added trade_offer.
        """

    @abstractmethod
    async def update_trade_offer(
            self,
            trade_offer_id: int,
            data: TradeOfferIn,
    ) -> Any | None:
        """The abstract updating trade_offer data in the data storage.

        Args:
            trade_offer_id (int): The id of the trade_offer.
            data (TradeOfferIn): The details of the updated trade_offer.

        Returns:
            Any | None: The updated trade_offer details.
        """

    @abstractmethod
    async def delete_trade_offer(self, trade_offer_id: int) -> bool:
        """The abstract updating removing trade_offer from the data storage.

        Args:
            trade_offer_id (int): The id of the trade_offer.

        Returns:
            bool: Success of the operation.
        """
