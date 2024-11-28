from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.exception_handlers import http_exception_handler

from card_collector.api.routers.card import router as card_router
from card_collector.api.routers.rarity import router as rarity_router

from card_collector.container import Container
from card_collector.db import database
from card_collector.db import init_db

container = Container()
container.wire(modules=[
    "card_collector.api.routers.card",
    "card_collector.api.routers.rarity",
])


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator:
    """Lifespan function working on app startup."""
    await init_db()
    await database.connect()
    yield
    await database.disconnect()


app = FastAPI(lifespan=lifespan)
app.include_router(card_router, prefix="/card")
app.include_router(rarity_router, prefix="/rarity")