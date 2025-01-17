from typing import Any, List

from sqlalchemy import select

from card_collector.core.repositories.i_profile_repository import IProfileRepository
from card_collector.core.domains.profile import Profile, ProfileIn
from card_collector.db import (
    profile_table,
    database,
)

class ProfileRepository(IProfileRepository):

    async def get_all_profiles(self) -> List[Any]:
        """
        The method getting all profiles from the database.

        Returns:
            List[Any]: Profiles in the database.
        """

        query = (
            select(profile_table)
        )
        profiles = await database.fetch_all(query)

        return [Profile.from_record(profile) for profile in profiles]

    async def get_by_id(self, profile_id: int) -> Any | None:
        """
        The method getting profile with a given id.

        Args:
            profile_id (int): The id of the profile.

        Returns:
            Any | None: The profile details.
        """
        query = (
            profile_table.select()
            .where(profile_table.c.id == profile_id)
        )

        profile = await database.fetch_one(query)

        return Profile.from_record(profile) if profile else None

    async def add_profile(self, data: ProfileIn) -> Any | None:
        """
        The method adding new profile to the database.

        Args:
            data (ProfileIn): The details of the new profile.

        Returns:
            Any | None: The newly added profile.
        """

        query = profile_table.insert().values(**data.model_dump())
        new_profile_id = await database.execute(query)
        new_profile = await self.get_by_id(new_profile_id)

        return Profile(**dict(new_profile)) if new_profile else None

    async def update_profile(
            self,
            profile_id: int,
            data: ProfileIn,
    ) -> Any | None:
        """
        The method updating profile data in the database.

        Args:
            profile_id (int): The id of the profile.
            data (ProfileIn): The details of the updated profile.

        Returns:
            Any | None: The updated profile details.
        """

        if self.get_by_id(profile_id):
            query = (
                profile_table.update()
                .where(profile_table.c.id == profile_id)
                .values(**data.model_dump())
            )
            await database.execute(query)

            profile = await self.get_by_id(profile_id)

            return Profile(**dict(profile)) if profile else None

        return None

    async def delete_profile(self, profile_id: int) -> bool:
        """
        The method removing profile from the database.

        Args:
            profile_id (int): The id of the profile.

        Returns:
            bool: Success of the operation.
        """

        if await self.get_by_id(profile_id):
            query = profile_table \
                .delete() \
                .where(profile_table.c.id == profile_id)
            await database.execute(query)

            return True

        return False
