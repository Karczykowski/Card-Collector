from typing import List

from card_collector.core.domains.profile_collection import ProfileCollection, ProfileCollectionIn
from card_collector.core.domains.quest import QuestIn
from card_collector.core.repositories.i_profile_collection_repository import IProfileCollectionRepository
from card_collector.core.services.i_profile_collection_service import IProfileCollectionService
from card_collector.core.services.i_trade_offer_service import ITradeOfferService
from card_collector.core.services.i_quest_service import IQuestService

class ProfileCollectionService(IProfileCollectionService):

    _repository: IProfileCollectionRepository
    _trade_offer_service: ITradeOfferService
    _quest_service: IQuestService

    def __init__(
            self,
            repository: IProfileCollectionRepository,
            trade_offer_service: ITradeOfferService,
            quest_service: IQuestService
    ) -> None:
        """
        The initializer of the profile_collection service.

        Args:
            repository (IProfileCollectionRepository): The reference to the repository.
            trade_offer_service (ITradeOfferService): The reference to the trade offer service.
            quest_service (IQuestService): The reference to the quest service.
        """
        self._repository = repository
        self._trade_offer_service = trade_offer_service
        self._quest_service = quest_service

    async def get_all(self) -> List[ProfileCollection]:
        """
        The method getting all profile collections from the repository.

        Returns:
            List[ProfileCollection]: All profile collections.
        """

        return await self._repository.get_all_profile_collections()

    async def get_all_by_card_id(self, card_id: int) -> List[ProfileCollection]:
        """
        The method getting all profile collections with a given card id from the repository.

        Args:
            card_id (int): The id of card.
        Returns:
            List[ProfileCollection]: Profile_collections.
        """

        return await self._repository.get_all_by_card_id(card_id)

    async def get_all_by_profile_id(self, profile_id: int) -> List[ProfileCollection]:
        """
        The method getting all profile collections with a given profile id from the repository.

        Args:
            profile_id (int): The id of card.
        Returns:
            List[ProfileCollection]: Profile collections.
        """

        return await self._repository.get_all_by_profile_id(profile_id)

    async def get_all_profile_collections_by_profile_id(self, profile_collection_id: int) -> List[ProfileCollection] | None:
        """
        The method getting profile collection with a given id from the repository.

        Args:
            profile_collection_id (int): The id of the profile collection.

        Returns:
            ProfileCollection | None: The profile collection details.
        """

        return await self._repository.get_all_by_profile_id(profile_collection_id)

    async def get_all_profile_collections_by_profile_id_and_card_id(
            self,
            profile_collection_id: int,
            card_id: int
    ) -> List[ProfileCollection] | None:
        """
        The method getting profile collection with a given profile collection id and card if from the repository.

        Args:
            profile_collection_id (int): The id of the profile_collection.
            card_id (int): The id of card.

        Returns:
            List[ProfileCollection] | None: Profile collections.
        """

        return await self._repository.get_all_profile_collections_by_profile_id_and_card_id(card_id, profile_collection_id)

    async def get_by_id(self, profile_collection_id: int) -> ProfileCollection | None:
        """
        The method getting profile collection with a given id from the repository.

        Args:
            profile_collection_id (int): The id of the profile collection.

        Returns:
            ProfileCollection | None: The profile collection details.
        """

        return await self._repository.get_by_id(profile_collection_id)

    async def add_profile_collection(self, data: ProfileCollectionIn) -> ProfileCollection | None:
        """
        The method adding new profile collection to the database.

        Args:
            data (ProfileCollectionIn): The details of the new profile collection.

        Returns:
            ProfileCollection | None: Details of the newly added profile collection.
        """

        associated_quests = await self._quest_service.get_all_by_profile(data.profile_id)

        for quest in associated_quests:
            await self._quest_service.update_quest(quest.id, QuestIn(
                profile_id=quest.profile_id,
                cards_collected=quest.cards_collected+1,
                cards_needed=quest.cards_needed,
                reward=quest.reward
            ))

            if quest.cards_collected+1 == quest.cards_needed:
                reward_id = quest.reward
                await self._quest_service.delete_quest(quest.id)
                await self.add_profile_collection(ProfileCollectionIn(
                    profile_id=data.profile_id,
                    card_id=reward_id
                ))


        return await self._repository.add_profile_collection(data)

    async def update_profile_collection(
            self,
            profile_collection_id: int,
            data: ProfileCollectionIn,
    ) -> ProfileCollection | None:
        """
        The method updating profile collection data in the database.

        Args:
            profile_collection_id (int): The id of the profile collection.
            data (ProfileCollectionIn): The details of the updated profile collection.

        Returns:
            ProfileCollection | None: The updated profile collection details.
        """

        return await self._repository.update_profile_collection(
            profile_collection_id=profile_collection_id,
            data=data,
        )

    async def delete_profile_collection(self, profile_collection_id: int) -> bool:
        """
        The method removing profile collection from the database.
            In case of removing last copy, it also removes any connected trade offers.

        Args:
            profile_collection_id (int): The id of the profile collection.

        Returns:
            bool: Success of the operation.
        """
        profile_collection = await self.get_by_id(profile_collection_id)
        removed_profile_collection_card_id = profile_collection.card_id
        removed_profile_collection_profile_id = profile_collection.profile_id

        removed_profile_collection = await self._repository.delete_profile_collection(profile_collection_id)

        if not await self.get_all_profile_collections_by_profile_id_and_card_id(
                removed_profile_collection_profile_id,
                removed_profile_collection_card_id):
            await self._trade_offer_service.delete_trade_offer_by_profile_id_and_card_offered_id(
                removed_profile_collection_profile_id,
                removed_profile_collection_card_id)

        return removed_profile_collection
