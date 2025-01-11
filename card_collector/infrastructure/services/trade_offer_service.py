"""Module containing continent service implementation."""
import random
from typing import List

from card_collector.core.domains.trade_offer import TradeOffer, TradeOfferIn
from card_collector.core.repositories.i_trade_offer_repository import ITradeOfferRepository
from card_collector.core.services.i_trade_offer_service import ITradeOfferService


class TradeOfferService(ITradeOfferService):
    """A class implementing the trade_offer service."""

    _repository: ITradeOfferRepository

    def __init__(self, repository: ITradeOfferRepository) -> None:
        """The initializer of the `trade_offer service`.

        Args:
            repository (ITradeOfferRepository): The reference to the repository.
        """
        self._repository = repository

    async def get_all(self) -> List[TradeOffer]:
        """The method getting all trade_offers from the repository.

        Returns:
            List[TradeOffer]: All trade_offers.
        """

        return await self._repository.get_all_trade_offers()

    async def get_all_by_card_offered(self, card_offered: int) -> List[TradeOffer]:
        """The method getting all trade_offers from the repository.

        Args:
            card_offered (int): the id of card_offered.

        Returns:
            List[TradeOffer]: All trade_offers.
        """

        return await self._repository.get_all_by_card_offered(card_offered)

    async def get_all_by_card_wanted(self, card_wanted: int) -> List[TradeOffer]:
        """The method getting all trade_offers from the repository.

        Args:
            card_wanted (int): the id of card_wanted.
        Returns:
            List[TradeOffer]: All trade_offers.
        """

        return await self._repository.get_all_by_card_wanted(card_wanted)

    async def get_all_by_profile_id_and_card_offered_id(self, profile_id: int, card_offered_id: int) -> List[TradeOffer] | None:
        """The method getting trade_offer by provided id.

        Args:
            profile_id (int): the id of profile.
            card_offered_id (int): the id of card_offered.

        Returns:
            TradeOffer | None: The trade_offer details.
        """

        return await self._repository.get_by_profile_id_and_card_offered_id(profile_id, card_offered_id)

    async def get_by_id(self, trade_offer_id: int) -> TradeOffer | None:
        """The method getting trade_offer by provided id.

        Args:
            trade_offer_id (int): The id of the trade_offer.

        Returns:
            TradeOffer | None: The trade_offer details.
        """

        return await self._repository.get_by_id(trade_offer_id)

    async def add_trade_offer(self, data: TradeOfferIn) -> TradeOffer | None:
        """The method adding new trade_offer to the data storage.

        Args:
            data (TradeOfferIn): The details of the new trade_offer.

        Returns:
            TradeOffer | None: Full details of the newly added trade_offer.
        """

        return await self._repository.add_trade_offer(data)

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

        return await self._repository.update_trade_offer(
            trade_offer_id=trade_offer_id,
            data=data,
        )

    async def delete_trade_offer(self, trade_offer_id: int) -> bool:
        """The method updating removing trade_offer from the data storage.

        Args:
            trade_offer_id (int): The id of the trade_offer.

        Returns:
            bool: Success of the operation.
        """

        return await self._repository.delete_trade_offer(trade_offer_id)

    async def delete_trade_offer_by_profile_id_and_card_offered_id(self, profile_id: int, card_offered_id: int) -> List[bool]:
        """The method updating removing trade_offer from the data storage.

        Args:
            profile_id (int): the id of profile.
            card_offered_id (int): the id of card_offered.

        Returns:
            bool: Success of the operation.
        """
        trade_offers = await self.get_all_by_profile_id_and_card_offered_id(profile_id, card_offered_id)
        return [await self._repository.delete_trade_offer(trade_offer.id) for trade_offer in trade_offers]
