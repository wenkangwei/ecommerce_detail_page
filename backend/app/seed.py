"""Seed the JSON data store with demo data."""

import json
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
DATA_DIR.mkdir(exist_ok=True)


def _write(name: str, data: list[dict]) -> None:
    path = DATA_DIR / f"{name}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    logger.info("Wrote %d items to %s", len(data), path.name)


# ── Sellers ───────────────────────────────────────────────────

SELLERS = [
    {"id": 1, "name": "Samsung Official Store", "is_official": True, "reputation": "MercadoLíder Platinum", "location": "Montevideo, Uruguay", "logo_url": "/static/images/sellers/samsung.png", "created_at": "2026-01-01T00:00:00"},
    {"id": 2, "name": "TechWorld", "is_official": False, "reputation": "MercadoLíder Gold", "location": "Buenos Aires, Argentina", "logo_url": "/static/images/sellers/techworld.png", "created_at": "2026-01-15T00:00:00"},
    {"id": 3, "name": "Global Electronics", "is_official": True, "reputation": "MercadoLíder Platinum", "location": "Santiago, Chile", "logo_url": "/static/images/sellers/global.png", "created_at": "2026-02-01T00:00:00"},
]

# ── Products ──────────────────────────────────────────────────

PRODUCTS = [
    {"id": 1, "title": "Samsung Galaxy A55 5G Dual SIM 256GB Dark Blue 8GB RAM", "description": "Experience the power of 5G with the Samsung Galaxy A55. Featuring a stunning 6.6-inch Super AMOLED display, 8GB RAM, and 256GB storage. Capture every moment with the 50MP main camera and 32MP front camera. With 5G connectivity, NFC support, and an all-day battery, this phone keeps up with your lifestyle. The elegant dark blue finish and Gorilla Glass Victus+ ensure both style and durability.", "price": 439.00, "original_price": 499.00, "currency": "US$", "category": "Electronics", "subcategory": "Smartphones", "stock": 15, "rating_avg": 4.8, "rating_count": 950, "free_shipping": True, "warranty_months": 12, "seller_id": 1},
    {"id": 2, "title": "Apple iPhone 15 128GB Black", "description": "The iPhone 15 features a 6.1-inch Super Retina XDR display, A16 Bionic chip, and an advanced dual-camera system with 48MP main camera. Dynamic Island keeps you connected with live activities. USB-C connectivity, Ceramic Shield front, and up to 20 hours of video playback.", "price": 799.00, "original_price": 899.00, "currency": "US$", "category": "Electronics", "subcategory": "Smartphones", "stock": 8, "rating_avg": 4.9, "rating_count": 1200, "free_shipping": True, "warranty_months": 12, "seller_id": 2},
    {"id": 3, "title": "Samsung Galaxy Tab S9 128GB WiFi Graphite", "description": "Unleash creativity with the Galaxy Tab S9. Featuring an 11-inch Dynamic AMOLED 2X display, Snapdragon 8 Gen 2 processor, and included S Pen. IP68 water resistant, 128GB storage expandable up to 1TB. Perfect for work, play, and everything in between.", "price": 549.00, "original_price": 699.00, "currency": "US$", "category": "Electronics", "subcategory": "Tablets", "stock": 12, "rating_avg": 4.7, "rating_count": 340, "free_shipping": True, "warranty_months": 12, "seller_id": 1},
    {"id": 4, "title": "Sony WH-1000XM5 Wireless Noise Cancelling Headphones Black", "description": "Industry-leading noise cancellation with Auto NC Optimizer. 30-hour battery life, multipoint connection, and speak-to-chat. Crystal clear hands-free calling with 4 beamforming microphones. Ultra-comfortable lightweight design at just 250g.", "price": 299.00, "original_price": 399.00, "currency": "US$", "category": "Electronics", "subcategory": "Audio", "stock": 25, "rating_avg": 4.6, "rating_count": 580, "free_shipping": True, "warranty_months": 12, "seller_id": 3},
    {"id": 5, "title": "MacBook Air M3 13-inch 256GB Midnight", "description": "Supercharged by M3. The remarkably thin MacBook Air packs a powerful punch with the M3 chip, up to 18 hours of battery life, and a stunning 13.6-inch Liquid Retina display. 8GB unified memory, 256GB SSD, MagSafe charging, and two Thunderbolt ports. Weighing just 2.7 pounds — it's the ultimate everyday laptop.", "price": 999.00, "original_price": 1099.00, "currency": "US$", "category": "Electronics", "subcategory": "Laptops", "stock": 6, "rating_avg": 4.9, "rating_count": 720, "free_shipping": True, "warranty_months": 12, "seller_id": 2},
    {"id": 6, "title": "Logitech MX Master 3S Wireless Mouse Graphite", "description": "The MX Master 3S is an advanced wireless mouse with 8000 DPI tracking, quiet click technology, and MagSpeed electromagnetic scrolling. Works on virtually any surface including glass. USB-C quick charging: 1 minute = 3 hours of use. Full charge lasts 70 days.", "price": 79.00, "original_price": 99.00, "currency": "US$", "category": "Electronics", "subcategory": "Accessories", "stock": 40, "rating_avg": 4.7, "rating_count": 450, "free_shipping": False, "warranty_months": 24, "seller_id": 3},
]

