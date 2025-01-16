"""Module containing card-related domain models"""

from typing import Optional
from asyncpg import Record
from pydantic import BaseModel, ConfigDict


class QuestIn(BaseModel):
    """Model representing quest's DTO attributes."""
    profile_id: int
    cards_collected: int
    cards_needed: int
    rarity_needed: int
    reward: int


class Quest(QuestIn):
    """Model representing card's attributes in the database."""
    id: int

    model_config = ConfigDict(from_attributes=True, extra="ignore")

    @classmethod
    def from_record(cls, record: Record) -> "Quest":
        """A method for preparing DTO instance based on DB quest.

        Args:
            record (Record): The DB quest.

        Returns:
            QuestDTO: The final DTO instance.
        """
        record_dict = dict(record)

        return cls(
            id=record_dict.get("id"),  # type: ignore
            profile_id=record_dict.get("profile_id"),  # type: ignore
            cards_collected=record_dict.get("cards_collected"), # type: ignore
            cards_needed=record_dict.get("cards_needed"), # type: ignore
            rarity_needed=record_dict.get("rarity_needed"), # type: ignore
            reward=record_dict.get("reward"), # type: ignore
        )
