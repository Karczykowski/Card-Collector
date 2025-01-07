"""Module containing continent service implementation."""
import random
from typing import Iterable

from card_collector.core.domains.card import Card, CardIn
from card_collector.core.repositories.i_card_repository import ICardRepository
from card_collector.core.services.i_card_service import ICardService


class CardService(ICardService):
    """A class implementing the card service."""

    _repository: ICardRepository

    def __init__(self, repository: ICardRepository) -> None:
        """The initializer of the `card service`.

        Args:
            repository (ICardRepository): The reference to the repository.
        """
        self._repository = repository

    async def get_all(self) -> Iterable[Card]:
        """The method getting all cards from the repository.

        Returns:
            Iterable[Card]: All cards.
        """

        return await self._repository.get_all_cards()

    async def get_all_by_rarity(self, rarity_id: int) -> Iterable[Card]:
        """The method getting all cards by id from the repository.

        Returns:
            Iterable[Card]: All cards.
        """

        return await self._repository.get_all_by_rarity(rarity_id)

    async def get_by_id(self, card_id: int) -> Card | None:
        """The method getting card by provided id.

        Args:
            card_id (int): The id of the card.

        Returns:
            Card | None: The card details.
        """

        return await self._repository.get_by_id(card_id)

    async def add_card(self, data: CardIn) -> Card | None:
        """The method adding new card to the data storage.

        Args:
            data (CardIn): The details of the new card.

        Returns:
            Card | None: Full details of the newly added card.
        """

        return await self._repository.add_card(data)

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

        return await self._repository.update_card(
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

        return await self._repository.delete_card(card_id)

    async def get_random_by_id(self, rarity_id: int) -> Card:
        """The method for generating a random card of a given rarity.

        Args:
            rarity_id (int): The id of rarity to generate.

        Returns:
            Card: generated card.
        """

        return random.choice(list(await self._repository.get_all_by_rarity(rarity_id)))
