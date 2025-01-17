from abc import ABC, abstractmethod
from typing import Any, List

from card_collector.core.domains.profile_collection import ProfileCollectionIn

class IProfileCollectionRepository(ABC):

    @abstractmethod
    async def get_all_profile_collections(self) -> List[Any]:
        """
        The abstract class getting all profile collections from the database.

        Returns:
            List[Any]: Profile Collections in the database.
        """

    @abstractmethod
    async def get_all_by_card_id(self, card_id: int) -> List[Any]:
        """
        The abstract class getting all profile collections with a given id from the database.

        Args:
            card_id (int): The id of the card.

        Returns:
            List[Any]: Profile Collections in the database.
        """

    @abstractmethod
    async def get_all_by_profile_id(self, profile_id: int) -> List[Any]:
        """
        The abstract class getting all profile collections with a given profile id from the database.

        Args:
            profile_id (int): The id of the profile.

        Returns:
            List[Any]: Profile Collections in the database.
        """

    @abstractmethod
    async def get_all_profile_collections_by_profile_id_and_card_id(self, card_id, profile_id: int) -> List[Any]:
        """
        The abstract class getting all profile collections with a given profile and card id from the database.

        Args:
            card_id (int): The id of the profile.
            profile_id (int): The id of the profile.

        Returns:
            List[Any]: Profile Collections in the database.
        """

    @abstractmethod
    async def get_by_id(self, profile_collection_id: int) -> Any | None:
        """
        The abstract class getting profile_collection by given id.

        Args:
            profile_collection_id (int): The id of the profile collection.

        Returns:
            Any | None: The profile collection details.
        """

    @abstractmethod
    async def add_profile_collection(self, data: ProfileCollectionIn) -> Any | None:
        """
        The abstract class adding new profile collection to the database.

        Args:
            data (ProfileCollectionIn): The details of the new profile collection.

        Returns:
            Any | None: The newly added profile collection.
        """

    @abstractmethod
    async def update_profile_collection(
            self,
            profile_collection_id: int,
            data: ProfileCollectionIn,
    ) -> Any | None:
        """
        The abstract class updating profile collection data in the database.

        Args:
            profile_collection_id (int): The id of the profile_collection.
            data (ProfileCollectionIn): The details of the updated profile collection.

        Returns:
            Any | None: The updated profile_collection details.
        """

    @abstractmethod
    async def delete_profile_collection(self, profile_collection_id: int) -> bool:
        """
        The abstract class updating removing profile_collection from the database.

        Args:
            profile_collection_id (int): The id of the profile collection.

        Returns:
            bool: Success of the operation.
        """
