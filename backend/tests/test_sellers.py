import pytest


@pytest.mark.asyncio
async def test_get_seller(client):
    res = await client.get("/api/v1/sellers/1")
    assert res.status_code == 200
    body = res.json()
    assert body["code"] == 0
    assert body["data"]["name"] == "Samsung Official Store"
    assert body["data"]["is_official"] is True


@pytest.mark.asyncio
async def test_get_seller_not_found(client):
    res = await client.get("/api/v1/sellers/999")
    assert res.status_code == 200
    body = res.json()
    assert body["code"] == 404
