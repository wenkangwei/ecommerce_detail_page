import pytest

from app.database import STORE
from app.seed import IMAGES, PAYMENT_METHODS, PRODUCTS, REVIEWS, SELLERS, SPECS


@pytest.fixture(autouse=True)
def setup_data():
    """Load seed data into the in-memory store before each test."""
    STORE["sellers"] = [s.copy() for s in SELLERS]
    STORE["products"] = [p.copy() for p in PRODUCTS]
    STORE["product_images"] = [i.copy() for i in IMAGES]
    STORE["product_specs"] = [s.copy() for s in SPECS]
    STORE["reviews"] = [r.copy() for r in REVIEWS]
    STORE["payment_methods"] = [m.copy() for m in PAYMENT_METHODS]
    yield


@pytest.fixture
def client():
    from httpx import ASGITransport, AsyncClient
    from app.main import app
    import asyncio

    transport = ASGITransport(app=app)
    async def _client():
        async with AsyncClient(transport=transport, base_url="http://test") as ac:
            yield ac

    # For sync test functions using pytest-httpx style
    return _client()


# Since our endpoints are async, use sync httpx with ASGI transport
from httpx import ASGITransport, AsyncClient
from app.main import app
import pytest_asyncio


@pytest_asyncio.fixture
async def client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac
