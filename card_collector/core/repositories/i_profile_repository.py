from abc import ABC, abstractmethod
from typing import Any, List

from card_collector.core.domains.profile import ProfileIn

class IProfileRepository(ABC):

    @abstractmethod
    async def get_all_profiles(self) -> List[Any]:
        """
        The abstract class getting all profiles from the database.

        Returns:
            List[Any]: Profiles in the database.
        """

    @abstractmethod
    async def get_by_id(self, profile_id: int) -> Any | None:
        """
        The abstract class getting profile with given id.

        Args:
            profile_id (int): The id of the profile.

        Returns:
            Any | None: The profile details.
        """

    @abstractmethod
    async def add_profile(self, data: ProfileIn) -> Any | None:
        """
        The abstract class adding new profile to the database.

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
        """
        The abstract class updating profile data in the database.

        Args:
            profile_id (int): The id of the profile.
            data (ProfileIn): The details of the updated profile.

        Returns:
            Any | None: The updated profile details.
        """

    @abstractmethod
    async def delete_profile(self, profile_id: int) -> bool:
        """
        The abstract class updating removing profile from the database.

        Args:
            profile_id (int): The id of the profile.

        Returns:
            bool: Success of the operation.
        """
