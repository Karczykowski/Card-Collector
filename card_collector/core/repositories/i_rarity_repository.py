"""Module containing rarity repository abstractions."""

from abc import ABC, abstractmethod
from typing import Any, Iterable

from card_collector.core.domains.rarity import RarityIn


class IRarityRepository(ABC):
    """An abstract class representing protocol of continent repository."""

    @abstractmethod
    async def get_all_rarities(self) -> Iterable[Any]:
        """The abstract getting all raritys from the data storage.

        Returns:
            Iterable[Any]: Raritys in the data storage.
        """

    @abstractmethod
    async def get_by_id(self, rarity_id: int) -> Any | None:
        """The abstract getting rarity by provided id.

        Args:
            rarity_id (int): The id of the rarity.

        Returns:
            Any | None: The rarity details.
        """

    @abstractmethod
    async def add_rarity(self, data: RarityIn) -> Any | None:
        """The abstract adding new rarity to the data storage.

        Args:
            data (RarityIn): The details of the new rarity.

        Returns:
            Any | None: The newly added rarity.
        """

    @abstractmethod
    async def update_rarity(
            self,
            rarity_id: int,
            data: RarityIn,
    ) -> Any | None:
        """The abstract updating rarity data in the data storage.

        Args:
            rarity_id (int): The id of the rarity.
            data (RarityIn): The details of the updated rarity.

        Returns:
            Any | None: The updated rarity details.
        """

    @abstractmethod
    async def delete_rarity(self, rarity_id: int) -> bool:
        """The abstract updating removing rarity from the data storage.

        Args:
            rarity_id (int): The id of the rarity.

        Returns:
            bool: Success of the operation.
        """