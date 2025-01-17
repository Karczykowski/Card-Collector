from typing import Any, List

from sqlalchemy import select

from card_collector.core.repositories.i_quest_repository import IQuestRepository
from card_collector.core.domains.quest import Quest, QuestIn
from card_collector.db import (
    quest_table,
    database,
)

class QuestRepository(IQuestRepository):

    async def get_all_quests(self) -> List[Any]:
        """
        The method getting all quests from the database.

        Returns:
            List[Any]: All quests in the database.
        """

        query = (
            select(quest_table)
        )
        quests = await database.fetch_all(query)

        return [Quest.from_record(quest) for quest in quests]

    async def get_all_by_profile(self, profile_id: int) -> List[Any]:
        """
        The method getting all quests with a given profile id from the database.

        Args:
            profile_id (int): The id of the profile.

        Returns:
            List[Quest]: Quests.
        """

        query = (
            select(quest_table)
            .where(quest_table.c.profile_id == profile_id) # type: ignore
        )
        quests = await database.fetch_all(query)

        return [Quest.from_record(quest) for quest in quests]

    async def get_all_by_reward(self, reward_id: int) -> List[Any]:
        """
        The method getting all quests with a given reward id from the database.

        Args:
            reward_id (int): The id of the reward.

        Returns:
            List[Quest]: Quests.
        """

        query = (
            select(quest_table)
            .where(quest_table.c.reward == reward_id) # type: ignore
        )
        quests = await database.fetch_all(query)

        return [Quest.from_record(quest) for quest in quests]

    async def get_by_id(self, quest_id: int) -> Any | None:
        """
        The method getting quest with a given id.

        Args:
            quest_id (int): The id of the quest.

        Returns:
            Any | None: The quest details.
        """

        query = (
            quest_table.select()
            .where(quest_table.c.id == quest_id)
        )

        quest = await database.fetch_one(query)

        return Quest.from_record(quest) if quest else None

    async def add_quest(self, data: QuestIn) -> Any | None:
        """
        The method adding new quest to the database.

        Args:
            data (QuestIn): The details of the new quest.

        Returns:
            Any | None: The newly added quest.
        """

        query = quest_table.insert().values(**data.model_dump())
        new_quest_id = await database.execute(query)
        new_quest = await self.get_by_id(new_quest_id)

        return Quest(**dict(new_quest)) if new_quest else None

    async def update_quest(
            self,
            quest_id: int,
            data: QuestIn,
    ) -> Any | None:
        """
        The method updating quest data in the database.

        Args:
            quest_id (int): The id of the quest.
            data (QuestIn): The details of the updated quest.

        Returns:
            Any | None: The updated quest details.
        """

        if self.get_by_id(quest_id):
            query = (
                quest_table.update()
                .where(quest_table.c.id == quest_id)
                .values(**data.model_dump())
            )
            await database.execute(query)

            quest = await self.get_by_id(quest_id)

            return Quest(**dict(quest)) if quest else None

        return None

    async def delete_quest(self, quest_id: int) -> bool:
        """
        The method removing quest from the database.

        Args:
            quest_id (int): The id of the quest.

        Returns:
            bool: Success of the operation.
        """

        if await self.get_by_id(quest_id):
            query = quest_table \
                .delete() \
                .where(quest_table.c.id == quest_id)
            await database.execute(query)

            return True

        return False
