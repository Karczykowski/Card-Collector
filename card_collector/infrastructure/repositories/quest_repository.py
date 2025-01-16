"""Module containing quest repository implementation."""

from typing import Any, List

from asyncpg import Record  # type: ignore
from sqlalchemy import select, join

from card_collector.core.repositories.i_quest_repository import IQuestRepository
from card_collector.core.domains.quest import Quest, QuestIn
from card_collector.db import (
    quest_table,
    database,
)

class QuestRepository(IQuestRepository):
    """A class representing continent DB repository."""

    async def get_all_quests(self) -> List[Any]:
        """The method getting all quests from the data storage.

        Returns:
            List[Any]: Quests in the data storage.
        """

        query = (
            select(quest_table)
            .order_by(quest_table.c.name.asc())
        )
        quests = await database.fetch_all(query)

        return [Quest.from_record(quest) for quest in quests]

    async def get_by_id(self, quest_id: int) -> Any | None:
        """The method getting quest by provided id.

        Args:
            quest_id (int): The id of the quest.

        Returns:
            Any | None: The quest details.
        """

        quest = await self._get_by_id(quest_id)

        return Quest.from_record(quest) if quest else None

    async def add_quest(self, data: QuestIn) -> Any | None:
        """The method adding new quest to the data storage.

        Args:
            data (QuestIn): The details of the new quest.

        Returns:
            Quest: Full details of the newly added quest.

        Returns:
            Any | None: The newly added quest.
        """

        query = quest_table.insert().values(**data.model_dump())
        new_quest_id = await database.execute(query)
        new_quest = await self._get_by_id(new_quest_id)

        return Quest(**dict(new_quest)) if new_quest else None

    async def update_quest(
            self,
            quest_id: int,
            data: QuestIn,
    ) -> Any | None:
        """The method updating quest data in the data storage.

        Args:
            quest_id (int): The id of the quest.
            data (QuestIn): The details of the updated quest.

        Returns:
            Any | None: The updated quest details.
        """

        if self._get_by_id(quest_id):
            query = (
                quest_table.update()
                .where(quest_table.c.id == quest_id)
                .values(**data.model_dump())
            )
            await database.execute(query)

            quest = await self._get_by_id(quest_id)

            return Quest(**dict(quest)) if quest else None

        return None

    async def delete_quest(self, quest_id: int) -> bool:
        """The method updating removing quest from the data storage.

        Args:
            quest_id (int): The id of the quest.

        Returns:
            bool: Success of the operation.
        """

        if await self._get_by_id(quest_id):
            query = quest_table \
                .delete() \
                .where(quest_table.c.id == quest_id)
            await database.execute(query)

            return True

        return False

    async def _get_by_id(self, quest_id: int) -> Record | None:
        """A private method getting quest from the DB based on its ID.

        Args:
            quest_id (int): The ID of the quest.

        Returns:
            Any | None: Quest record if exists.
        """

        query = (
            quest_table.select()
            .where(quest_table.c.id == quest_id)
            .order_by(quest_table.c.name.asc())
        )

        return await database.fetch_one(query)
