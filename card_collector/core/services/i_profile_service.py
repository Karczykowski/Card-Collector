"""Module containing profile service abstractions."""

from abc import ABC, abstractmethod
from typing import Iterable

from card_collector.core.domains.profile import Profile, ProfileIn


class IProfileService(ABC):
    """A class representing profile repository."""

    @abstractmethod
    async def get_all(self) -> Iterable[Profile]:
        """The method getting all profiles from the repository.

        Returns:
            Iterable[Profile]: All profiles.
        """


    @abstractmethod
    async def get_by_id(self, profile_id: int) -> Profile | None:
        """The method getting profile by provided id.

        Args:
            profile_id (int): The id of the profile.

        Returns:
            Profile | None: The profile details.
        """


    @abstractmethod
    async def add_profile(self, data: ProfileIn) -> Profile | None:
        """The method adding new profile to the data storage.

        Args:
            data (ProfileIn): The details of the new profile.

        Returns:
            Profile | None: Full details of the newly added profile.
        """

    @abstractmethod
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

    @abstractmethod
    async def delete_profile(self, profile_id: int) -> bool:
        """The method updating removing profile from the data storage.

        Args:
            profile_id (int): The id of the profile.

        Returns:
            bool: Success of the operation.
        """