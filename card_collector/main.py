from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.exception_handlers import http_exception_handler

from card_collector.api.routers.card import router as card_router
from card_collector.api.routers.profile import router as profile_router
from card_collector.api.routers.profile_collection import router as profile_collection_router
from card_collector.api.routers.trade_offer import router as trade_offer_router

from card_collector.container import Container
from card_collector.db import database
from card_collector.db import init_db
from card_collector.utils import setup

container = Container()
container.wire(modules=[
    "card_collector.api.routers.card",
    "card_collector.api.routers.profile",
    "card_collector.api.routers.profile_collection",
    "card_collector.api.routers.trade_offer",
    "card_collector.utils.setup"
])


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator:
    """Lifespan function working on app startup."""
    await init_db()
    await database.connect()
    await setup.main()
    yield
    await database.disconnect()


app = FastAPI(lifespan=lifespan)
app.include_router(card_router, prefix="/card")
app.include_router(profile_router, prefix="/profile")
app.include_router(profile_collection_router, prefix="/profile_collection")
app.include_router(trade_offer_router, prefix="/trade_offer")