# ── Product Images ────────────────────────────────────────────

IMAGES = [
    {"id": 1, "product_id": 1, "url": "https://placehold.co/480x480/F5F5F5/333?text=A55+Front", "alt_text": "Galaxy A55 Front", "sort_order": 0},
    {"id": 2, "product_id": 1, "url": "https://placehold.co/480x480/E8EAF6/333?text=A55+Back", "alt_text": "Galaxy A55 Back", "sort_order": 1},
    {"id": 3, "product_id": 1, "url": "https://placehold.co/480x480/E3F2FD/333?text=A55+Side", "alt_text": "Galaxy A55 Side", "sort_order": 2},
    {"id": 4, "product_id": 1, "url": "https://placehold.co/480x480/FFF3E0/333?text=A55+Camera", "alt_text": "Galaxy A55 Camera", "sort_order": 3},
    {"id": 5, "product_id": 2, "url": "https://placehold.co/480x480/F5F5F5/333?text=iPhone+15", "alt_text": "iPhone 15 Front", "sort_order": 0},
    {"id": 6, "product_id": 2, "url": "https://placehold.co/480x480/E0E0E0/333?text=iPhone+Back", "alt_text": "iPhone 15 Back", "sort_order": 1},
    {"id": 7, "product_id": 2, "url": "https://placehold.co/480x480/BDBDBD/333?text=iPhone+Side", "alt_text": "iPhone 15 Side", "sort_order": 2},
    {"id": 8, "product_id": 3, "url": "https://placehold.co/480x480/F5F5F5/333?text=Tab+S9", "alt_text": "Galaxy Tab S9 Front", "sort_order": 0},
    {"id": 9, "product_id": 3, "url": "https://placehold.co/480x480/E8EAF6/333?text=Tab+S9+Back", "alt_text": "Galaxy Tab S9 Back", "sort_order": 1},
    {"id": 10, "product_id": 4, "url": "https://placehold.co/480x480/F5F5F5/333?text=XM5+Front", "alt_text": "WH-1000XM5 Front", "sort_order": 0},
    {"id": 11, "product_id": 4, "url": "https://placehold.co/480x480/E0E0E0/333?text=XM5+Side", "alt_text": "WH-1000XM5 Side", "sort_order": 1},
    {"id": 12, "product_id": 4, "url": "https://placehold.co/480x480/E8EAF6/333?text=XM5+Case", "alt_text": "WH-1000XM5 Case", "sort_order": 2},
    {"id": 13, "product_id": 5, "url": "https://placehold.co/480x480/F5F5F5/333?text=MacBook+Air", "alt_text": "MacBook Air Open", "sort_order": 0},
    {"id": 14, "product_id": 5, "url": "https://placehold.co/480x480/E0E0E0/333?text=MacBook+Closed", "alt_text": "MacBook Air Closed", "sort_order": 1},
    {"id": 15, "product_id": 5, "url": "https://placehold.co/480x480/E8EAF6/333?text=MacBook+Angle", "alt_text": "MacBook Air Angle", "sort_order": 2},
    {"id": 16, "product_id": 6, "url": "https://placehold.co/480x480/F5F5F5/333?text=MX+Master", "alt_text": "MX Master 3S Top", "sort_order": 0},
    {"id": 17, "product_id": 6, "url": "https://placehold.co/480x480/E0E0E0/333?text=MX+Side", "alt_text": "MX Master 3S Side", "sort_order": 1},
]

# ── Product Specs ─────────────────────────────────────────────

