from asyncpg import Record
from pydantic import BaseModel, ConfigDict

class QuestIn(BaseModel):
    """Model representing quest's attributes."""
    profile_id: int
    cards_collected: int
    cards_needed: int
    reward: int

class Quest(QuestIn):
    """Model representing card's attributes in the database."""
    id: int

    model_config = ConfigDict(from_attributes=True, extra="ignore")

    @classmethod
    def from_record(cls, record: Record) -> "Quest":
        """A method for preparing instance based on DB quest.

        Args:
            record (Record): The DB quest.

        Returns:
            Quest: The final quest instance.
        """
        record_dict = dict(record)

        return cls(
            id=record_dict.get("id"),
            profile_id=record_dict.get("profile_id"),
            cards_collected=record_dict.get("cards_collected"),
            cards_needed=record_dict.get("cards_needed"),
            reward=record_dict.get("reward"),
        )
