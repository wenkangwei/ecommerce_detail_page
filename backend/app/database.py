"""JSON file-based data store — replaces SQLite."""

import json
import logging
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
DATA_DIR.mkdir(exist_ok=True)

STORE: dict[str, list[dict]] = {}


def _path(name: str) -> Path:
    return DATA_DIR / f"{name}.json"


def load_store(name: str) -> list[dict]:
    """Load a collection from JSON file."""
    p = _path(name)
    if p.exists():
        with open(p, encoding="utf-8") as f:
            return json.load(f)
    return []


def save_store(name: str, data: list[dict]) -> None:
    """Persist a collection to JSON file."""
    with open(_path(name), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def init_store() -> None:
    """Load all collections into memory at startup."""
    for name in ("products", "sellers", "reviews", "payment_methods", "product_images", "product_specs", "related_products", "brand_products"):
        STORE[name] = load_store(name)
        logger.info("Loaded %d %s from JSON", len(STORE[name]), name)

    if not STORE["products"]:
        logger.info("Data store empty — run: python -m app.seed")


def get_collection(name: str) -> list[dict]:
    """Get an in-memory collection."""
    return STORE.get(name, [])


def find_by_id(collection: str, item_id: int) -> dict | None:
    """Find a single item by id."""
    for item in get_collection(collection):
        if item.get("id") == item_id:
            return item
    return None


def find_all(collection: str, **filters) -> list[dict]:
    """Find all items matching filters."""
    results = get_collection(collection)
    for key, value in filters.items():
        results = [r for r in results if r.get(key) == value]
    return results
