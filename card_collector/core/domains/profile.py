"""Module containing profile-related domain models"""

from typing import Optional
from asyncpg import Record
from pydantic import BaseModel, ConfigDict


class ProfileIn(BaseModel):
    """Model representing profile's DTO attributes."""
    name: str


class Profile(ProfileIn):
    """Model representing profile's attributes in the database."""
    id: int

    model_config = ConfigDict(from_attributes=True, extra="ignore")

    @classmethod
    def from_record(cls, record: Record) -> "Profile":
        """A method for preparing DTO instance based on DB record.

        Args:
            record (Record): The DB record.

        Returns:
            ProfileDTO: The final DTO instance.
        """
        record_dict = dict(record)

        return cls(
            id=record_dict.get("id"),  # type: ignore
            name=record_dict.get("name"),  # type: ignore
        )