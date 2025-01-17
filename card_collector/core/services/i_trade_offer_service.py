from abc import ABC, abstractmethod
from typing import List

from card_collector.core.domains.trade_offer import TradeOffer, TradeOfferIn

class ITradeOfferService(ABC):

    @abstractmethod
    async def get_all(self) -> List[TradeOffer]:
        """
        The method getting all trade offers from the repository.

        Returns:
            List[TradeOffer]: All trade offers.
        """

    @abstractmethod
    async def get_all_by_card_offered(self, card_offered: int) -> List[TradeOffer] | None:
        """
        The method getting trade offer with a given card offered id from the repository.

        Args:
            card_offered (int): The id of the card offered.

        Returns:
            List[TradeOffer] The trade offer details.
        """

    @abstractmethod
    async def get_all_by_card_wanted(self, card_wanted: int) -> List[TradeOffer] | None:
        """
        The method getting trade offer with a given card wanted id from the repository.

        Args:
            card_wanted (int): The id of the card wanted.

        Returns:
            TradeOffer | None: The trade offer details.
        """

    @abstractmethod
    async def get_all_by_profile_id_and_card_offered_id(
            self,
            profile_id: int,
            card_offered_id: int
    ) -> List[TradeOffer] | None:
        """
        The method getting all trade offers with a given profile and card offered id from the repository.

        Args:
            profile_id (int): the id of profile.
            card_offered_id (int): the id of card_offered.

        Returns:
            TradeOffer | None: The trade_offer details.
        """

    @abstractmethod
    async def get_by_id(self, trade_offer_id: int) -> TradeOffer | None:
        """
        The method getting trade offer with a given id.

        Args:
            trade_offer_id (int): The id of the trade offer.

        Returns:
            TradeOffer | None: The trade offer details.
        """

    @abstractmethod
    async def get_by_offer(self, card_offered: int, card_wanted: int) -> TradeOffer | None:
        """
        The method getting trade offer with a given offer.

        Args:
            card_offered (int): the id of card offered.
            card_wanted (int): the id of card wanted.

        Returns:
            TradeOffer | None: The trade offer details.
        """

    @abstractmethod
    async def add_trade_offer(self, data: TradeOfferIn) -> TradeOffer | None:
        """
        The method adding new trade offer to the database.

        Args:
            data (TradeOfferIn): The details of the new trade offer.

        Returns:
            TradeOffer | None: Full details of the newly added trade offer.
        """

    @abstractmethod
    async def update_trade_offer(
            self,
            trade_offer_id: int,
            data: TradeOfferIn,
    ) -> TradeOffer | None:
        """
        The method updating trade offer data in the database.

        Args:
            trade_offer_id (int): The id of the trade offer.
            data (TradeOfferIn): The details of the updated trade offer.

        Returns:
            TradeOffer | None: The updated trade offer details.
        """

    @abstractmethod
    async def delete_trade_offer(self, trade_offer_id: int) -> bool:
        """
        The method removing trade offer from the database.

        Args:
            trade_offer_id (int): The id of the trade_offer.

        Returns:
            bool: Success of the operation.
        """

    @abstractmethod
    async def delete_trade_offer_by_profile_id_and_card_offered_id(
            self,
            profile_id: int,
            card_offered_id: int
    ) -> List[bool]:
        """
        The method updating removing trade offer with a given profile and card offered id from the database.

        Args:
            profile_id (int): the id of profile.
            card_offered_id (int): the id of card offered.

        Returns:
            bool: Success of the operation.
        """
