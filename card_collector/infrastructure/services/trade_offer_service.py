"""Module containing continent service implementation."""
import random
from typing import Iterable, List

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

    async def get_all(self) -> Iterable[TradeOffer]:
        """The method getting all trade_offers from the repository.

        Returns:
            Iterable[TradeOffer]: All trade_offers.
        """

        return await self._repository.get_all_trade_offers()

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