SPECS = [
    {"id": 1, "product_id": 1, "spec_key": "Screen Size", "spec_value": "6.6 inches", "sort_order": 0},
    {"id": 2, "product_id": 1, "spec_key": "RAM", "spec_value": "8 GB", "sort_order": 1},
    {"id": 3, "product_id": 1, "spec_key": "Storage", "spec_value": "256 GB", "sort_order": 2},
    {"id": 4, "product_id": 1, "spec_key": "Rear Camera", "spec_value": "50 MP", "sort_order": 3},
    {"id": 5, "product_id": 1, "spec_key": "Front Camera", "spec_value": "32 MP", "sort_order": 4},
    {"id": 6, "product_id": 1, "spec_key": "Connectivity", "spec_value": "5G, NFC, WiFi 6", "sort_order": 5},
    {"id": 7, "product_id": 1, "spec_key": "Battery", "spec_value": "5000 mAh", "sort_order": 6},
    {"id": 8, "product_id": 1, "spec_key": "Operating System", "spec_value": "Android 14", "sort_order": 7},
    {"id": 9, "product_id": 2, "spec_key": "Screen Size", "spec_value": "6.1 inches", "sort_order": 0},
    {"id": 10, "product_id": 2, "spec_key": "Storage", "spec_value": "128 GB", "sort_order": 1},
    {"id": 11, "product_id": 2, "spec_key": "Main Camera", "spec_value": "48 MP", "sort_order": 2},
    {"id": 13, "product_id": 2, "spec_key": "Connectivity", "spec_value": "5G, NFC, USB-C", "sort_order": 3},
    {"id": 14, "product_id": 2, "spec_key": "Chip", "spec_value": "A16 Bionic", "sort_order": 4},
    {"id": 15, "product_id": 3, "spec_key": "Screen Size", "spec_value": "11 inches", "sort_order": 0},
    {"id": 16, "product_id": 3, "spec_key": "Storage", "spec_value": "128 GB", "sort_order": 1},
    {"id": 17, "product_id": 3, "spec_key": "Processor", "spec_value": "Snapdragon 8 Gen 2", "sort_order": 2},
    {"id": 18, "product_id": 3, "spec_key": "Stylus", "spec_value": "S Pen included", "sort_order": 3},
    {"id": 19, "product_id": 4, "spec_key": "Type", "spec_value": "Over-ear Wireless", "sort_order": 0},
    {"id": 20, "product_id": 4, "spec_key": "Battery Life", "spec_value": "30 hours", "sort_order": 1},
    {"id": 21, "product_id": 4, "spec_key": "Noise Cancellation", "spec_value": "Yes (Auto NC)", "sort_order": 2},
    {"id": 22, "product_id": 4, "spec_key": "Weight", "spec_value": "250g", "sort_order": 3},
    {"id": 23, "product_id": 5, "spec_key": "Screen Size", "spec_value": "13.6 inches", "sort_order": 0},
    {"id": 24, "product_id": 5, "spec_key": "Chip", "spec_value": "Apple M3", "sort_order": 1},
    {"id": 25, "product_id": 5, "spec_key": "Memory", "spec_value": "8 GB", "sort_order": 2},
    {"id": 26, "product_id": 5, "spec_key": "Storage", "spec_value": "256 GB SSD", "sort_order": 3},
    {"id": 27, "product_id": 5, "spec_key": "Battery", "spec_value": "Up to 18 hours", "sort_order": 4},
    {"id": 28, "product_id": 6, "spec_key": "DPI", "spec_value": "8000", "sort_order": 0},
    {"id": 29, "product_id": 6, "spec_key": "Battery Life", "spec_value": "70 days", "sort_order": 1},
    {"id": 30, "product_id": 6, "spec_key": "Connectivity", "spec_value": "Bluetooth + USB", "sort_order": 2},
    {"id": 31, "product_id": 6, "spec_key": "Weight", "spec_value": "141g", "sort_order": 3},
]

# ── Reviews ───────────────────────────────────────────────────

