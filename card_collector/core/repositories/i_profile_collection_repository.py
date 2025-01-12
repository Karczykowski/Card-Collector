"""Module containing profile_collection repository abstractions."""

from abc import ABC, abstractmethod
from typing import Any, List

from card_collector.core.domains.profile_collection import ProfileCollectionIn


class IProfileCollectionRepository(ABC):
    """An abstract class representing protocol of continent repository."""

    @abstractmethod
    async def get_all_profile_collections(self) -> List[Any]:
        """The abstract getting all profile_collections from the data storage.

        Returns:
            List[Any]: ProfileCollections in the data storage.
        """

    @abstractmethod
    async def get_all_by_card_id(self, card_id: int) -> List[Any]:
        """The abstract getting all profile_collections from the data storage.

        Returns:
            List[Any]: ProfileCollections in the data storage.
        """

    @abstractmethod
    async def get_all_by_profile_id(self, profile_id: int) -> List[Any]:
        """The abstract getting all profile_collections from the data storage.

        Returns:
            List[Any]: ProfileCollections in the data storage.
        """

    @abstractmethod
    async def get_profile_collection_by_profile_id(self, profile_id: int) -> List[Any]:
        """The abstract getting all profile_collections from the data storage.

        Returns:
            List[Any]: ProfileCollections in the data storage.
        """

    @abstractmethod
    async def get_profile_collection_by_profile_id_and_card_id(self, card_id, profile_id: int) -> List[Any]:
        """The abstract getting all profile_collections from the data storage.

        Returns:
            List[Any]: ProfileCollections in the data storage.
        """

    @abstractmethod
    async def get_by_id(self, profile_collection_id: int) -> Any | None:
        """The abstract getting profile_collection by provided id.

        Args:
            profile_collection_id (int): The id of the profile_collection.

        Returns:
            Any | None: The profile_collection details.
        """

    @abstractmethod
    async def get_by_trade_offer(self, trade_offer_id: int) -> Any | None:
        """The abstract getting profile_collection by provided id.

        Args:
            trade_offer_id (int): The id of the trade offer.

        Returns:
            Any | None: The profile_collection details.
        """

    @abstractmethod
    async def add_card_to_profile_collection(self, data: ProfileCollectionIn) -> Any | None:
        """The abstract adding new profile_collection to the data storage.

        Args:
            data (ProfileCollectionIn): The details of the new profile_collection.

        Returns:
            Any | None: The newly added profile_collection.
        """

    @abstractmethod
    async def update_profile_collection(
            self,
            profile_collection_id: int,
            data: ProfileCollectionIn,
    ) -> Any | None:
        """The abstract updating profile_collection data in the data storage.

        Args:
            profile_collection_id (int): The id of the profile_collection.
            data (ProfileCollectionIn): The details of the updated profile_collection.

        Returns:
            Any | None: The updated profile_collection details.
        """

    @abstractmethod
    async def delete_profile_collection(self, profile_collection_id: int) -> bool:
        """The abstract updating removing profile_collection from the data storage.

        Args:
            profile_collection_id (int): The id of the profile_collection.

        Returns:
            bool: Success of the operation.
        """