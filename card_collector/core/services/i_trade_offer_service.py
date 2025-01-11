"""Module containing trade_offer service abstractions."""

from abc import ABC, abstractmethod
from typing import List

from card_collector.core.domains.trade_offer import TradeOffer, TradeOfferIn


class ITradeOfferService(ABC):
    """A class representing trade_offer repository."""

    @abstractmethod
    async def get_all(self) -> List[TradeOffer]:
        """The method getting all trade_offers from the repository.

        Returns:
            List[TradeOffer]: All trade_offers.
        """

    @abstractmethod
    async def get_all_by_card_offered(self, card_offered: int) -> List[TradeOffer] | None:
        """The method getting trade_offer by provided id.

        Args:
            card_offered (int): The id of the trade_offer.

        Returns:
            List[TradeOffer] The trade_offer details.
        """

    @abstractmethod
    async def get_all_by_card_wanted(self, card_wanted: int) -> List[TradeOffer] | None:
        """The method getting trade_offer by provided id.

        Args:
            card_wanted (int): The id of the trade_offer.

        Returns:
            TradeOffer | None: The trade_offer details.
        """

    @abstractmethod
    async def get_all_by_profile_id_and_card_offered_id(self, profile_id: int, card_offered_id: int) -> TradeOffer | None:
        """The method getting trade_offer by provided id.

        Args:
            profile_id (int): the id of profile.
            card_offered_id (int): the id of card_offered.

        Returns:
            TradeOffer | None: The trade_offer details.
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

    @abstractmethod
    async def delete_trade_offer_by_profile_id_and_card_offered_id(self, profile_id: int, card_offered_id: int) -> List[bool]:
        """The method updating removing trade_offer from the data storage.

        Args:
            profile_id (int): the id of profile.
            card_offered_id (int): the id of card_offered.

        Returns:
            bool: Success of the operation.
        """
