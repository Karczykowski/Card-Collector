"""Module containing profile repository abstractions."""

from abc import ABC, abstractmethod
from typing import Any, Iterable

from card_collector.core.domains.profile import ProfileIn


class IProfileRepository(ABC):
    """An abstract class representing protocol of continent repository."""

    @abstractmethod
    async def get_all_profiles(self) -> Iterable[Any]:
        """The abstract getting all profiles from the data storage.

        Returns:
            Iterable[Any]: Profiles in the data storage.
        """

    @abstractmethod
    async def get_by_id(self, profile_id: int) -> Any | None:
        """The abstract getting profile by provided id.

        Args:
            profile_id (int): The id of the profile.

        Returns:
            Any | None: The profile details.
        """

    @abstractmethod
    async def add_profile(self, data: ProfileIn) -> Any | None:
        """The abstract adding new profile to the data storage.

        Args:
            data (ProfileIn): The details of the new profile.

        Returns:
            Any | None: The newly added profile.
        """

    @abstractmethod
    async def update_profile(
            self,
            profile_id: int,
            data: ProfileIn,
    ) -> Any | None:
        """The abstract updating profile data in the data storage.

        Args:
            profile_id (int): The id of the profile.
            data (ProfileIn): The details of the updated profile.

        Returns:
            Any | None: The updated profile details.
        """

    @abstractmethod
    async def delete_profile(self, profile_id: int) -> bool:
        """The abstract updating removing profile from the data storage.

        Args:
            profile_id (int): The id of the profile.

        Returns:
            bool: Success of the operation.
        """

    @abstractmethod
    async def open_pack(self, profile_id: int) -> bool:
        """

        """









