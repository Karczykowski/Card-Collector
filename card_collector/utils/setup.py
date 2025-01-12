from dependency_injector.wiring import Provide

from card_collector.core.domains.card import CardIn
from card_collector.core.domains.profile import ProfileIn
from card_collector.core.domains.profile_collection import ProfileCollectionIn
from card_collector.core.domains.trade_offer import TradeOfferIn
from card_collector.core.services.i_card_service import ICardService
from card_collector.core.services.i_profile_service import IProfileService
from card_collector.core.services.i_profile_collection_service import IProfileCollectionService
from card_collector.core.services.i_trade_offer_service import ITradeOfferService
from card_collector.container import Container

async def main(
        card_service: ICardService = Provide[Container.card_service],
        profile_service: IProfileService = Provide[Container.profile_service],
        profile_collection_service: IProfileCollectionService = Provide[Container.profile_collection_service],
        trade_offer_service: ITradeOfferService = Provide[Container.trade_offer_service],

):
    cards = []
    profiles = []
    """
    Adding Cards
    """
    cards.append(
        await card_service.add_card(CardIn(
            name="Strike",
            rarity_id=1
        ))
    )

    cards.append(
        await card_service.add_card(CardIn(
            name="Hit",
            rarity_id=1
        ))
    )

    cards.append(
        await card_service.add_card(CardIn(
            name="Defend",
            rarity_id=1
        ))
    )

    cards.append(
        await card_service.add_card(CardIn(
            name="Attack",
            rarity_id=1
        ))
    )

    cards.append(
        await card_service.add_card(CardIn(
            name="Shield",
            rarity_id=1
        ))
    )

    cards.append(
        await card_service.add_card(CardIn(
            name="Swarm",
            rarity_id=1
        ))
    )

    cards.append(
        await card_service.add_card(CardIn(
            name="Thunder",
            rarity_id=1
        ))
    )

    cards.append(
        await card_service.add_card(CardIn(
            name="Fire",
            rarity_id=1
        ))
    )

    cards.append(
        await card_service.add_card(CardIn(
            name="Water",
            rarity_id=1
        ))
    )

    cards.append(
        await card_service.add_card(CardIn(
            name="Fairy",
            rarity_id=1
        ))
    )

    cards.append(
        await card_service.add_card(CardIn(
            name="Dragon",
            rarity_id=1
        ))
    )

    cards.append(
        await card_service.add_card(CardIn(
            name="Fight",
            rarity_id=1
        ))
    )

    cards.append(
        await card_service.add_card(CardIn(
            name="Superhit",
            rarity_id=2
        ))
    )

    cards.append(
        await card_service.add_card(CardIn(
            name="Waterfall",
            rarity_id=2
        ))
    )

    cards.append(
        await card_service.add_card(CardIn(
            name="Firestorm",
            rarity_id=2
        ))
    )

    cards.append(
        await card_service.add_card(CardIn(
            name="Earthquake",
            rarity_id=2
        ))
    )

    cards.append(
        await card_service.add_card(CardIn(
            name="Blizzard",
            rarity_id=2
        ))
    )

    cards.append(
        await card_service.add_card(CardIn(
            name="Heaven",
            rarity_id=3
        ))
    )

    cards.append(
        await card_service.add_card(CardIn(
            name="Hell",
            rarity_id=3
        ))
    )

    cards.append(
        await card_service.add_card(CardIn(
            name="God",
            rarity_id=3
        ))
    )
    """
    Adding Users
    """
    profiles.append(
        await profile_service.add_profile(ProfileIn(
            name="Stephan",
        ))
    )

    profiles.append(
        await profile_service.add_profile(ProfileIn(
            name="Jake",
        ))
    )

    profiles.append(
        await profile_service.add_profile(ProfileIn(
            name="Gretchen",
        ))
    )

    profiles.append(
        await profile_service.add_profile(ProfileIn(
            name="Mary",
        ))
    )

    profiles.append(
        await profile_service.add_profile(ProfileIn(
            name="Richard",
        ))
    )

    profiles.append(
        await profile_service.add_profile(ProfileIn(
            name="Gregory",
        ))
    )


    """
    Adding Cards to Profiles
    """

    await profile_collection_service.add_card_to_profile_collection(ProfileCollectionIn(
        profile_id=profiles[0].id,
        card_id=cards[0].id
    ))

    await profile_collection_service.add_card_to_profile_collection(ProfileCollectionIn(
        profile_id=profiles[0].id,
        card_id=cards[1].id
    ))

    await profile_collection_service.add_card_to_profile_collection(ProfileCollectionIn(
        profile_id=profiles[0].id,
        card_id=cards[5].id
    ))

    await profile_collection_service.add_card_to_profile_collection(ProfileCollectionIn(
        profile_id=profiles[0].id,
        card_id=cards[15].id
    ))

    await profile_collection_service.add_card_to_profile_collection(ProfileCollectionIn(
        profile_id=profiles[1].id,
        card_id=cards[1].id
    ))

    await profile_collection_service.add_card_to_profile_collection(ProfileCollectionIn(
        profile_id=profiles[1].id,
        card_id=cards[1].id
    ))

    await profile_collection_service.add_card_to_profile_collection(ProfileCollectionIn(
        profile_id=profiles[1].id,
        card_id=cards[1].id
    ))

    await profile_collection_service.add_card_to_profile_collection(ProfileCollectionIn(
        profile_id=profiles[1].id,
        card_id=cards[6].id
    ))

    await profile_collection_service.add_card_to_profile_collection(ProfileCollectionIn(
        profile_id=profiles[1].id,
        card_id=cards[12].id
    ))

    await profile_collection_service.add_card_to_profile_collection(ProfileCollectionIn(
        profile_id=profiles[1].id,
        card_id=cards[13].id
    ))

    await profile_collection_service.add_card_to_profile_collection(ProfileCollectionIn(
        profile_id=profiles[2].id,
        card_id=cards[3].id
    ))
    await profile_collection_service.add_card_to_profile_collection(ProfileCollectionIn(
        profile_id=profiles[2].id,
        card_id=cards[4].id
    ))
    await profile_collection_service.add_card_to_profile_collection(ProfileCollectionIn(
        profile_id=profiles[2].id,
        card_id=cards[5].id
    ))
    await profile_collection_service.add_card_to_profile_collection(ProfileCollectionIn(
        profile_id=profiles[3].id,
        card_id=cards[9].id
    ))
    await profile_collection_service.add_card_to_profile_collection(ProfileCollectionIn(
        profile_id=profiles[3].id,
        card_id=cards[10].id
    ))
    await profile_collection_service.add_card_to_profile_collection(ProfileCollectionIn(
        profile_id=profiles[3].id,
        card_id=cards[17].id
    ))
    await profile_collection_service.add_card_to_profile_collection(ProfileCollectionIn(
        profile_id=profiles[3].id,
        card_id=cards[19].id
    ))
    await profile_collection_service.add_card_to_profile_collection(ProfileCollectionIn(
        profile_id=profiles[3].id,
        card_id=cards[2].id
    ))
    await profile_collection_service.add_card_to_profile_collection(ProfileCollectionIn(
        profile_id=profiles[3].id,
        card_id=cards[3].id
    ))
    await profile_collection_service.add_card_to_profile_collection(ProfileCollectionIn(
        profile_id=profiles[3].id,
        card_id=cards[17].id
    ))
    await profile_collection_service.add_card_to_profile_collection(ProfileCollectionIn(
        profile_id=profiles[4].id,
        card_id=cards[17].id
    ))
    await profile_collection_service.add_card_to_profile_collection(ProfileCollectionIn(
        profile_id=profiles[4].id,
        card_id=cards[18].id
    ))
    await profile_collection_service.add_card_to_profile_collection(ProfileCollectionIn(
        profile_id=profiles[4].id,
        card_id=cards[19].id
    ))

    """
   Adding Trade Offers
   """

    await trade_offer_service.add_trade_offer(TradeOfferIn(
        profile_posted=profiles[2].id,
        card_offered=cards[3].id,
        card_wanted=cards[17].id
    ))

    await trade_offer_service.add_trade_offer(TradeOfferIn(
        profile_posted=profiles[2].id,
        card_offered=cards[4].id,
        card_wanted=cards[17].id
    ))

    await trade_offer_service.add_trade_offer(TradeOfferIn(
        profile_posted=profiles[2].id,
        card_offered=cards[5].id,
        card_wanted=cards[17].id
    ))

    await trade_offer_service.add_trade_offer(TradeOfferIn(
        profile_posted=profiles[2].id,
        card_offered=cards[5].id,
        card_wanted=cards[16].id
    ))

    await trade_offer_service.add_trade_offer(TradeOfferIn(
        profile_posted=profiles[2].id,
        card_offered=cards[5].id,
        card_wanted=cards[15].id
    ))

    await trade_offer_service.add_trade_offer(TradeOfferIn(
        profile_posted=profiles[3].id,
        card_offered=cards[9].id,
        card_wanted=cards[1].id
    ))

    await trade_offer_service.add_trade_offer(TradeOfferIn(
        profile_posted=profiles[3].id,
        card_offered=cards[2].id,
        card_wanted=cards[3].id
    ))

    await trade_offer_service.add_trade_offer(TradeOfferIn(
        profile_posted=profiles[4].id,
        card_offered=cards[19].id,
        card_wanted=cards[5].id
    ))

    await trade_offer_service.add_trade_offer(TradeOfferIn(
        profile_posted=profiles[4].id,
        card_offered=cards[19].id,
        card_wanted=cards[5].id
    ))
