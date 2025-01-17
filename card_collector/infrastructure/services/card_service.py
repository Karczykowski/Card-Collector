import random
from typing import List

from card_collector.core.domains.card import Card, CardIn
from card_collector.core.repositories.i_card_repository import ICardRepository
from card_collector.core.services.i_card_service import ICardService
from card_collector.core.services.i_profile_collection_service import IProfileCollectionService

class CardService(ICardService):

    _repository: ICardRepository
    _profile_collection_service: IProfileCollectionService

    def __init__(self, repository: ICardRepository, profile_collection_service: IProfileCollectionService) -> None:
        """
        The initializer of the card service.

        Args:
            repository (ICardRepository): The reference to the repository.
            profile_collection_service (IProfileCollectionService): The reference to the profile collection service.
        """
        self._repository = repository
        self._profile_collection_service = profile_collection_service

    async def get_all(self) -> List[Card]:
        """
        The method getting all cards from the repository.

        Returns:
            List[Card]: All cards.
        """

        return await self._repository.get_all_cards()

    async def get_all_by_rarity(self, rarity_id: int) -> List[Card]:
        """
        The method getting all cards with a given rarity id from the repository.

        Returns:
            List[Card]: Cards.
        """

        return await self._repository.get_all_by_rarity(rarity_id)

    async def get_by_id(self, card_id: int) -> Card | None:
        """
        The method getting card with a given id.

        Args:
            card_id (int): The id of the card.

        Returns:
            Card | None: The card details.
        """

        return await self._repository.get_by_id(card_id)

    async def get_random_cards_by_rarity(self, amount: int, rarity_id: int) -> List[Card]:
        """
        The method for generating a given amount of random cards with a given rarity.

        Args:
            amount (int): amount of cards to generate.
            rarity_id (int): The id of rarity to generate.

        Returns:
            Card: generated card.
        """
        cards = []

        for _ in range(amount):
            cards.append(random.choice(list(await self.get_all_by_rarity(rarity_id))))

        return cards

    async def get_random_cards(self, amount: int) -> List[Card]:
        """
        The method for generating random cards

        Args:
            amount (int): The number of cards to generate.

        Returns:
            List[Card]: Generated cards.
        """
        cards = []

        for _ in range(amount):
            cards.append(random.choice(list(await self._repository.get_all_cards())))

        return cards


    async def add_card(self, data: CardIn) -> Card | None:
        """
        The method adding new card to the database.

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
        """
        The method updating card data in the database.

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
        """
        The method removing card from the database.

        Args:
            card_id (int): The id of the card.

        Returns:
            bool: Success of the operation.
        """

        return await self._repository.delete_card(card_id)
