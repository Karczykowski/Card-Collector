"""Module containing card service abstractions."""

from abc import ABC, abstractmethod
from typing import Iterable, List

from card_collector.core.domains.card import Card, CardIn


class ICardService(ABC):
    """A class representing card repository."""

    @abstractmethod
    async def get_all(self) -> Iterable[Card]:
        """The method getting all cards from the repository.

        Returns:
            Iterable[Card]: All cards.
        """

    async def get_all_by_rarity(self, rarity_id: int) -> Iterable[Card]:
        """The method getting all cards by id from the repository.

        Returns:
            Iterable[Card]: All cards.
        """

    @abstractmethod
    async def get_by_id(self, card_id: int) -> Card | None:
        """The method getting card by provided id.

        Args:
            card_id (int): The id of the card.

        Returns:
            Card | None: The card details.
        """


    @abstractmethod
    async def add_card(self, data: CardIn) -> Card | None:
        """The method adding new card to the data storage.

        Args:
            data (CardIn): The details of the new card.

        Returns:
            Card | None: Full details of the newly added card.
        """

    @abstractmethod
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

    @abstractmethod
    async def delete_card(self, card_id: int) -> bool:
        """The method updating removing card from the data storage.

        Args:
            card_id (int): The id of the card.

        Returns:
            bool: Success of the operation.
        """

    @abstractmethod
    async def get_random_cards_by_rarity(self, amount: int, rarity_id: int) -> List[Card]:
        """The method for generating a random card of a given rarity.

        Args:
            amount: amount of cards to generate.
            rarity_id (int): The id of rarity to generate.

        Returns:
            Card: generated card.
        """

    @abstractmethod
    async def get_random_cards(self, amount: int) -> List[Card]:
        """The method for generating random cards

        Args:
            amount (int): The number of cards to generate.

        Returns:
            Card: generated card.
        """
