"""Module containing quest repository abstractions."""

from abc import ABC, abstractmethod
from typing import Any, List

from card_collector.core.domains.quest import QuestIn


class IQuestRepository(ABC):
    """An abstract class representing protocol of continent repository."""

    @abstractmethod
    async def get_all_quests(self) -> List[Any]:
        """The abstract getting all quests from the data storage.

        Returns:
            List[Any]: Quests in the data storage.
        """

    @abstractmethod
    async def get_by_id(self, quest_id: int) -> Any | None:
        """The abstract getting quest by provided id.

        Args:
            quest_id (int): The id of the quest.

        Returns:
            Any | None: The quest details.
        """

    @abstractmethod
    async def add_quest(self, data: QuestIn) -> Any | None:
        """The abstract adding new quest to the data storage.

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
        """The abstract updating quest data in the data storage.

        Args:
            quest_id (int): The id of the quest.
            data (QuestIn): The details of the updated quest.

        Returns:
            Any | None: The updated quest details.
        """

    @abstractmethod
    async def delete_quest(self, quest_id: int) -> bool:
        """The abstract updating removing quest from the data storage.

        Args:
            quest_id (int): The id of the quest.

        Returns:
            bool: Success of the operation.
        """
        