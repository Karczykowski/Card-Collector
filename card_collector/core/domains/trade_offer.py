"""Module containing trade_offer-related domain models"""

from typing import Optional
from asyncpg import Record
from pydantic import BaseModel, ConfigDict


class TradeOfferIn(BaseModel):
    """Model representing trade_offer's DTO attributes."""
    profile_posted: int
    card_offered: int
    card_wanted: int


class TradeOffer(TradeOfferIn):
    """Model representing trade_offer's attributes in the database."""
    id: int

    model_config = ConfigDict(from_attributes=True, extra="ignore")

    @classmethod
    def from_record(cls, record: Record) -> "TradeOffer":
        """A method for preparing DTO instance based on DB record.

        Args:
            record (Record): The DB record.

        Returns:
            TradeOfferDTO: The final DTO instance.
        """
        record_dict = dict(record)

        return cls(
            id=record_dict.get("id"),  # type: ignore
            profile_posted=record_dict.get("profile_posted"),  # type: ignore
            card_offered=record_dict.get("card_offered"),  # type: ignore
            card_wanted=record_dict.get("card_wanted"), # type: ignore
        )
