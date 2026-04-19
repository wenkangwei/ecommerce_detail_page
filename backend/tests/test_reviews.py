import pytest


@pytest.mark.asyncio
async def test_get_reviews(client):
    res = await client.get("/api/v1/products/1/reviews")
    assert res.status_code == 200
    body = res.json()
    assert body["code"] == 0
    assert len(body["data"]["items"]) >= 5
    assert body["data"]["summary"]["average"] > 0
    assert body["data"]["pagination"]["total"] >= 5


@pytest.mark.asyncio
async def test_get_reviews_pagination(client):
    res = await client.get("/api/v1/products/1/reviews?page=1&page_size=3")
    assert res.status_code == 200
    body = res.json()
    assert len(body["data"]["items"]) == 3


@pytest.mark.asyncio
async def test_get_reviews_distribution(client):
    res = await client.get("/api/v1/products/1/reviews")
    assert res.status_code == 200
    dist = res.json()["data"]["summary"]["distribution"]
    assert dist["star_5"] > 0
    assert dist["star_4"] > 0
