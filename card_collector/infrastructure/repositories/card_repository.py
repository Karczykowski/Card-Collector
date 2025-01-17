from typing import Any, List

from sqlalchemy import select

from card_collector.core.repositories.i_card_repository import ICardRepository
from card_collector.core.domains.card import Card, CardIn
from card_collector.db import (
    card_table,
    database,
)

class CardRepository(ICardRepository):

    async def get_all_cards(self) -> List[Any]:
        """
        The method getting all cards from the database.

        Returns:
            List[Any]: Cards in the database.
        """

        query = (
            select(card_table)
            .order_by(card_table.c.name.asc())
        )
        cards = await database.fetch_all(query)

        return [Card.from_record(card) for card in cards]

    async def get_all_by_rarity(self, _rarity_id: int) -> List[Any]:
        """
        The method getting all cards with a given rarity from the database.

        Returns:
            List[Any]: Cards in the database.
        """

        query = (
            select(card_table)
            .where(card_table.c.rarity_id == _rarity_id) # type: ignore
            .order_by(card_table.c.name.asc())
        )
        cards = await database.fetch_all(query)

        return [Card.from_record(card) for card in cards]


    async def get_by_id(self, card_id: int) -> Any | None:
        """
        The method getting card with a given id.

        Args:
            card_id (int): The id of the card.

        Returns:
            Any | None: The card details.
        """
        query = (
            card_table.select()
            .where(card_table.c.id == card_id)
            .order_by(card_table.c.name.asc())
        )

        card = await database.fetch_one(query)

        return Card.from_record(card) if card else None

    async def add_card(self, data: CardIn) -> Any | None:
        """
        The method adding new card to the database.

        Args:
            data (CardIn): The details of the new card.

        Returns:
            Any | None: The newly added card.
        """

        query = card_table.insert().values(**data.model_dump())
        new_card_id = await database.execute(query)
        new_card = await self.get_by_id(new_card_id)

        return Card(**dict(new_card)) if new_card else None

    async def update_card(
            self,
            card_id: int,
            data: CardIn,
    ) -> Any | None:
        """
        The method updating card data in the database.

        Args:
            card_id (int): The id of the card.
            data (CardIn): The details of the updated card.

        Returns:
            Any | None: The updated card details.
        """

        if self.get_by_id(card_id):
            query = (
                card_table.update()
                .where(card_table.c.id == card_id)
                .values(**data.model_dump())
            )
            await database.execute(query)

            card = await self.get_by_id(card_id)

            return Card(**dict(card)) if card else None

        return None

    async def delete_card(self, card_id: int) -> bool:
        """
        The method removing card from the database.

        Args:
            card_id (int): The id of the card.

        Returns:
            bool: Success of the operation.
        """

        if await self.get_by_id(card_id):
            query = card_table \
                .delete() \
                .where(card_table.c.id == card_id)
            await database.execute(query)

            return True

        return False
