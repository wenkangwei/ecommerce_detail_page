import asyncio
from typing import AsyncGenerator

import pytest
import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.database import Base, get_db
from app.main import app
from app.models import PaymentMethod, Product, ProductImage, ProductSpec, Review, Seller
from app.seed import IMAGES, PAYMENT_METHODS, PRODUCTS, REVIEWS, SELLERS, SPECS

TEST_DATABASE_URL = "sqlite+aiosqlite://"

test_engine = create_async_engine(TEST_DATABASE_URL, echo=False)
test_session_factory = async_sessionmaker(test_engine, class_=AsyncSession, expire_on_commit=False)


async def override_get_db() -> AsyncGenerator[AsyncSession, None]:
    async with test_session_factory() as session:
        yield session


app.dependency_overrides[get_db] = override_get_db


@pytest_asyncio.fixture(scope="session")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(autouse=True)
async def setup_database():
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with test_session_factory() as session:
        for seller in SELLERS:
            session.add(Seller(**{c.name: getattr(seller, c.name) for c in seller.__table__.columns if c.name != "created_at"}))
        for product in PRODUCTS:
            session.add(Product(**{c.name: getattr(product, c.name) for c in product.__table__.columns if c.name not in ("created_at", "updated_at")}))
        for image in IMAGES:
            session.add(ProductImage(**{c.name: getattr(image, c.name) for c in image.__table__.columns}))
        for spec in SPECS:
            session.add(ProductSpec(**{c.name: getattr(spec, c.name) for c in spec.__table__.columns}))
        for review in REVIEWS:
            session.add(Review(**{c.name: getattr(review, c.name) for c in review.__table__.columns if c.name != "created_at"}))
        for method in PAYMENT_METHODS:
            session.add(PaymentMethod(**{c.name: getattr(method, c.name) for c in method.__table__.columns}))
        await session.commit()

    yield

    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest_asyncio.fixture
async def client() -> AsyncGenerator[AsyncClient, None]:
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac
