from abc import ABC, abstractmethod
from typing import Any, List

from card_collector.core.domains.quest import QuestIn

class IQuestRepository(ABC):

    @abstractmethod
    async def get_all_quests(self) -> List[Any]:
        """
        The abstract class getting all quests from the database.

        Returns:
            List[Any]: Quests in the database.
.
        """

    @abstractmethod
    async def get_all_by_profile(self, profile_id: int) -> List[Any]:
        """
        The abstract class getting all quests by a given profile id from the repository.

        Args:
            profile_id (int): The id of the profile.

        Returns:
            List[Any]: Quests in the database.
        """

    @abstractmethod
    async def get_all_by_reward(self, reward_id: int) -> List[Any]:
        """
        The abstract class getting all quests by a given reward id from the repository.

        Args:
            reward_id (int): The id of the reward.

        Returns:
            List[Any]: Quests in the database.
        """

    @abstractmethod
    async def get_by_id(self, quest_id: int) -> Any | None:
        """
        The abstract class getting quest by a given id.

        Args:
            quest_id (int): The id of the quest.

        Returns:
            Any | None: The quest details.
        """

    @abstractmethod
    async def add_quest(self, data: QuestIn) -> Any | None:
        """
        The abstract class adding new quest to the database.

        Args:
            data (QuestIn): The details of the new quest.

        Returns:
            Any | None: The newly added quest.
        """

    @abstractmethod
    async def update_quest(
            self,
            quest_id: int,
            data: QuestIn,
    ) -> Any | None:
        """
        The abstract class updating quest data in the database.

        Args:
            quest_id (int): The id of the quest.
            data (QuestIn): The details of the updated quest.

        Returns:
            Any | None: The updated quest details.
        """

    @abstractmethod
    async def delete_quest(self, quest_id: int) -> bool:
        """
        The abstract class removing quest from the database.

        Args:
            quest_id (int): The id of the quest.

        Returns:
            bool: Success of the operation.
        """