REVIEWS_RAW = {
    1: [("Juan P.", 5, "Excellent phone!", "Great value for money. The camera is amazing and battery lasts all day. Highly recommend."), ("Maria L.", 5, "Love it!", "Beautiful design, fast performance, and the 5G is blazing fast. Best phone I've owned."), ("Carlos R.", 4, "Very good phone", "Almost perfect. Great screen, good cameras. Only minor issue is it's slightly heavy."), ("Ana S.", 5, "Perfect gift", "Bought this for my daughter and she absolutely loves it. The color is gorgeous."), ("Pedro M.", 5, "Samsung quality", "Another great Samsung phone. Smooth experience, no lag, great display."), ("Lucia G.", 4, "Great mid-range", "Excellent for the price point. Does everything I need and more."), ("Roberto F.", 5, "Impressive camera", "The 50MP camera takes stunning photos even in low light. Very impressed."), ("Elena V.", 4, "Good but big", "Great phone overall, but it's quite large. Hard to use one-handed."), ("Diego H.", 5, "Best in class", "Tried many phones in this price range. This is by far the best. Super smooth."), ("Sofia K.", 5, "Battery beast", "The 5000mAh battery is incredible. Two days of normal use easily.")],
    2: [("Miguel A.", 5, "Best iPhone yet", "The camera improvements are noticeable. Dynamic Island is actually useful."), ("Laura B.", 5, "Smooth and fast", "iOS runs perfectly. USB-C is finally here and it's great."), ("Fernando C.", 5, "Worth the upgrade", "Coming from iPhone 13, the improvements are significant. Great purchase."), ("Isabella D.", 4, "Great but expensive", "Amazing phone but the price is steep. Still, you get what you pay for."), ("Andres E.", 5, "Premium experience", "Every detail is polished. The build quality is unmatched."), ("Carmen F.", 5, "Camera is insane", "48MP photos look professional. Night mode is incredible.")],
    3: [("Gabriel G.", 5, "Perfect tablet", "S Pen is responsive, screen is gorgeous. Great for drawing and note-taking."), ("Valentina H.", 4, "Almost perfect", "Great tablet for the price. Wish it had more RAM for multitasking."), ("Ricardo I.", 5, "iPad alternative", "Just as good as iPad Pro for half the price. Android tablet apps are improving.")],
    4: [("Patricia J.", 5, "Best NC headphones", "Noise cancellation is unreal. Can't hear anything on the subway."), ("Alejandro K.", 5, "Worth every penny", "Sound quality is superb. Battery lasts forever. Super comfortable."), ("Natalia L.", 4, "Great for travel", "Used these on a 12-hour flight. Battery didn't die. Very comfortable."), ("Sebastian M.", 5, "Sony delivers again", "XM4 was great, XM5 is better in every way. The design is much improved.")],
    5: [("Daniela N.", 5, "Perfect laptop", "M3 chip is incredibly fast. Battery lasts all day. Best laptop I've ever used."), ("Javier O.", 5, "Light and powerful", "Can't believe this much power fits in such a thin device. No fan noise at all."), ("Camila P.", 5, "Worth the switch", "Switched from Windows. macOS is smooth, the hardware is beautiful."), ("Tomas Q.", 4, "Great but pricey", "Amazing laptop but expensive for 256GB. Would love more base storage."), ("Veronica R.", 5, "Creative powerhouse", "Runs Photoshop, Final Cut, and Xcode simultaneously without breaking a sweat.")],
    6: [("Martin S.", 5, "Best mouse ever", "The scroll wheel is magical. Infinite scroll is a game changer for long documents."), ("Adriana T.", 5, "Ergonomic perfection", "No wrist pain after long coding sessions. The shape is perfect."), ("Felipe U.", 4, "Great for productivity", "Customizable buttons save me tons of time. Only wish it was cheaper.")],
}

REVIEWS = []
review_id = 1
for product_id, reviews_list in REVIEWS_RAW.items():
    for user_name, rating, title, content in reviews_list:
        REVIEWS.append({"id": review_id, "product_id": product_id, "user_name": user_name, "rating": rating, "title": title, "content": content, "created_at": "2026-03-15T10:00:00"})
        review_id += 1

# ── Payment Methods ───────────────────────────────────────────

PAYMENT_METHODS = [
    {"id": 1, "name": "VISA", "type": "credit_card", "icon_url": "/static/images/payments/visa.svg", "max_installments": 12, "sort_order": 0},
    {"id": 2, "name": "Mastercard", "type": "credit_card", "icon_url": "/static/images/payments/mastercard.svg", "max_installments": 12, "sort_order": 1},
    {"id": 3, "name": "OCA", "type": "credit_card", "icon_url": "/static/images/payments/oca.svg", "max_installments": 6, "sort_order": 2},
    {"id": 4, "name": "VISA Debit", "type": "debit_card", "icon_url": "/static/images/payments/visa-debit.svg", "max_installments": 1, "sort_order": 3},
    {"id": 5, "name": "Mastercard Debit", "type": "debit_card", "icon_url": "/static/images/payments/mastercard-debit.svg", "max_installments": 1, "sort_order": 4},
    {"id": 6, "name": "Mercado Pago", "type": "digital_wallet", "icon_url": "/static/images/payments/mercadopago.svg", "max_installments": 12, "sort_order": 5},
]


def seed():
    _write("sellers", SELLERS)
    _write("products", PRODUCTS)
    _write("product_images", IMAGES)
    _write("product_specs", SPECS)
    _write("reviews", REVIEWS)
    _write("payment_methods", PAYMENT_METHODS)
    logger.info("Seed complete: %d sellers, %d products, %d images, %d specs, %d reviews, %d payment methods",
                len(SELLERS), len(PRODUCTS), len(IMAGES), len(SPECS), len(REVIEWS), len(PAYMENT_METHODS))


if __name__ == "__main__":
    seed()
