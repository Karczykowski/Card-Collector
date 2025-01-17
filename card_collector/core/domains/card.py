from asyncpg import Record
from pydantic import BaseModel, ConfigDict

class CardIn(BaseModel):
    """Model representing card's attributes."""
    name: str
    rarity_id: int

class Card(CardIn):
    """Model representing card's attributes in the database."""
    id: int

    model_config = ConfigDict(from_attributes=True, extra="ignore")

    @classmethod
    def from_record(cls, record: Record) -> "Card":
        """
        A method for preparing instance based on DB record.

        Args:
            record (Record): The DB record.

        Returns:
            Card: The final Card instance.
        """
        record_dict = dict(record)

        return cls(
            id=record_dict.get("id"),
            name=record_dict.get("name"),
            rarity_id=record_dict.get("rarity_id"),
        )
