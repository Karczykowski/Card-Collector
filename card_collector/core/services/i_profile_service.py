from abc import ABC, abstractmethod
from typing import List

from card_collector.core.domains.profile import Profile, ProfileIn
from card_collector.core.domains.card import Card

class IProfileService(ABC):

    @abstractmethod
    async def get_all(self) -> List[Profile]:
        """
        The method getting all profiles from the repository.

        Returns:
            List[Profile]: All profiles.
        """


    @abstractmethod
    async def get_by_id(self, profile_id: int) -> Profile | None:
        """
        The method getting profile by given id.

        Args:
            profile_id (int): The id of the profile.

        Returns:
            Profile | None: The profile details.
        """


    @abstractmethod
    async def add_profile(self, data: ProfileIn) -> Profile | None:
        """
        The method adding new profile to the database.

        Args:
            data (ProfileIn): The details of the new profile.

        Returns:
            Profile | None: Full details of the newly added profile.
        """

    @abstractmethod
    async def open_pack(self, profile_id: int, amount_of_cards: int) -> List[Card]:
        """
        The method for opening a pack of 5 cards and adding it to profile collection

        Args:
            profile_id (int): The id of the profile.
            amount_of_cards (int): Amount of cards in a pack.

        Returns:
            List[Card]: List of cards opened.
        """

    @abstractmethod
    async def update_profile(
            self,
            profile_id: int,
            data: ProfileIn,
    ) -> Profile | None:
        """
        The method updating profile data in the database.

        Args:
            profile_id (int): The id of the profile.
            data (ProfileIn): The details of the updated profile.

        Returns:
            Profile | None: The updated profile details.
        """

    @abstractmethod
    async def delete_profile(self, profile_id: int) -> bool:
        """
        The method removing profile from the database.

        Args:
            profile_id (int): The id of the profile.

        Returns:
            bool: Success of the operation.
        """
