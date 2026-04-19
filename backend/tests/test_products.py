import pytest


@pytest.mark.asyncio
async def test_get_product_detail(client):
    res = await client.get("/api/v1/products/1")
    assert res.status_code == 200
    body = res.json()
    assert body["code"] == 0
    data = body["data"]
    assert data["id"] == 1
    assert "Samsung Galaxy" in data["title"]
    assert data["price"] == 439.0
    assert data["original_price"] == 499.0
    assert data["discount_percentage"] == 12
    assert len(data["images"]) >= 1
    assert len(data["specs"]) >= 1
    assert data["seller"]["name"] == "Samsung Official Store"
    assert data["seller"]["is_official"] is True


@pytest.mark.asyncio
async def test_get_product_not_found(client):
    res = await client.get("/api/v1/products/999")
    assert res.status_code == 200
    body = res.json()
    assert body["code"] == 404
    assert body["data"] is None


@pytest.mark.asyncio
async def test_list_products(client):
    res = await client.get("/api/v1/products")
    assert res.status_code == 200
    body = res.json()
    assert body["code"] == 0
    assert len(body["data"]["items"]) >= 5
    assert body["data"]["pagination"]["total"] >= 5


@pytest.mark.asyncio
async def test_list_products_pagination(client):
    res = await client.get("/api/v1/products?page=1&page_size=2")
    assert res.status_code == 200
    body = res.json()
    assert len(body["data"]["items"]) == 2
    assert body["data"]["pagination"]["page"] == 1
    assert body["data"]["pagination"]["page_size"] == 2


@pytest.mark.asyncio
async def test_list_products_filter_category(client):
    res = await client.get("/api/v1/products?category=Electronics")
    assert res.status_code == 200
    body = res.json()
    assert body["code"] == 0
    for item in body["data"]["items"]:
        assert item["category"] == "Electronics"
