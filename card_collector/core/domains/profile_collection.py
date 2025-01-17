from asyncpg import Record
from pydantic import BaseModel, ConfigDict

class ProfileCollectionIn(BaseModel):
    """Model representing profile collection's attributes."""
    profile_id: int
    card_id: int

class ProfileCollection(ProfileCollectionIn):
    """Model representing profile collection's attributes in the database."""
    id: int

    model_config = ConfigDict(from_attributes=True, extra="ignore")

    @classmethod
    def from_record(cls, record: Record) -> "ProfileCollection":
        """A method for preparing instance based on DB record.

        Args:
            record (Record): The DB record.

        Returns:
            ProfileCollection: The final profile collection instance.
        """
        record_dict = dict(record)

        return cls(
            id=record_dict.get("id"),
            profile_id=record_dict.get("profile_id"),
            card_id=record_dict.get("card_id"),
        )
