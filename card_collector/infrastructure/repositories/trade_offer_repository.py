from typing import Any, List

from sqlalchemy import select, and_

from card_collector.core.repositories.i_trade_offer_repository import ITradeOfferRepository
from card_collector.core.domains.trade_offer import TradeOffer, TradeOfferIn
from card_collector.db import (
    trade_offer_table,
    database,
)

class TradeOfferRepository(ITradeOfferRepository):

    async def get_all_trade_offers(self) -> List[Any]:
        """
        The method getting all trade offers from the database.

        Returns:
            List[Any]: Trade Offers in the database.
        """

        query = (
            select(trade_offer_table)
        )
        trade_offers = await database.fetch_all(query)

        return [TradeOffer.from_record(trade_offer) for trade_offer in trade_offers]

    async def get_all_by_card_offered(self, card_offered: int) -> List[Any]:
        """
        The method getting all trade offers with a given card id from the database.

        Args:
            card_offered (int): the id of card offered.

        Returns:
            List[Any]: Trade Offers in the database.
        """

        query = (
            select(trade_offer_table)
            .where(trade_offer_table.c.card_offered == card_offered) # type: ignore
        )
        trade_offers = await database.fetch_all(query)

        return [TradeOffer.from_record(trade_offer) for trade_offer in trade_offers]

    async def get_all_by_card_wanted(self, card_wanted: int) -> List[Any]:
        """
        The method getting all trade offers with a given card id from the database.

        Args:
            card_wanted (int): the id of card wanted.

        Returns:
            List[Any]: Trade Offers in the database.
        """

        query = (
            select(trade_offer_table)
            .where(trade_offer_table.c.card_wanted == card_wanted) # type: ignore
        )
        trade_offers = await database.fetch_all(query)

        return [TradeOffer.from_record(trade_offer) for trade_offer in trade_offers]


    async def get_by_id(self, trade_offer_id: int) -> Any | None:
        """
        The method getting trade offer by provided id.

        Args:
            trade_offer_id (int): The id of the trade offer.

        Returns:
            Any | None: The trade offer details.
        """

        query = (
            trade_offer_table.select()
            .where(trade_offer_table.c.id == trade_offer_id)
        )

        trade_offer = await database.fetch_one(query)

        return TradeOffer.from_record(trade_offer) if trade_offer else None

    async def get_by_offer(self, card_offered: int, card_wanted: int) -> Any | None:
        """
        The method getting trade offer with a given offer.

        Args:
            card_offered (int): the id of card offered.
            card_wanted (int): the id of card wanted.

        Returns:
            TradeOffer | None: The trade offer details.
        """
        query = (
            trade_offer_table.select()
            .where(
                trade_offer_table.c.card_offered == card_offered,
                trade_offer_table.c.card_wanted == card_wanted)
        )

        trade_offer = await database.fetch_one(query)

        return TradeOffer.from_record(trade_offer) if trade_offer else None

    async def get_by_profile_id_and_card_offered_id(self, profile_id: int, card_offered_id: int) -> Any | None:
        """
        The method getting trade offer with a given profile id and card offered id.

        Args:
            profile_id (int): the id of profile.
            card_offered_id (int): the id of card offered.

        Returns:
            Any | None: The trade offer details.
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
        """
        The method adding new trade offer to the database.

        Args:
            data (TradeOfferIn): The details of the new trade offer.

        Returns:
            Any | None: The newly added trade offer.
        """

        query = trade_offer_table.insert().values(**data.model_dump())
        new_trade_offer_id = await database.execute(query)
        new_trade_offer = await self.get_by_id(new_trade_offer_id)

        return TradeOffer(**dict(new_trade_offer)) if new_trade_offer else None

    async def update_trade_offer(
            self,
            trade_offer_id: int,
            data: TradeOfferIn,
    ) -> Any | None:
        """
        The method updating trade offer data in the database.

        Args:
            trade_offer_id (int): The id of the trade offer.
            data (TradeOfferIn): The details of the updated trade offer.

        Returns:
            Any | None: The updated trade offer details.
        """

        if self.get_by_id(trade_offer_id):
            query = (
                trade_offer_table.update()
                .where(trade_offer_table.c.id == trade_offer_id)
                .values(**data.model_dump())
            )
            await database.execute(query)

            trade_offer = await self.get_by_id(trade_offer_id)

            return TradeOffer(**dict(trade_offer)) if trade_offer else None

        return None

    async def delete_trade_offer(self, trade_offer_id: int) -> bool:
        """
        The method removing trade offer from the database.

        Args:
            trade_offer_id (int): The id of the trade offer.

        Returns:
            bool: Success of the operation.
        """

        if await self.get_by_id(trade_offer_id):
            query = trade_offer_table \
                .delete() \
                .where(trade_offer_table.c.id == trade_offer_id)
            await database.execute(query)

            return True

        return False
