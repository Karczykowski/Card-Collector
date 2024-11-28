"""Module containing rarity service abstractions."""

from abc import ABC, abstractmethod
from typing import Iterable

from card_collector.core.domains.rarity import Rarity, RarityIn


class IRarityService(ABC):
    """A class representing rarity repository."""

    @abstractmethod
    async def get_all(self) -> Iterable[Rarity]:
        """The method getting all rarities from the repository.

        Returns:
            Iterable[Rarity]: All rarities.
        """


    @abstractmethod
    async def get_by_id(self, rarity_id: int) -> Rarity | None:
        """The method getting rarity by provided id.

        Args:
            rarity_id (int): The id of the rarity.

        Returns:
            Rarity | None: The rarity details.
        """


    @abstractmethod
    async def add_rarity(self, data: RarityIn) -> Rarity | None:
        """The method adding new rarity to the data storage.

        Args:
            data (RarityIn): The details of the new rarity.

        Returns:
            Rarity | None: Full details of the newly added rarity.
        """

    @abstractmethod
    async def update_rarity(
            self,
            rarity_id: int,
            data: RarityIn,
    ) -> Rarity | None:
        """The method updating rarity data in the data storage.

        Args:
            rarity_id (int): The id of the rarity.
            data (RarityIn): The details of the updated rarity.

        Returns:
            Rarity | None: The updated rarity details.
        """

    @abstractmethod
    async def delete_rarity(self, rarity_id: int) -> bool:
        """The method updating removing rarity from the data storage.

        Args:
            rarity_id (int): The id of the rarity.

        Returns:
            bool: Success of the operation.
        """