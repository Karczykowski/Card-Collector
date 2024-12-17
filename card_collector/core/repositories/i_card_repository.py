"""Module containing card repository abstractions."""

from abc import ABC, abstractmethod
from typing import Any, Iterable

from card_collector.core.domains.card import CardIn


class ICardRepository(ABC):
    """An abstract class representing protocol of continent repository."""

    @abstractmethod
    async def get_all_cards(self) -> Iterable[Any]:
        """The abstract getting all cards from the data storage.

        Returns:
            Iterable[Any]: Cards in the data storage.
        """

    @abstractmethod
    async def get_by_id(self, card_id: int) -> Any | None:
        """The abstract getting card by provided id.

        Args:
            card_id (int): The id of the card.

        Returns:
            Any | None: The card details.
        """

    @abstractmethod
    async def add_card(self, data: CardIn) -> Any | None:
        """The abstract adding new card to the data storage.

        Args:
            data (CardIn): The details of the new card.

        Returns:
            Any | None: The newly added card.
        """

    @abstractmethod
    async def update_card(
            self,
            card_id: int,
            data: CardIn,
    ) -> Any | None:
        """The abstract updating card data in the data storage.

        Args:
            card_id (int): The id of the card.
            data (CardIn): The details of the updated card.

        Returns:
            Any | None: The updated card details.
        """

    @abstractmethod
    async def delete_card(self, card_id: int) -> bool:
        """The abstract updating removing card from the data storage.

        Args:
            card_id (int): The id of the card.

        Returns:
            bool: Success of the operation.
        """
