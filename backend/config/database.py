from contextlib import asynccontextmanager
from logging import Logger
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from backend.config.settings import settings
from backend.utils import setup_logger

logger: Logger = setup_logger(__name__)


@asynccontextmanager
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as db:
        logger.info("Database session created")
        try:
            yield db
        except Exception as e:
            logger.error("Error occurred when handling the database session: %s", e)
            raise
        finally:
            logger.info("Database session closed")


DATABASE_URL: str = (
    f"postgresql+asyncpg://{settings.DB_USER}:"
    f"{settings.DB_PASSWORD}"
    f"@{settings.DB_HOST}:"
    f"{settings.DB_PORT}/"
    f"{settings.DB_NAME}"
)

# Use the async version of SQLAlchemy engine.
engine = create_async_engine(DATABASE_URL, echo=True)

# Use async session maker
SessionLocal = async_sessionmaker(bind=engine, autoflush=False, class_=AsyncSession)
