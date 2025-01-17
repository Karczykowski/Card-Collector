from typing import List

from card_collector.core.domains.trade_offer import TradeOffer, TradeOfferIn
from card_collector.core.repositories.i_trade_offer_repository import ITradeOfferRepository
from card_collector.core.services.i_trade_offer_service import ITradeOfferService

class TradeOfferService(ITradeOfferService):

    _repository: ITradeOfferRepository

    def __init__(self, repository: ITradeOfferRepository) -> None:
        """
        The initializer of the trade offer service.

        Args:
            repository (ITradeOfferRepository): The reference to the repository.
        """
        self._repository = repository

    async def get_all(self) -> List[TradeOffer]:
        """
        The method getting all trade offers from the repository.

        Returns:
            List[TradeOffer]: All trade_offers.
        """

        return await self._repository.get_all_trade_offers()

    async def get_all_by_card_offered(self, card_offered: int) -> List[TradeOffer]:
        """
        The method getting all trade offers with a given card offered id from the repository.

        Args:
            card_offered (int): the id of card offered.

        Returns:
            List[TradeOffer]: Trade offers.
        """

        return await self._repository.get_all_by_card_offered(card_offered)

    async def get_all_by_card_wanted(self, card_wanted: int) -> List[TradeOffer]:
        """
        The method getting all trade offers with a given card wanted id from the repository.

        Args:
            card_wanted (int): the id of card wanted.

        Returns:
            List[TradeOffer]: Trade offers.
        """

        return await self._repository.get_all_by_card_wanted(card_wanted)

    async def get_all_by_profile_id_and_card_offered_id(
            self,
            profile_id: int,
            card_offered_id: int
    ) -> List[TradeOffer] | None:
        """
        The method getting trade offer with a given profile id and card offered id from the repository.

        Args:
            profile_id (int): the id of profile.
            card_offered_id (int): the id of card_offered.

        Returns:
            List[TradeOffer] | None: The trade_offer details.
        """

        return await self._repository.get_by_profile_id_and_card_offered_id(profile_id, card_offered_id)

    async def get_by_id(self, trade_offer_id: int) -> TradeOffer | None:
        """
        The method getting trade offer with a given id from the repository.

        Args:
            trade_offer_id (int): The id of the trade offer.

        Returns:
            TradeOffer | None: The trade offer details.
        """

        return await self._repository.get_by_id(trade_offer_id)

    async def get_by_offer(self, card_offered: int, card_wanted: int) -> TradeOffer | None:
        """
        The method getting trade offer with a given offer id from the repository.

        Args:
            card_offered (int): the id of card offered.
            card_wanted (int): the id of card wanted.

        Returns:
            TradeOffer | None: The trade_offer details.
        """

        return await self._repository.get_by_offer(card_offered, card_wanted)

    async def add_trade_offer(self, data: TradeOfferIn) -> TradeOffer | None:
        """
        The method adding new trade offer to the database.

        Args:
            data (ProfileIn): The details of the new trade offer.

        Returns:
            Profile | None: Full details of the newly added trade offer.
        """

        return await self._repository.add_trade_offer(data)

    async def update_trade_offer(
            self,
            trade_offer_id: int,
            data: TradeOfferIn,
    ) -> TradeOffer | None:
        """
        The method updating trade offer data in the database.

        Args:
            trade_offer_id (int): The id of the trade offer.
            data (TradeOfferIn): The details of the updated trade offer.

        Returns:
            TradeOffer | None: The updated trade offer details.
        """

        return await self._repository.update_trade_offer(
            trade_offer_id=trade_offer_id,
            data=data,
        )

    async def delete_trade_offer(self, trade_offer_id: int) -> bool:
        """
        The method removing trade offer from the database.

        Args:
            trade_offer_id (int): The id of the trade offer.

        Returns:
            bool: Success of the operation.
        """

        return await self._repository.delete_trade_offer(trade_offer_id)

    async def delete_trade_offer_by_profile_id_and_card_offered_id(
            self,
            profile_id: int,
            card_offered_id: int
    ) -> List[bool]:
        """
        The method removing trade offer with a given profile id and card id from the database.

        Args:
            profile_id (int): the id of profile.
            card_offered_id (int): the id of card offered.

        Returns:
            bool: Success of the operation.
        """
        trade_offers = await self.get_all_by_profile_id_and_card_offered_id(profile_id, card_offered_id)
        return [await self._repository.delete_trade_offer(trade_offer.id) for trade_offer in trade_offers]
