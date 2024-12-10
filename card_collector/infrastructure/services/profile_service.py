"""Module containing continent service implementation."""

from typing import Iterable

from card_collector.core.domains.profile import Profile, ProfileIn
from card_collector.core.repositories.i_profile_repository import IProfileRepository
from card_collector.core.services.i_profile_service import IProfileService


class ProfileService(IProfileService):
    """A class implementing the profile service."""

    _repository: IProfileRepository

    def __init__(self, repository: IProfileRepository) -> None:
        """The initializer of the `profile service`.

        Args:
            repository (IProfileRepository): The reference to the repository.
        """
        self._repository = repository

    async def get_all(self) -> Iterable[Profile]:
        """The method getting all profiles from the repository.

        Returns:
            Iterable[Profile]: All profiles.
        """

        return await self._repository.get_all_profiles()

    async def get_by_id(self, profile_id: int) -> Profile | None:
        """The method getting profile by provided id.

        Args:
            profile_id (int): The id of the profile.

        Returns:
            Profile | None: The profile details.
        """

        return await self._repository.get_by_id(profile_id)

    async def add_profile(self, data: ProfileIn) -> Profile | None:
        """The method adding new profile to the data storage.

        Args:
            data (ProfileIn): The details of the new profile.

        Returns:
            Profile | None: Full details of the newly added profile.
        """

        return await self._repository.add_profile(data)

    async def update_profile(
            self,
            profile_id: int,
            data: ProfileIn,
    ) -> Profile | None:
        """The method updating profile data in the data storage.

        Args:
            profile_id (int): The id of the profile.
            data (ProfileIn): The details of the updated profile.

        Returns:
            Profile | None: The updated profile details.
        """

        return await self._repository.update_profile(
            profile_id=profile_id,
            data=data,
        )

    async def delete_profile(self, profile_id: int) -> bool:
        """The method updating removing profile from the data storage.

        Args:
            profile_id (int): The id of the profile.

        Returns:
            bool: Success of the operation.
        """

        return await self._repository.delete_profile(profile_id)
