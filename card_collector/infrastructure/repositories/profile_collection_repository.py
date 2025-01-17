from typing import Any, List

from sqlalchemy import select, and_

from card_collector.core.repositories.i_profile_collection_repository import IProfileCollectionRepository
from card_collector.core.domains.profile_collection import ProfileCollection, ProfileCollectionIn
from card_collector.db import (
    profile_collection_table,
    database,
)

class ProfileCollectionRepository(IProfileCollectionRepository):

    async def get_all_profile_collections(self) -> List[Any]:
        """
        The method getting all profile collections from the database.

        Returns:
            List[Any]: Profile Collections in the database.
        """

        query = (
            select(profile_collection_table)
        )
        profile_collections = await database.fetch_all(query)

        return [ProfileCollection.from_record(profile_collection) for profile_collection in profile_collections]

    async def get_all_by_card_id(self, card_id: int) -> List[Any]:
        """
        The method getting all profile collections with a given card id from the database.

        Args:
            card_id (int): The id of the card.

        Returns:
            List[Any]: Profile Collections in the database.
        """

        query = (
            select(profile_collection_table)
            .where(profile_collection_table.c.card_id == card_id) # type: ignore
        )
        profile_collections = await database.fetch_all(query)

        return [ProfileCollection.from_record(profile_collection) for profile_collection in profile_collections]

    async def get_all_by_profile_id(self, profile_id: int) -> List[Any]:
        """
        The method getting all profile collections with a given profile id from the database.

        Args:
            profile_id (int): The id of the profile.

        Returns:
            List[Any]: Profile Collections in the database.
        """

        query = (
            select(profile_collection_table)
            .where(profile_collection_table.c.profile_id == profile_id) # type: ignore
        )
        profile_collections = await database.fetch_all(query)

        return [ProfileCollection.from_record(profile_collection) for profile_collection in profile_collections]

    async def get_all_profile_collections_by_profile_id_and_card_id(self, card_id: int, profile_id: int) -> List[Any]:
        """
        The method getting all profile collections with a given profile id and card id from the database.

        Args:
            card_id (int): The id of the card.
            profile_id (int): The id of the profile.

        Returns:
            List[Any]: ProfileCollections in the database.
        """

        query = (
            select(profile_collection_table)
            .where(
                and_(
                    profile_collection_table.c.profile_id == profile_id,
                    profile_collection_table.c.card_id == card_id)
            )
        )
        profile_collections = await database.fetch_all(query)

        return [ProfileCollection.from_record(profile_collection) for profile_collection in profile_collections]

    async def get_by_id(self, profile_collection_id: int) -> Any | None:
        """
        The method getting profile collection with a given id from the database.

        Args:
            profile_collection_id (int): The id of the profile collection.

        Returns:
            Any | None: The profile_collection details.
        """

        query = (
            profile_collection_table.select()
            .where(profile_collection_table.c.id == profile_collection_id)
        )

        profile_collection = await database.fetch_one(query)

        return ProfileCollection.from_record(profile_collection) if profile_collection else None

    async def add_profile_collection(self, data: ProfileCollectionIn) -> Any | None:
        """
        The method adding new profile collection to the database.

        Args:
            data (ProfileCollectionIn): The details of the new profile collection.

        Returns:
            ProfileCollection: Details of the newly added profile collection.

        Returns:
            Any | None: The newly added profile collection.
        """

        query = profile_collection_table.insert().values(**data.model_dump())
        new_profile_collection_id = await database.execute(query)
        new_profile_collection = await self.get_by_id(new_profile_collection_id)

        return ProfileCollection(**dict(new_profile_collection)) if new_profile_collection else None

    async def update_profile_collection(
            self,
            profile_collection_id: int,
            data: ProfileCollectionIn,
    ) -> Any | None:
        """
        The method updating profile collection data in the database.

        Args:
            profile_collection_id (int): The id of the profile collection.
            data (ProfileCollectionIn): The details of the updated profile collection.

        Returns:
            Any | None: The updated profile collection details.
        """

        if self.get_by_id(profile_collection_id):
            query = (
                profile_collection_table.update()
                .where(profile_collection_table.c.id == profile_collection_id)
                .values(**data.model_dump())
            )
            await database.execute(query)

            profile_collection = await self.get_by_id(profile_collection_id)

            return ProfileCollection(**dict(profile_collection)) if profile_collection else None

        return None

    async def delete_profile_collection(self, profile_collection_id: int) -> bool:
        """
        The method removing profile collection from the database.

        Args:
            profile_collection_id (int): The id of the profile collection.

        Returns:
            bool: Success of the operation.
        """

        if await self.get_by_id(profile_collection_id):
            query = profile_collection_table \
                .delete() \
                .where(profile_collection_table.c.id == profile_collection_id)
            await database.execute(query)

            return True

        return False
