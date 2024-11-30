"""Module containing continent service implementation."""

from typing import Iterable

from card_collector.core.domains.card import Card, CardIn
from card_collector.core.repositories.i_card_repository import ICardRepository
from card_collector.core.services.i_card_service import ICardService
from card_collector.core.repositories.i_rarity_repository import IRarityRepository


class CardService(ICardService):
    """A class implementing the card service."""

    _card_repository: ICardRepository
    _rarity_repository: IRarityRepository

    def __init__(self, card_repository: ICardRepository, rarity_repository: IRarityRepository) -> None:
        """The initializer of the `card service`.

        Args:
            repository (ICardRepository): The reference to the repository.
        """
        self._rarity_repository = rarity_repository
        self._card_repository = card_repository

    async def get_all(self) -> Iterable[Card]:
        """The method getting all cards from the repository.

        Returns:
            Iterable[Card]: All cards.
        """

        return await self._card_repository.get_all_cards()

    async def get_by_id(self, card_id: int) -> Card | None:
        """The method getting card by provided id.

        Args:
            card_id (int): The id of the card.

        Returns:
            Card | None: The card details.
        """

        return await self._card_repository.get_by_id(card_id)

    async def add_card(self, data: CardIn) -> Card | None:
        """The method adding new card to the data storage.

        Args:
            data (CardIn): The details of the new card.

        Returns:
            Card | None: Full details of the newly added card.
        """

        if await self._rarity_repository.get_by_id(data.rarity_id) is None:
            return None

        return await self._card_repository.add_card(data)

    async def update_card(
            self,
            card_id: int,
            data: CardIn,
    ) -> Card | None:
        """The method updating card data in the data storage.

        Args:
            card_id (int): The id of the card.
            data (CardIn): The details of the updated card.

        Returns:
            Card | None: The updated card details.
        """

        return await self._card_repository.update_card(
            card_id=card_id,
            data=data,
        )

    async def delete_card(self, card_id: int) -> bool:
        """The method updating removing card from the data storage.

        Args:
            card_id (int): The id of the card.

        Returns:
            bool: Success of the operation.
        """

        return await self._card_repository.delete_card(card_id)
