"""Module providing containers injecting dependencies."""

from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Factory, Singleton

from card_collector.infrastructure.repositories.card_repository import CardRepository
from card_collector.infrastructure.repositories.rarity_repository import RarityRepository
from card_collector.infrastructure.services.card_service import CardService
from card_collector.infrastructure.services.rarity_service import RarityService
class Container(DeclarativeContainer):
    """Container class for dependency injecting purposes."""
    card_repository = Singleton(CardRepository)
    rarity_repository = Singleton(RarityRepository)

    card_service = Factory(
        CardService,
        repository=card_repository,
    )

    rarity_service = Factory(
        RarityService,
        repository=rarity_repository,
    )