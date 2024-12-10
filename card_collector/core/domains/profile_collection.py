"""Module containing profile_collection-related domain models"""

from typing import Optional
from asyncpg import Record
from pydantic import BaseModel, ConfigDict


class ProfileCollectionIn(BaseModel):
    """Model representing profile_collection's DTO attributes."""
    profile_id: int
    card_id: int


class ProfileCollection(ProfileCollectionIn):
    """Model representing profile_collection's attributes in the database."""
    id: int

    model_config = ConfigDict(from_attributes=True, extra="ignore")

    @classmethod
    def from_record(cls, record: Record) -> "ProfileCollection":
        """A method for preparing DTO instance based on DB record.

        Args:
            record (Record): The DB record.

        Returns:
            Profile_collectionDTO: The final DTO instance.
        """
        record_dict = dict(record)

        return cls(
            id=record_dict.get("id"),  # type: ignore
            profile_id=record_dict.get("profile_id"),  # type: ignore
            card_id=record_dict.get("card_id"), # type: ignore
        )