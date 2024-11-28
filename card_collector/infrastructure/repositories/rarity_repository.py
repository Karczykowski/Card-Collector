"""Module containing rarity repository implementation."""

from typing import Any, Iterable

from asyncpg import Record  # type: ignore
from sqlalchemy import select, join

from card_collector.core.repositories.i_rarity_repository import IRarityRepository
from card_collector.core.domains.rarity import Rarity, RarityIn
from card_collector.db import (
    rarity_table,
    database,
)

class RarityRepository(IRarityRepository):
    """A class representing continent DB repository."""

    async def get_all_rarities(self) -> Iterable[Any]:
        """The method getting all rarities from the data storage.

        Returns:
            Iterable[Any]: Rarities in the data storage.
        """

        query = (
            select(rarity_table)
            #.order_by(rarity_table.c.name.asc())
        )
        rarities = await database.fetch_all(query)

        return [Rarity.from_record(rarity) for rarity in rarities]

    async def get_by_id(self, rarity_id: int) -> Any | None:
        """The method getting rarity by provided id.

        Args:
            rarity_id (int): The id of the rarity.

        Returns:
            Any | None: The rarity details.
        """

        return await self._get_by_id(rarity_id)

    async def add_rarity(self, data: RarityIn) -> Any | None:
        """The method adding new rarity to the data storage.

        Args:
            data (RarityIn): The details of the new rarity.

        Returns:
            Rarity: Full details of the newly added rarity.

        Returns:
            Any | None: The newly added rarity.
        """

        query = rarity_table.insert().values(**data.model_dump())
        new_rarity_id = await database.execute(query)
        new_rarity = await self._get_by_id(new_rarity_id)

        return Rarity(**dict(new_rarity)) if new_rarity else None

    async def update_rarity(
            self,
            rarity_id: int,
            data: RarityIn,
    ) -> Any | None:
        """The method updating rarity data in the data storage.

        Args:
            rarity_id (int): The id of the rarity.
            data (RarityIn): The details of the updated rarity.

        Returns:
            Any | None: The updated rarity details.
        """

        if self._get_by_id(rarity_id):
            query = (
                rarity_table.update()
                .where(rarity_table.c.id == rarity_id)
                .values(**data.model_dump())
            )
            await database.execute(query)

            rarity = await self._get_by_id(rarity_id)

            return Rarity(**dict(rarity)) if rarity else None

        return None

    async def delete_rarity(self, rarity_id: int) -> bool:
        """The method updating removing rarity from the data storage.

        Args:
            rarity_id (int): The id of the rarity.

        Returns:
            bool: Success of the operation.
        """

        if self._get_by_id(rarity_id):
            query = rarity_table \
                .delete() \
                .where(rarity_table.c.id == rarity_id)
            await database.execute(query)

            return True

        return False

    async def _get_by_id(self, rarity_id: int) -> Record | None:
        """A private method getting rarity from the DB based on its ID.

        Args:
            rarity_id (int): The ID of the rarity.

        Returns:
            Any | None: Rarity record if exists.
        """

        query = (
            rarity_table.select()
            .where(rarity_table.c.id == rarity_id)
            .order_by(rarity_table.c.name.asc())
        )

        return await database.fetch_one(query)