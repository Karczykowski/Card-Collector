from abc import ABC, abstractmethod
from typing import List

from card_collector.core.domains.quest import Quest, QuestIn

class IQuestService(ABC):

    @abstractmethod
    async def get_all(self) -> List[Quest]:
        """
        The method getting all quests from the repository.

        Returns:
            List[Quest]: All quests.
        """

    @abstractmethod
    async def get_all_by_profile(self, profile_id: int) -> List[Quest]:
        """
        The method getting all quests with a given profile id from the repository.

        Args:
            profile_id (int): The id of the profile.

        Returns:
            List[Quest]: Quests.
        """

    @abstractmethod
    async def get_all_by_reward(self, reward_id: int) -> List[Quest]:
        """
        The method getting all quests with a given reward id from the repository.

        Args:
            reward_id (int): The of the reward.

        Returns:
            List[Quest]: Quests.
        """

    @abstractmethod
    async def get_by_id(self, quest_id: int) -> Quest | None:
        """
        The method getting quest by given id.

        Args:
            quest_id (int): The id of the quest.

        Returns:
            Quest | None: The quest details.
        """

    @abstractmethod
    async def add_quest(self, data: QuestIn) -> Quest | None:
        """
        The method adding new quest to the database.

        Args:
            data (QuestIn): The details of the new quest.

        Returns:
            Quest | None: Full details of the newly added quest.
        """

    @abstractmethod
    async def update_quest(
            self,
            quest_id: int,
            data: QuestIn,
    ) -> Quest | None:
        """
        The method updating quest data in the database.

        Args:
            quest_id (int): The id of the quest.
            data (QuestIn): The details of the updated quest.

        Returns:
            Quest | None: The updated quest details.
        """

    @abstractmethod
    async def delete_quest(self, quest_id: int) -> bool:
        """
        The method removing quest from the database.

        Args:
            quest_id (int): The id of the quest.

        Returns:
            bool: Success of the operation.
        """
