"""Module containing card-related domain models"""

from typing import Optional
from asyncpg import Record
from pydantic import BaseModel, ConfigDict


class QuestIn(BaseModel):
    """Model representing card's DTO attributes."""
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
    def from_quest(cls, quest: Record) -> "Quest":
        """A method for preparing DTO instance based on DB quest.

        Args:
            quest (Record): The DB quest.

        Returns:
            QuestDTO: The final DTO instance.
        """
        quest_dict = dict(quest)

        return cls(
            id=quest_dict.get("id"),  # type: ignore
            name=quest_dict.get("name"),  # type: ignore
            rarity_id=quest_dict.get("rarity_id"), # type: ignore
        )
