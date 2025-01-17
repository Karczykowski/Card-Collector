from abc import ABC, abstractmethod
from typing import List

from card_collector.core.domains.profile_collection import ProfileCollection, ProfileCollectionIn

class IProfileCollectionService(ABC):

    @abstractmethod
    async def get_all(self) -> List[ProfileCollection]:
        """
        The method getting all profile collections from the repository.

        Returns:
            List[ProfileCollection]: All profile collections.
        """

    @abstractmethod
    async def get_all_by_card_id(self, card_id: int) -> List[ProfileCollection]:
        """
        The method getting all profile collections with a given card id from the repository.

        Args:
            card_id (int): The id of card.

        Returns:
            List[ProfileCollection]: Profile collections.
        """

    async def get_all_by_profile_id(self, profile_id: int) -> List[ProfileCollection]:
        """
        The method getting all profile collections with a given profile id from the repository.

        Args:
            profile_id (int): The id of profile.

        Returns:
            List[ProfileCollection]: Profile collections.
        """

    @abstractmethod
    async def get_all_profile_collections_by_profile_id(self, profile_id: int) -> List[ProfileCollection]:
        """
        The method getting all profile collections with a given profile id from the repository.

        Args:
            profile_id (int): The id of the profile.

        Returns:
            List[ProfileCollection]: Profile collections.
        """

    @abstractmethod
    async def  get_all_profile_collections_by_profile_id_and_card_id(
            self,
            profile_id: int,
            card_id: int
    ) -> List[ProfileCollection]:
        """
        The method getting all profile collections with a given profile and card id from the repository.

        Args:
            profile_id (int): The id of the profile.
            card_id (int): The id of the card.

        Returns:
            List[ProfileCollection]: Profile collections.
        """

    @abstractmethod
    async def get_by_id(self, profile_collection_id: int) -> ProfileCollection | None:
        """
        The method getting profile collection with a given id from the repository.

        Args:
            profile_collection_id (int): The id of the profile collection.

        Returns:
            ProfileCollection | None: The profile collection details.
        """

    @abstractmethod
    async def add_profile_collection(self, data: ProfileCollectionIn) -> ProfileCollection | None:
        """
        The method adding new profile collection to the database.

        Args:
            data (ProfileCollectionIn): The details of the new profile collection.

        Returns:
            ProfileCollection | None: Full details of the newly added profile collection.
        """

    @abstractmethod
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

    @abstractmethod
    async def delete_profile_collection(self, profile_collection_id: int) -> bool:
        """
        The method removing profile_collection from the database.

        Args:
            profile_collection_id (int): The id of the profile collection.

        Returns:
            bool: Success of the operation.
        """
