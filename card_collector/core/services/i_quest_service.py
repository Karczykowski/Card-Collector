"""Module containing quest service abstractions."""

from abc import ABC, abstractmethod
from typing import List

from card_collector.core.domains.quest import Quest, QuestIn


class IQuestService(ABC):
    """A class representing quest repository."""

    @abstractmethod
    async def get_all(self) -> List[Quest]:
        """The method getting all quests from the repository.

        Returns:
            List[Quest]: All quests.
        """

    @abstractmethod
    async def get_all_by_profile(self, profile_id: int) -> List[Quest]:
        """The method getting all quests from the repository.

        Returns:
            List[Quest]: All quests.
        """

    @abstractmethod
    async def get_all_by_reward(self, reward_id: int) -> List[Quest]:
        """The method getting all quests from the repository.

        Returns:
            List[Quest]: All quests.
        """

    @abstractmethod
    async def get_by_id(self, quest_id: int) -> Quest | None:
        """The method getting quest by provided id.

        Args:
            quest_id (int): The id of the quest.

        Returns:
            Quest | None: The quest details.
        """

    @abstractmethod
    async def add_quest(self, data: QuestIn) -> Quest | None:
        """The method adding new quest to the data storage.

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
        """The method updating quest data in the data storage.

        Args:
            quest_id (int): The id of the quest.
            data (QuestIn): The details of the updated quest.

        Returns:
            Quest | None: The updated quest details.
        """

    @abstractmethod
    async def complete_quest(self, quest_id: int) -> bool:
        """The method for completing quest

        Args:
            quest_id (int): The id of the quest.

        Returns:
            bool: Success of the operation.
        """

    @abstractmethod
    async def delete_quest(self, quest_id: int) -> bool:
        """The method updating removing quest from the data storage.

        Args:
            quest_id (int): The id of the quest.

        Returns:
            bool: Success of the operation.
        """
