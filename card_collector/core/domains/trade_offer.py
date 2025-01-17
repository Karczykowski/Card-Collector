from asyncpg import Record
from pydantic import BaseModel, ConfigDict

class TradeOfferIn(BaseModel):
    """Model representing trade_offer's attributes."""
    profile_posted: int
    card_offered: int
    card_wanted: int

class TradeOffer(TradeOfferIn):
    """Model representing trade_offer's attributes in the database."""
    id: int

    model_config = ConfigDict(from_attributes=True, extra="ignore")

    @classmethod
    def from_record(cls, record: Record) -> "TradeOffer":
        """A method for preparing instance based on DB record.

        Args:
            record (Record): The DB record.

        Returns:
            TradeOffer: The final trade offer instance.
        """
        record_dict = dict(record)

        return cls(
            id=record_dict.get("id"),
            profile_posted=record_dict.get("profile_posted"),
            card_offered=record_dict.get("card_offered"),
            card_wanted=record_dict.get("card_wanted"),
        )
