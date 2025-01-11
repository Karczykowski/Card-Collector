"""Module containing continent service implementation."""

from typing import List

from card_collector.core.domains.profile_collection import ProfileCollection, ProfileCollectionIn
from card_collector.core.repositories.i_profile_collection_repository import IProfileCollectionRepository
from card_collector.core.services.i_profile_collection_service import IProfileCollectionService
from card_collector.core.services.i_trade_offer_service import ITradeOfferService


class ProfileCollectionService(IProfileCollectionService):
    """A class implementing the profile_collection service."""

    _repository: IProfileCollectionRepository
    _trade_offer_service: ITradeOfferService

    def __init__(self, repository: IProfileCollectionRepository, trade_offer_service: ITradeOfferService) -> None:
        """The initializer of the `profile_collection service`.

        Args:
            repository (IProfileCollectionRepository): The reference to the repository.
        """
        self._repository = repository
        self._trade_offer_service = trade_offer_service

    async def get_all(self) -> List[ProfileCollection]:
        """The method getting all profile_collections from the repository.

        Returns:
            List[ProfileCollection]: All profile_collections.
        """

        return await self._repository.get_all_profile_collections()

    async def get_all_by_card_id(self, card_id: int) -> List[ProfileCollection]:
        """The method getting all profile_collections from the repository.

        Args:
            card_id (int): The id of card.
        Returns:
            List[ProfileCollection]: All profile_collections.
        """

        return await self._repository.get_all_by_card_id(card_id)

    async def get_all_by_profile_id(self, profile_id: int) -> List[ProfileCollection]:
        """The method getting all profile_collections from the repository.

        Args:
            profile_id (int): The id of card.
        Returns:
            List[ProfileCollection]: All profile_collections.
        """

        return await self._repository.get_all_by_profile_id(profile_id)

    async def get_by_id(self, profile_collection_id: int) -> ProfileCollection | None:
        """The method getting profile_collection by provided id.

        Args:
            profile_collection_id (int): The id of the profile_collection.

        Returns:
            ProfileCollection | None: The profile_collection details.
        """

        return await self._repository.get_by_id(profile_collection_id)

    async def get_profile_collection_by_profile_id(self, profile_collection_id: int) -> List[ProfileCollection] | None:
        """The method getting profile_collection by provided id.

        Args:
            profile_collection_id (int): The id of the profile_collection.

        Returns:
            ProfileCollection | None: The profile_collection details.
        """

        return await self._repository.get_profile_collection_by_profile_id(profile_collection_id)

    async def get_profile_collection_by_profile_id_and_card_id(self, profile_collection_id: int, card_id: int) -> List[ProfileCollection] | None:
        """The method getting profile_collection by provided id.

        Args:
            card_id (int): The id of card.
            profile_collection_id (int): The id of the profile_collection.

        Returns:
            ProfileCollection | None: The profile_collection details.
        """

        return await self._repository.get_profile_collection_by_profile_id_and_card_id(card_id, profile_collection_id)

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
            In case of removing last copy, it also removes any connected trade offers.

        Args:
            profile_collection_id (int): The id of the profile_collection.

        Returns:
            bool: Success of the operation.
        """
        profile_collection = await self.get_by_id(profile_collection_id)
        removed_profile_collection_card_id = profile_collection.card_id
        removed_profile_collection_profile_id = profile_collection.profile_id

        removed_profile_collection = await self._repository.delete_profile_collection(profile_collection_id)

        if not await self.get_profile_collection_by_profile_id_and_card_id(removed_profile_collection_profile_id, removed_profile_collection_card_id):
            await self._trade_offer_service.delete_trade_offer_by_profile_id_and_card_offered_id(removed_profile_collection_profile_id, removed_profile_collection_card_id)

        return removed_profile_collection
