from abc import ABC, abstractmethod
from typing import Any, List

from card_collector.core.domains.trade_offer import TradeOfferIn

class ITradeOfferRepository(ABC):

    @abstractmethod
    async def get_all_trade_offers(self) -> List[Any]:
        """
        The abstract class getting all trade offers from the database.

        Returns:
            List[Any]: Trade Offers in the database.
        """
    @abstractmethod
    async def get_all_by_card_offered(self, card_offered: int) -> List[Any]:
        """
        The abstract class getting all trade offers with a given card id from the database.

        Args:
            card_offered (int): the id of card offered.

        Returns:
            List[Any]: Trade Offers in the database.
        """

    @abstractmethod
    async def get_all_by_card_wanted(self, card_wanted: int) -> List[Any]:
        """
        The abstract class getting all trade offers with a given card id from the database.

        Args:
            card_wanted (int): the id of card wanted.

        Returns:
            List[Any]: Trade Offers in the database.
        """

    @abstractmethod
    async def get_by_id(self, trade_offer_id: int) -> Any | None:
        """
        The abstract class getting trade offer with a given id from the database.

        Args:
            trade_offer_id (int): The id of the trade offer.

        Returns:
            Any | None: The trade offer details.
        """

    @abstractmethod
    async def get_by_profile_id_and_card_offered_id(self, profile_id: int, card_offered_id: int) -> Any | None:
        """
        The abstract class getting trade offer with a given profile and card id from the database.

        Args:
            profile_id (int): the id of profile.
            card_offered_id (int): the id of card offered.

        Returns:
            Any | None: The trade offer details.
        """

    @abstractmethod
    async def get_by_offer(self, card_offered: int, card_wanted: int) -> Any | None:
        """
        The abstract class getting trade offer with a given card offered and wanted id from the database.

        Args:
            card_offered (int): the id of card offered.
            card_wanted (int): the id of card wanted.

        Returns:
            TradeOffer | None: The trade offer details.
        """

    @abstractmethod
    async def add_trade_offer(self, data: TradeOfferIn) -> Any | None:
        """
        The abstract class adding new trade offer to the database.

        Args:
            data (TradeOfferIn): The details of the new trade offer.

        Returns:
            Any | None: The newly added trade offer.
        """

    @abstractmethod
    async def update_trade_offer(
            self,
            trade_offer_id: int,
            data: TradeOfferIn,
    ) -> Any | None:
        """
        The abstract class updating trade offer data in the database.

        Args:
            trade_offer_id (int): The id of the trade offer.
            data (TradeOfferIn): The details of the updated trade offer.

        Returns:
            Any | None: The updated trade offer details.
        """

    @abstractmethod
    async def delete_trade_offer(self, trade_offer_id: int) -> bool:
        """
        The abstract class removing trade offer from the database.

        Args:
            trade_offer_id (int): The id of the trade offer.

        Returns:
            bool: Success of the operation.
        """
