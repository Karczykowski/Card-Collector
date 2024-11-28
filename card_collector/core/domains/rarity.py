"""Module containing rarity-related domain models"""

from typing import Optional
from asyncpg import Record
from pydantic import BaseModel, ConfigDict


class RarityIn(BaseModel):
    """Model representing rarity's DTO attributes."""
    name: str


class Rarity(RarityIn):
    """Model representing rarity's attributes in the database."""
    id: int

    model_config = ConfigDict(from_attributes=True, extra="ignore")

@classmethod
def from_record(cls, record: Record) -> "Rarity":
    """A method for preparing DTO instance based on DB record.

    Args:
        record (Record): The DB record.

    Returns:
        RarityDTO: The final DTO instance.
    """
    record_dict = dict(record)

    return cls(
        id=record_dict.get("id"),  # type: ignore
        name=record_dict.get("name"),  # type: ignore
        rarity_id=record_dict("rarity_id"), # type: ignore
    )