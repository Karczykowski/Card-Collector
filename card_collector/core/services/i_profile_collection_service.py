"""Module containing profile_collection service abstractions."""

from abc import ABC, abstractmethod
from typing import Iterable

from card_collector.core.domains.profile_collection import ProfileCollection, ProfileCollectionIn


class IProfileCollectionService(ABC):
    """A class representing profile_collection repository."""

    @abstractmethod
    async def get_all(self) -> Iterable[ProfileCollection]:
        """The method getting all profile_collections from the repository.

        Returns:
            Iterable[ProfileCollection]: All profile_collections.
        """


    @abstractmethod
    async def get_by_id(self, profile_collection_id: int) -> ProfileCollection | None:
        """The method getting profile_collection by provided id.

        Args:
            profile_collection_id (int): The id of the profile_collection.

        Returns:
            ProfileCollection | None: The profile_collection details.
        """


    @abstractmethod
    async def add_card_to_profile_collection(self, data: ProfileCollectionIn) -> ProfileCollection | None:
        """The method adding new profile_collection to the data storage.

        Args:
            data (ProfileCollectionIn): The details of the new profile_collection.

        Returns:
            ProfileCollection | None: Full details of the newly added profile_collection.
        """

    @abstractmethod
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

    @abstractmethod
    async def delete_profile_collection(self, profile_collection_id: int) -> bool:
        """The method updating removing profile_collection from the data storage.

        Args:
            profile_collection_id (int): The id of the profile_collection.

        Returns:
            bool: Success of the operation.
        """