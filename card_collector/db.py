"""A module providing database access."""

import asyncio

import databases
import sqlalchemy
from sqlalchemy.exc import OperationalError, DatabaseError
from sqlalchemy.ext.asyncio import create_async_engine
from asyncpg.exceptions import (    # type: ignore
    CannotConnectNowError,
    ConnectionDoesNotExistError,
)

from card_collector.config import config

metadata = sqlalchemy.MetaData()

card_table = sqlalchemy.Table(
    "card",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("rarity_id", sqlalchemy.Integer),
)

profile_table = sqlalchemy.Table(
    "profile",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String),
)

profile_collection_table = sqlalchemy.Table(
    "profile_collection",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("profile_id", sqlalchemy.Integer, sqlalchemy.ForeignKey('profile.id')),
    sqlalchemy.Column("card_id", sqlalchemy.Integer, sqlalchemy.ForeignKey('card.id')),
)

trade_offer_table = sqlalchemy.Table(
    "trade_offer",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("profile_posted", sqlalchemy.Integer),
    sqlalchemy.Column("card_offered", sqlalchemy.Integer, sqlalchemy.ForeignKey('card.id')),
    sqlalchemy.Column("card_wanted", sqlalchemy.Integer, sqlalchemy.ForeignKey('card.id'))
)

quest_table = sqlalchemy.Table(
    "quest_table",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("profile_id", sqlalchemy.Integer, sqlalchemy.ForeignKey('profile.id')),
    sqlalchemy.Column("cards_collected", sqlalchemy.Integer),
    sqlalchemy.Column("cards_needed", sqlalchemy.Integer),
    sqlalchemy.Column("reward", sqlalchemy.Integer, sqlalchemy.ForeignKey('card.id'))
)

db_uri = (
    f"postgresql+asyncpg://{config.DB_USER}:{config.DB_PASSWORD}"
    f"@{config.DB_HOST}/{config.DB_NAME}"
)

engine = create_async_engine(
    db_uri,
    echo=True,
    future=True,
    pool_pre_ping=True,
)

database = databases.Database(
    db_uri,
    force_rollback=True,
)


async def init_db(retries: int = 5, delay: int = 5) -> None:
    """Function initializing the DB.

    Args:
        retries (int, optional): Number of retries of connect to DB.
            Defaults to 5.
        delay (int, optional): Delay of connect do DB. Defaults to 2.
    """
    for attempt in range(retries):
        try:
            async with engine.begin() as conn:
                await conn.run_sync(metadata.create_all)
            return
        except (
                OperationalError,
                DatabaseError,
                CannotConnectNowError,
                ConnectionDoesNotExistError,
        ) as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            await asyncio.sleep(delay)

    raise ConnectionError("Could not connect to DB after several retries.")
