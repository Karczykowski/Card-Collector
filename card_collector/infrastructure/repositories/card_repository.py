"""Module containing card repository implementation."""

from typing import Any, Iterable

from asyncpg import Record  # type: ignore
from sqlalchemy import select, join

from card_collector.core.repositories.i_card_repository import ICardRepository
from card_collector.core.domains.card import Card, CardIn
from card_collector.db import (
    card_table,
    database,
)

class CardRepository(ICardRepository):
    """A class representing continent DB repository."""

    async def get_all_cards(self) -> Iterable[Any]:
        """The method getting all cards from the data storage.

        Returns:
            Iterable[Any]: Cards in the data storage.
        """

        query = (
            select(card_table)
            .order_by(card_table.c.name.asc())
        )
        cards = await database.fetch_all(query)

        return [Card.from_record(card) for card in cards]

    async def get_by_id(self, card_id: int) -> Any | None:
        """The method getting card by provided id.

        Args:
            card_id (int): The id of the card.

        Returns:
            Any | None: The card details.
        """

        card = await self._get_by_id(card_id)

        return Card.from_record(card) if card else None

    async def add_card(self, data: CardIn) -> Any | None:
        """The method adding new card to the data storage.

        Args:
            data (CardIn): The details of the new card.

        Returns:
            Card: Full details of the newly added card.

        Returns:
            Any | None: The newly added card.
        """

        query = card_table.insert().values(**data.model_dump())
        new_card_id = await database.execute(query)
        new_card = await self._get_by_id(new_card_id)

        return Card(**dict(new_card)) if new_card else None

    async def update_card(
            self,
            card_id: int,
            data: CardIn,
    ) -> Any | None:
        """The method updating card data in the data storage.

        Args:
            card_id (int): The id of the card.
            data (CardIn): The details of the updated card.

        Returns:
            Any | None: The updated card details.
        """

        if self._get_by_id(card_id):
            query = (
                card_table.update()
                .where(card_table.c.id == card_id)
                .values(**data.model_dump())
            )
            await database.execute(query)

            card = await self._get_by_id(card_id)

            return Card(**dict(card)) if card else None

        return None

    async def delete_card(self, card_id: int) -> bool:
        """The method updating removing card from the data storage.

        Args:
            card_id (int): The id of the card.

        Returns:
            bool: Success of the operation.
        """

        if self._get_by_id(card_id):
            query = card_table \
                .delete() \
                .where(card_table.c.id == card_id)
            await database.execute(query)

            return True

        return False

    async def _get_by_id(self, card_id: int) -> Record | None:
        """A private method getting card from the DB based on its ID.

        Args:
            card_id (int): The ID of the card.

        Returns:
            Any | None: Card record if exists.
        """

        query = (
            card_table.select()
            .where(card_table.c.id == card_id)
            .order_by(card_table.c.name.asc())
        )

        return await database.fetch_one(query)
