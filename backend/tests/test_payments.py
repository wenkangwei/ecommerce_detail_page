import pytest


@pytest.mark.asyncio
async def test_list_payment_methods(client):
    res = await client.get("/api/v1/payment-methods")
    assert res.status_code == 200
    body = res.json()
    assert body["code"] == 0
    assert len(body["data"]) >= 4

    types = {m["type"] for m in body["data"]}
    assert "credit_card" in types
    assert "debit_card" in types
    assert "digital_wallet" in types


@pytest.mark.asyncio
async def test_payment_method_fields(client):
    res = await client.get("/api/v1/payment-methods")
    methods = res.json()["data"]
    for m in methods:
        assert "id" in m
        assert "name" in m
        assert "type" in m
        assert "icon_url" in m
        assert "max_installments" in m
