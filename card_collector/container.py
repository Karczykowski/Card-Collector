from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Factory, Singleton

from card_collector.infrastructure.repositories.card_repository import CardRepository
from card_collector.infrastructure.services.card_service import CardService

from card_collector.infrastructure.repositories.profile_repository import ProfileRepository
from card_collector.infrastructure.services.profile_service import ProfileService

from card_collector.infrastructure.repositories.profile_collection_repository import ProfileCollectionRepository
from card_collector.infrastructure.services.profile_collection_service import ProfileCollectionService

from card_collector.infrastructure.repositories.trade_offer_repository import TradeOfferRepository
from card_collector.infrastructure.services.trade_offer_service import TradeOfferService

from card_collector.infrastructure.repositories.quest_repository import QuestRepository
from card_collector.infrastructure.services.quest_service import QuestService

from card_collector.infrastructure.services.collection_integration_service import CollectionIntegrationService

class Container(DeclarativeContainer):
    card_repository = Singleton(CardRepository)
    profile_repository = Singleton(ProfileRepository)
    profile_collection_repository = Singleton(ProfileCollectionRepository)
    trade_offer_repository = Singleton(TradeOfferRepository)
    quest_repository = Singleton(QuestRepository)

    trade_offer_service = Factory(
        TradeOfferService,
        repository=trade_offer_repository,
    )

    quest_service = Factory(
        QuestService,
        repository=quest_repository
    )

    profile_collection_service = Factory(
        ProfileCollectionService,
        repository=profile_collection_repository,
        trade_offer_service=trade_offer_service,
        quest_service=quest_service
    )

    collection_integration_service = Factory(
        CollectionIntegrationService,
        profile_collection_service=profile_collection_service,
        trade_offer_service=trade_offer_service
    )

    card_service = Factory(
        CardService,
        repository=card_repository,
        profile_collection_service=profile_collection_service,
    )

    profile_service = Factory(
        ProfileService,
        repository=profile_repository,
        card_service=card_service,
        profile_collection_service=profile_collection_service,
        quest_service=quest_service
    )
