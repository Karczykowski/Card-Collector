"""Module containing profile_collection repository implementation."""

from typing import Any, Iterable

from asyncpg import Record  # type: ignore
from sqlalchemy import select, join

from card_collector.core.repositories.i_profile_collection_repository import IProfileCollectionRepository
from card_collector.core.domains.profile_collection import ProfileCollection, ProfileCollectionIn
from card_collector.core.domains.card import Card
from card_collector.db import (
    profile_collection_table,
    card_table,
    database,
)

class ProfileCollectionRepository(IProfileCollectionRepository):
    """A class representing continent DB repository."""

    async def get_all_profile_collections(self) -> Iterable[Any]:
        """The method getting all profile_collections from the data storage.

        Returns:
            Iterable[Any]: ProfileCollections in the data storage.
        """

        query = (
            select(profile_collection_table)
        )
        profile_collections = await database.fetch_all(query)

        return [ProfileCollection.from_record(profile_collection) for profile_collection in profile_collections]

    async def get_by_id(self, profile_collection_id: int) -> Any | None:
        """The method getting profile_collection by provided id.

        Args:
            profile_collection_id (int): The id of the profile_collection.

        Returns:
            Any | None: The profile_collection details.
        """

        profile_collection = await self._get_by_id(profile_collection_id)

        return ProfileCollection.from_record(profile_collection) if profile_collection else None


    async def add_card_to_profile_collection(self, data: ProfileCollectionIn) -> Any | None:
        """The method adding new profile_collection to the data storage.

        Args:
            data (ProfileCollectionIn): The details of the new profile_collection.

        Returns:
            ProfileCollection: Full details of the newly added profile_collection.

        Returns:
            Any | None: The newly added profile_collection.
        """

        query = profile_collection_table.insert().values(**data.model_dump())
        new_profile_collection_id = await database.execute(query)
        new_profile_collection = await self._get_by_id(new_profile_collection_id)

        return ProfileCollection(**dict(new_profile_collection)) if new_profile_collection else None

    async def update_profile_collection(
            self,
            profile_collection_id: int,
            data: ProfileCollectionIn,
    ) -> Any | None:
        """The method updating profile_collection data in the data storage.

        Args:
            profile_collection_id (int): The id of the profile_collection.
            data (ProfileCollectionIn): The details of the updated profile_collection.

        Returns:
            Any | None: The updated profile_collection details.
        """

        if self._get_by_id(profile_collection_id):
            query = (
                profile_collection_table.update()
                .where(profile_collection_table.c.id == profile_collection_id)
                .values(**data.model_dump())
            )
            await database.execute(query)

            profile_collection = await self._get_by_id(profile_collection_id)

            return ProfileCollection(**dict(profile_collection)) if profile_collection else None

        return None

    async def delete_profile_collection(self, profile_collection_id: int) -> bool:
        """The method updating removing profile_collection from the data storage.

        Args:
            profile_collection_id (int): The id of the profile_collection.

        Returns:
            bool: Success of the operation.
        """

        if self._get_by_id(profile_collection_id):
            query = profile_collection_table \
                .delete() \
                .where(profile_collection_table.c.id == profile_collection_id)
            await database.execute(query)

            return True

        return False

    async def _get_by_id(self, profile_collection_id: int) -> Record | None:
        """A private method getting profile_collection from the DB based on its ID.

        Args:
            profile_collection_id (int): The ID of the profile_collection.

        Returns:
            Any | None: ProfileCollection record if exists.
        """

        query = (
            profile_collection_table.select()
            .where(profile_collection_table.c.id == profile_collection_id)
        )

        return await database.fetch_one(query)
