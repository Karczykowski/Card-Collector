from typing import List

from card_collector.core.domains.profile_collection import ProfileCollectionIn
from card_collector.core.domains.profile import Profile, ProfileIn
from card_collector.core.domains.card import Card
from card_collector.core.repositories.i_profile_repository import IProfileRepository
from card_collector.core.services.i_profile_service import IProfileService
from card_collector.core.services.i_card_service import ICardService
from card_collector.core.services.i_profile_collection_service import IProfileCollectionService
from card_collector.core.services.i_quest_service import IQuestService

class ProfileService(IProfileService):

    _repository: IProfileRepository
    _card_service: ICardService
    _profile_collection_service: IProfileCollectionService
    _quest_service: IQuestService

    def __init__(
            self,
            repository: IProfileRepository,
            card_service: ICardService,
            profile_collection_service: IProfileCollectionService,
            quest_service: IQuestService
    ) -> None:
        """
        The initializer of the profile service.

        Args:
            repository (IProfileRepository): The reference to the repository.
            card_service (ICardService): The reference to the card service.
            profile_collection_service (IProfileCollectionService): The reference to the profile collection service.
            quest_service (IQuestService): The reference to the profile collection service.
        """
        self._repository = repository
        self._card_service = card_service
        self._profile_collection_service = profile_collection_service
        self._quest_service = quest_service

    async def get_all(self) -> List[Profile]:
        """
        The method getting all profiles from the repository.

        Returns:
            List[Profile]: All profiles.
        """

        return await self._repository.get_all_profiles()

    async def get_by_id(self, profile_id: int) -> Profile | None:
        """
        The method getting profile with a given id from the repository.

        Args:
            profile_id (int): The id of the profile.

        Returns:
            Profile | None: The profile details.
        """

        return await self._repository.get_by_id(profile_id)

    async def open_pack(self, profile_id: int, amount_of_cards: int) -> List[Card]:
        """
        The method for opening a pack of 5 cards and adding it to profile collection.

        Args:
            profile_id (int): The id of the profile.
            amount_of_cards (int): Amount of cards in a pack.

        Returns:
            List[Card]: List of cards opened from the pack.
        """

        cards = await self._card_service.get_random_cards(amount_of_cards)

        for i in range(amount_of_cards):
            await self._profile_collection_service.add_profile_collection(ProfileCollectionIn(
                profile_id = profile_id,
                card_id = cards[i].id
            ))
        return cards

    async def add_profile(self, data: ProfileIn) -> Profile | None:
        """
        The method adding new profile to the database.

        Args:
            data (ProfileIn): The details of the new profile.

        Returns:
            Profile | None: Details of the newly added profile.
        """

        return await self._repository.add_profile(data)

    async def update_profile(
            self,
            profile_id: int,
            data: ProfileIn,
    ) -> Profile | None:
        """
        The method updating profile data in the database.

        Args:
            profile_id (int): The id of the profile.
            data (ProfileIn): The details of the updated profile.

        Returns:
            Profile | None: The updated profile details.
        """

        return await self._repository.update_profile(
            profile_id=profile_id,
            data=data,
        )

    async def delete_profile(self, profile_id: int) -> bool:
        """
        The method removing profile from the database.

        Args:
            profile_id (int): The id of the profile.

        Returns:
            bool: Success of the operation.
        """
        [await self._profile_collection_service.delete_profile_collection(profile_collection.id)
         for profile_collection in await self._profile_collection_service.get_all_by_profile_id(profile_id)]
        [await self._quest_service.delete_quest(quest.id)
         for quest in await self._quest_service.get_all_by_profile(profile_id)]
        return await self._repository.delete_profile(profile_id)
