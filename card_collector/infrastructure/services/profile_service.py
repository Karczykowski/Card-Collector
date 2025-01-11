"""Module containing continent service implementation."""

from typing import List, List

from card_collector.core.domains.profile_collection import ProfileCollectionIn
from card_collector.core.domains.profile import Profile, ProfileIn
from card_collector.core.domains.card import Card
from card_collector.core.repositories.i_profile_repository import IProfileRepository
from card_collector.core.services.i_profile_service import IProfileService
from card_collector.core.services.i_card_service import ICardService
from card_collector.core.services.i_profile_collection_service import IProfileCollectionService

class ProfileService(IProfileService):
    """A class implementing the profile service."""

    _repository: IProfileRepository
    _card_service: ICardService
    _profile_collection_service: IProfileCollectionService

    def __init__(self, repository: IProfileRepository, card_service: ICardService, profile_collection_service: IProfileCollectionService) -> None:
        """The initializer of the `profile service`.

        Args:
            repository (IProfileRepository): The reference to the repository.
        """
        self._repository = repository
        self._card_service = card_service
        self._profile_collection_service = profile_collection_service

    async def get_all(self) -> List[Profile]:
        """The method getting all profiles from the repository.

        Returns:
            List[Profile]: All profiles.
        """

        return await self._repository.get_all_profiles()

    async def get_by_id(self, profile_id: int) -> Profile | None:
        """The method getting profile by provided id.

        Args:
            profile_id (int): The id of the profile.

        Returns:
            Profile | None: The profile details.
        """

        return await self._repository.get_by_id(profile_id)

    async def add_profile(self, data: ProfileIn) -> Profile | None:
        """The method adding new profile to the data storage.

        Args:
            data (ProfileIn): The details of the new profile.

        Returns:
            Profile | None: Full details of the newly added profile.
        """

        return await self._repository.add_profile(data)

    async def update_profile(
            self,
            profile_id: int,
            data: ProfileIn,
    ) -> Profile | None:
        """The method updating profile data in the data storage.

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
        """The method updating removing profile from the data storage.

        Args:
            profile_id (int): The id of the profile.

        Returns:
            bool: Success of the operation.
        """
        [await self._profile_collection_service.delete_profile_collection(profile_collection.id) for profile_collection in await self._profile_collection_service.get_all_by_profile_id(profile_id)]
        return await self._repository.delete_profile(profile_id)

    async def open_pack(self, profile_id: int) -> List[Card]:
        """The method for opening a pack of 5 cards and adding it to profile collection

        Args:
            profile_id (int): The id of the profile.

        Returns:
            bool: Success of the operation.
        """

        cards = await self._card_service.get_random_cards(5)

        for i in range(5):
            await self._profile_collection_service.add_card_to_profile_collection(ProfileCollectionIn(
                profile_id = profile_id,
                card_id = cards[i].id
            ))
        return cards