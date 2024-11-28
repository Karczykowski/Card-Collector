"""Module containing continent service implementation."""

from typing import Iterable

from card_collector.core.domains.rarity import Rarity, RarityIn
from card_collector.core.repositories.i_rarity_repository import IRarityRepository
from card_collector.core.services.i_rarity_service import IRarityService


class RarityService(IRarityService):
    """A class implementing the rarity service."""

    _repository: IRarityRepository

    def __init__(self, repository: IRarityRepository) -> None:
        """The initializer of the `rarity service`.

        Args:
            repository (IRarityRepository): The reference to the repository.
        """

        self._repository = repository

    async def get_all(self) -> Iterable[Rarity]:
        """The method getting all rarities from the repository.

        Returns:
            Iterable[Rarity]: All rarities.
        """

        return await self._repository.get_all_rarities()

    async def get_by_id(self, rarity_id: int) -> Rarity | None:
        """The method getting rarity by provided id.

        Args:
            rarity_id (int): The id of the rarity.

        Returns:
            Rarity | None: The rarity details.
        """

        return await self._repository.get_by_id(rarity_id)

    async def add_rarity(self, data: RarityIn) -> Rarity | None:
        """The method adding new rarity to the data storage.

        Args:
            data (RarityIn): The details of the new rarity.

        Returns:
            Rarity | None: Full details of the newly added rarity.
        """

        return await self._repository.add_rarity(data)

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

        return await self._repository.update_rarity(
            rarity_id=rarity_id,
            data=data,
        )

    async def delete_rarity(self, rarity_id: int) -> bool:
        """The method updating removing rarity from the data storage.

        Args:
            rarity_id (int): The id of the rarity.

        Returns:
            bool: Success of the operation.
        """

        return await self._repository.delete_rarity(rarity_id)