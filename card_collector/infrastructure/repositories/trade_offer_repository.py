"""Module containing trade_offer repository implementation."""

from typing import Any, List

from asyncpg import Record  # type: ignore
from sqlalchemy import select, join, and_

from card_collector.core.repositories.i_trade_offer_repository import ITradeOfferRepository
from card_collector.core.domains.trade_offer import TradeOffer, TradeOfferIn
from card_collector.db import (
    trade_offer_table,
    database,
)

class TradeOfferRepository(ITradeOfferRepository):
    """A class representing continent DB repository."""

    async def get_all_trade_offers(self) -> List[Any]:
        """The method getting all trade_offers from the data storage.

        Returns:
            List[Any]: TradeOffers in the data storage.
        """

        query = (
            select(trade_offer_table)
        )
        trade_offers = await database.fetch_all(query)

        return [TradeOffer.from_record(trade_offer) for trade_offer in trade_offers]

    async def get_all_by_card_offered(self, card_offered: int) -> List[Any]:
        """The method getting all trade_offers from the data storage.

        Args:
            card_offered (int): the id of card_offered.

        Returns:
            List[Any]: TradeOffers in the data storage.
        """

        query = (
            select(trade_offer_table)
            .where(trade_offer_table.c.card_offered == card_offered)
        )
        trade_offers = await database.fetch_all(query)

        return [TradeOffer.from_record(trade_offer) for trade_offer in trade_offers]

    async def get_all_by_card_wanted(self, card_wanted: int) -> List[Any]:
        """The method getting all trade_offers from the data storage.

        Args:
            card_wanted (int): the id of card_wanted.

        Returns:
            List[Any]: TradeOffers in the data storage.
        """

        query = (
            select(trade_offer_table)
            .where(trade_offer_table.c.card_wanted == card_wanted)
        )
        trade_offers = await database.fetch_all(query)

        return [TradeOffer.from_record(trade_offer) for trade_offer in trade_offers]


    async def get_by_id(self, trade_offer_id: int) -> Any | None:
        """The method getting trade_offer by provided id.

        Args:
            trade_offer_id (int): The id of the trade_offer.

        Returns:
            Any | None: The trade_offer details.
        """

        trade_offer = await self._get_by_id(trade_offer_id)

        return TradeOffer.from_record(trade_offer) if trade_offer else None

    async def get_by_profile_id_and_card_offered_id(self, profile_id: int, card_offered_id: int) -> Any | None:
        """The method getting trade_offer by provided id.

        Args:
            profile_id (int): the id of profile.
            card_offered_id (int): the id of card_offered.

        Returns:
            Any | None: The trade_offer details.
        """

        query = (
            trade_offer_table.select()
            .where(
                and_(
                    trade_offer_table.c.profile_posted == profile_id,
                    trade_offer_table.c.card_offered == card_offered_id)
            )
        )
        trade_offers = await database.fetch_all(query)

        return [TradeOffer.from_record(trade_offer) for trade_offer in trade_offers]

    async def add_trade_offer(self, data: TradeOfferIn) -> Any | None:
        """The method adding new trade_offer to the data storage.

        Args:
            data (TradeOfferIn): The details of the new trade_offer.

        Returns:
            TradeOffer: Full details of the newly added trade_offer.

        Returns:
            Any | None: The newly added trade_offer.
        """

        query = trade_offer_table.insert().values(**data.model_dump())
        new_trade_offer_id = await database.execute(query)
        new_trade_offer = await self._get_by_id(new_trade_offer_id)

        return TradeOffer(**dict(new_trade_offer)) if new_trade_offer else None

    async def update_trade_offer(
            self,
            trade_offer_id: int,
            data: TradeOfferIn,
    ) -> Any | None:
        """The method updating trade_offer data in the data storage.

        Args:
            trade_offer_id (int): The id of the trade_offer.
            data (TradeOfferIn): The details of the updated trade_offer.

        Returns:
            Any | None: The updated trade_offer details.
        """

        if self._get_by_id(trade_offer_id):
            query = (
                trade_offer_table.update()
                .where(trade_offer_table.c.id == trade_offer_id)
                .values(**data.model_dump())
            )
            await database.execute(query)

            trade_offer = await self._get_by_id(trade_offer_id)

            return TradeOffer(**dict(trade_offer)) if trade_offer else None

        return None

    async def delete_trade_offer(self, trade_offer_id: int) -> bool:
        """The method updating removing trade_offer from the data storage.

        Args:
            trade_offer_id (int): The id of the trade_offer.

        Returns:
            bool: Success of the operation.
        """

        if await self._get_by_id(trade_offer_id):
            query = trade_offer_table \
                .delete() \
                .where(trade_offer_table.c.id == trade_offer_id)
            await database.execute(query)

            return True

        return False

    async def _get_by_id(self, trade_offer_id: int) -> Record | None:
        """A private method getting trade_offer from the DB based on its ID.

        Args:
            trade_offer_id (int): The ID of the trade_offer.

        Returns:
            Any | None: TradeOffer record if exists.
        """

        query = (
            trade_offer_table.select()
            .where(trade_offer_table.c.id == trade_offer_id)
        )

        return await database.fetch_one(query)