"""Module containing continent service implementation."""
import random
from typing import List

from card_collector.core.domains.quest import Quest, QuestIn
from card_collector.core.repositories.i_quest_repository import IQuestRepository
from card_collector.core.services.i_quest_service import IQuestService
from card_collector.core.services.i_profile_collection_service import IProfileCollectionService


class QuestService(IQuestService):
    """A class implementing the quest service."""

    _repository: IQuestRepository
    _profile_collection_service: IProfileCollectionService

    def __init__(self, repository: IQuestRepository, profile_collection_service: IProfileCollectionService) -> None:
        """The initializer of the `quest service`.

        Args:
            repository (IQuestRepository): The reference to the repository.
        """
        self._repository = repository
        self._profile_collection_service = profile_collection_service

    async def get_all(self) -> List[Quest]:
        """The method getting all quests from the repository.

        Returns:
            List[Quest]: All quests.
        """

        return await self._repository.get_all_quests()

    async def get_all_by_rarity(self, rarity_id: int) -> List[Quest]:
        """The method getting all quests by id from the repository.

        Returns:
            List[Quest]: All quests.
        """

        return await self._repository.get_all_by_rarity(rarity_id)

    async def get_by_id(self, quest_id: int) -> Quest | None:
        """The method getting quest by provided id.

        Args:
            quest_id (int): The id of the quest.

        Returns:
            Quest | None: The quest details.
        """

        return await self._repository.get_by_id(quest_id)

    async def add_quest(self, data: QuestIn) -> Quest | None:
        """The method adding new quest to the data storage.

        Args:
            data (QuestIn): The details of the new quest.

        Returns:
            Quest | None: Full details of the newly added quest.
        """

        return await self._repository.add_quest(data)

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

        return await self._repository.update_quest(
            quest_id=quest_id,
            data=data,
        )

    async def delete_quest(self, quest_id: int) -> bool:
        """The method updating removing quest from the data storage.

        Args:
            quest_id (int): The id of the quest.

        Returns:
            bool: Success of the operation.
        """

        [await self._profile_collection_service.delete_profile_collection(profile_collection.id) for profile_collection in await self._profile_collection_service.get_all_by_quest_id(quest_id)]
        return await self._repository.delete_quest(quest_id)

    async def get_random_quests_by_rarity(self, amount: int, rarity_id: int) -> List[Quest]:
        """The method for generating a random quest of a given rarity.

        Args:
            amount: amount of quests to generate.
            rarity_id (int): The id of rarity to generate.

        Returns:
            Quest: generated quest.
        """
        quests = []

        for _ in range(amount):
            quests.append(random.choice(list(await self.get_all_by_rarity(rarity_id))))

        return quests

    async def get_random_quests(self, amount: int) -> List[Quest]:
        """The method for generating random quests

        Args:
            amount (int): The number of quests to generate.

        Returns:
            Quest: generated quest.
        """
        quests = []

        for _ in range(amount):
            quests.append(random.choice(list(await self._repository.get_all_quests())))

        return quests
