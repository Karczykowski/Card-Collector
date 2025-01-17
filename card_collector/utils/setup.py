from dependency_injector.wiring import Provide

from card_collector.core.domains.card import CardIn
from card_collector.core.domains.profile import ProfileIn
from card_collector.core.domains.profile_collection import ProfileCollectionIn
from card_collector.core.domains.trade_offer import TradeOfferIn
from card_collector.core.domains.quest import QuestIn
from card_collector.core.services.i_card_service import ICardService
from card_collector.core.services.i_profile_service import IProfileService
from card_collector.core.services.i_profile_collection_service import IProfileCollectionService
from card_collector.core.services.i_trade_offer_service import ITradeOfferService
from card_collector.core.services.i_quest_service import IQuestService
from card_collector.container import Container

async def main(
        card_service: ICardService = Provide[Container.card_service],
        profile_service: IProfileService = Provide[Container.profile_service],
        profile_collection_service: IProfileCollectionService = Provide[Container.profile_collection_service],
        trade_offer_service: ITradeOfferService = Provide[Container.trade_offer_service],
        quest_service: IQuestService = Provide[Container.quest_repository],

):
    cards = []
    profiles = []
    cards_data = (
        ("Strike", 1),
        ("Hit", 1),
        ("Defend", 1),
        ("Attack", 1),
        ("Shield", 1),
        ("Swarm", 1),
        ("Thunder", 1),
        ("Fire", 1),
        ("Water", 1),
        ("Fairy", 1),
        ("Dragon", 1),
        ("Fight", 1),
        ("Superheat", 2),
        ("Waterfall", 2),
        ("Firestorm", 2),
        ("Earthquake", 2),
        ("Blizzard", 2),
        ("Heaven", 3),
        ("Hell", 3),
        ("God", 3),
    )

    for card in cards_data:
        cards.append(
            await card_service.add_card(CardIn(
                name=card[0],
                rarity_id=card[1]
            ))
        )

    profiles_data = (
        "Stephan",
        "Jake",
        "Gretchen",
        "Mary",
        "Richard",
        "Gregory"
    )

    for profile in profiles_data:
        profiles.append(
            await profile_service.add_profile(ProfileIn(
                name=profile
            ))
        )

    profile_collection_data = (
        (0, 0),
        (0, 1),
        (0, 5),
        (0, 15),
        (1, 1),
        (1, 1),
        (1, 1),
        (1, 6),
        (1, 12),
        (1, 13),
        (2, 3),
        (2, 4),
        (2, 5),
        (3, 9),
        (3, 10),
        (3, 17),
        (3, 19),
        (3, 2),
        (3, 3),
        (3, 17),
        (4, 17),
        (4, 18),
        (4, 19),
    )

    for profile_collection in profile_collection_data:
        await profile_collection_service.add_profile_collection(ProfileCollectionIn(
            profile_id=profiles[profile_collection[0]].id,
            card_id=cards[profile_collection[1]].id
        ))

    trade_offer_data = (
        (0, 0 , 17),
        (2, 4, 17),
        (2, 5, 17),
        (2, 5, 16),
        (2, 5, 15),
        (3, 9, 1),
        (3, 2, 3),
        (4, 19, 5),
        (4, 19, 5),
    )

    for trade_offer in trade_offer_data:
        await trade_offer_service.add_trade_offer(TradeOfferIn(
            profile_posted=profiles[trade_offer[0]].id,
            card_offered=cards[trade_offer[1]].id,
            card_wanted=cards[trade_offer[2]].id
        ))

    quests_data = (
        (2, 2, 8, 18),
        (2, 13, 15, 15),
        (3, 0, 11, 18),
        (5, 7, 9, 13),
    )

    for quest in quests_data:
        await quest_service.add_quest(QuestIn(
            profile_id=profiles[quest[0]].id,
            cards_collected=quest[1],
            cards_needed=quest[2],
            reward=cards[quest[3]].id,
        ))
