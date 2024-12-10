"""Module providing containers injecting dependencies."""

from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Factory, Singleton

from card_collector.infrastructure.repositories.card_repository import CardRepository
from card_collector.infrastructure.services.card_service import CardService

from card_collector.infrastructure.repositories.profile_repository import ProfileRepository
from card_collector.infrastructure.services.profile_service import ProfileService

from card_collector.infrastructure.repositories.profile_collection_repository import ProfileCollectionRepository
from card_collector.infrastructure.services.profile_collection_service import ProfileCollectionService

class Container(DeclarativeContainer):
    """Container class for dependency injecting purposes."""
    card_repository = Singleton(CardRepository)
    profile_repository = Singleton(ProfileRepository)
    profile_collection_repository = Singleton(ProfileCollectionRepository)

    card_service = Factory(
        CardService,
        repository=card_repository,
    )

    profile_service = Factory(
        ProfileService,
        repository=profile_repository,
    )

    profile_collection_service = Factory(
        ProfileCollectionService,
        repository=profile_collection_repository
    )