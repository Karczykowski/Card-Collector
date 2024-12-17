"""Module containing profile repository implementation."""

from typing import Any, Iterable

from asyncpg import Record  # type: ignore
from sqlalchemy import select, join

from card_collector.core.repositories.i_profile_repository import IProfileRepository
from card_collector.core.domains.profile import Profile, ProfileIn
from card_collector.db import (
    profile_table,
    database,
)

class ProfileRepository(IProfileRepository):
    """A class representing continent DB repository."""

    async def get_all_profiles(self) -> Iterable[Any]:
        """The method getting all profiles from the data storage.

        Returns:
            Iterable[Any]: Profiles in the data storage.
        """

        query = (
            select(profile_table)
            .order_by(profile_table.c.name.asc())
        )
        profiles = await database.fetch_all(query)

        return [Profile.from_record(profile) for profile in profiles]

    async def get_by_id(self, profile_id: int) -> Any | None:
        """The method getting profile by provided id.

        Args:
            profile_id (int): The id of the profile.

        Returns:
            Any | None: The profile details.
        """

        profile = await self._get_by_id(profile_id)

        return Profile.from_record(profile) if profile else None

    async def add_profile(self, data: ProfileIn) -> Any | None:
        """The method adding new profile to the data storage.

        Args:
            data (ProfileIn): The details of the new profile.

        Returns:
            Profile: Full details of the newly added profile.

        Returns:
            Any | None: The newly added profile.
        """

        query = profile_table.insert().values(**data.model_dump())
        new_profile_id = await database.execute(query)
        new_profile = await self._get_by_id(new_profile_id)

        return Profile(**dict(new_profile)) if new_profile else None

    async def update_profile(
            self,
            profile_id: int,
            data: ProfileIn,
    ) -> Any | None:
        """The method updating profile data in the data storage.

        Args:
            profile_id (int): The id of the profile.
            data (ProfileIn): The details of the updated profile.

        Returns:
            Any | None: The updated profile details.
        """

        if self._get_by_id(profile_id):
            query = (
                profile_table.update()
                .where(profile_table.c.id == profile_id)
                .values(**data.model_dump())
            )
            await database.execute(query)

            profile = await self._get_by_id(profile_id)

            return Profile(**dict(profile)) if profile else None

        return None

    async def delete_profile(self, profile_id: int) -> bool:
        """The method updating removing profile from the data storage.

        Args:
            profile_id (int): The id of the profile.

        Returns:
            bool: Success of the operation.
        """

        if self._get_by_id(profile_id):
            query = profile_table \
                .delete() \
                .where(profile_table.c.id == profile_id)
            await database.execute(query)

            return True

        return False

    async def _get_by_id(self, profile_id: int) -> Record | None:
        """A private method getting profile from the DB based on its ID.

        Args:
            profile_id (int): The ID of the profile.

        Returns:
            Any | None: Profile record if exists.
        """

        query = (
            profile_table.select()
            .where(profile_table.c.id == profile_id)
            .order_by(profile_table.c.name.asc())
        )

        return await database.fetch_one(query)
