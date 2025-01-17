import string
from abc import ABC, abstractmethod
from typing import Any, List

from card_collector.core.domains.card import CardIn

class ICardRepository(ABC):

    @abstractmethod
    async def get_all_cards(self) -> List[Any]:
        """
        The abstract class getting all cards from the database.

        Returns:
            List[Any]: Cards in the database.
        """

    @abstractmethod
    async def get_all_by_rarity(self, rarity_id: int) -> List[Any]:
        """
        The abstract class getting all cards with a given rarity from the database.

        Args:
            rarity_id (int): The id of the rarity.
        Returns:
            List[Any]: Cards in the database.
        """

    @abstractmethod
    async def get_by_id(self, card_id: int) -> Any | None:
        """
        The abstract class getting card by given id.

        Args:
            card_id (int): The id of the card.

        Returns:
            Any | None: The card details.
        """

    @abstractmethod
    async def get_by_name(self, name: string) -> Any | None:
        """
        The abstract class getting card by given name.

        Args:
            name (string): The name of the card.

        Returns:
            Any | None: The card details.
        """

    @abstractmethod
    async def add_card(self, data: CardIn) -> Any | None:
        """
        The abstract class adding new card to the database.

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
        """
        The abstract class updating card data in the database.

        Args:
            card_id (int): The id of the card.
            data (CardIn): The details of the updated card.

        Returns:
            Any | None: The updated card details.
        """

    @abstractmethod
    async def delete_card(self, card_id: int) -> bool:
        """
        The abstract class removing card from the database.

        Args:
            card_id (int): The id of the card.

        Returns:
            bool: Success of the operation.
        """
        