"""Module containing continent service implementation."""

from typing import Iterable

from card_collector.core.domains.profile_collection import ProfileCollection, ProfileCollectionIn
from card_collector.core.repositories.i_profile_collection_repository import IProfileCollectionRepository
from card_collector.core.services.i_profile_collection_service import IProfileCollectionService


class ProfileCollectionService(IProfileCollectionService):
    """A class implementing the profile_collection service."""

    _repository: IProfileCollectionRepository

    def __init__(self, repository: IProfileCollectionRepository) -> None:
        """The initializer of the `profile_collection service`.

        Args:
            repository (IProfileCollectionRepository): The reference to the repository.
        """
        self._repository = repository

    async def get_all(self) -> Iterable[ProfileCollection]:
        """The method getting all profile_collections from the repository.

        Returns:
            Iterable[ProfileCollection]: All profile_collections.
        """

        return await self._repository.get_all_profile_collections()

    async def get_by_id(self, profile_collection_id: int) -> ProfileCollection | None:
        """The method getting profile_collection by provided id.

        Args:
            profile_collection_id (int): The id of the profile_collection.

        Returns:
            ProfileCollection | None: The profile_collection details.
        """

        return await self._repository.get_by_id(profile_collection_id)

    async def get_profile_collection_by_profile_id(self, profile_collection_id: int) -> Iterable[ProfileCollection] | None:
        """The method getting profile_collection by provided id.

        Args:
            profile_collection_id (int): The id of the profile_collection.

        Returns:
            ProfileCollection | None: The profile_collection details.
        """

        return await self._repository.get_profile_collection_by_profile_id(profile_collection_id)

    async def add_card_to_profile_collection(self, data: ProfileCollectionIn) -> ProfileCollection | None:
        """The method adding new profile_collection to the data storage.

        Args:
            data (ProfileCollectionIn): The details of the new profile_collection.

        Returns:
            ProfileCollection | None: Full details of the newly added profile_collection.
        """

        return await self._repository.add_card_to_profile_collection(data)

    async def update_profile_collection(
            self,
            profile_collection_id: int,
            data: ProfileCollectionIn,
    ) -> ProfileCollection | None:
        """The method updating profile_collection data in the data storage.

        Args:
            profile_collection_id (int): The id of the profile_collection.
            data (ProfileCollectionIn): The details of the updated profile_collection.

        Returns:
            ProfileCollection | None: The updated profile_collection details.
        """

        return await self._repository.update_profile_collection(
            profile_collection_id=profile_collection_id,
            data=data,
        )

    async def delete_profile_collection(self, profile_collection_id: int) -> bool:
        """The method updating removing profile_collection from the data storage.

        Args:
            profile_collection_id (int): The id of the profile_collection.

        Returns:
            bool: Success of the operation.
        """

        return await self._repository.delete_profile_collection(profile_collection_id)
