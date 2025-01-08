"""Module providing containers injecting dependencies."""

from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Factory, Singleton

from card_collector.db import profile_collection_table
from card_collector.infrastructure.repositories.card_repository import CardRepository
from card_collector.infrastructure.services.card_service import CardService

from card_collector.infrastructure.repositories.profile_repository import ProfileRepository
from card_collector.infrastructure.services.profile_service import ProfileService

from card_collector.infrastructure.repositories.profile_collection_repository import ProfileCollectionRepository
from card_collector.infrastructure.services.profile_collection_service import ProfileCollectionService

from card_collector.infrastructure.repositories.trade_offer_repository import TradeOfferRepository
from card_collector.infrastructure.services.trade_offer_service import TradeOfferService

class Container(DeclarativeContainer):
    """Container class for dependency injecting purposes."""
    card_repository = Singleton(CardRepository)
    profile_repository = Singleton(ProfileRepository)
    profile_collection_repository = Singleton(ProfileCollectionRepository)
    trade_offer_repository = Singleton(TradeOfferRepository)

    card_service = Factory(
        CardService,
        repository=card_repository,
    )

    profile_collection_service = Factory(
        ProfileCollectionService,
        repository=profile_collection_repository
    )

    profile_service = Factory(
        ProfileService,
        repository=profile_repository,
        card_service=card_service,
        profile_collection_service=profile_collection_service
    )

    trade_offer_service = Factory(
        TradeOfferService,
        repository=trade_offer_repository,
    )

