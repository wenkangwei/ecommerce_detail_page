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
    {"id": 1, "name": "Samsung", "is_official": True, "reputation": "MercadoLíder Platinum", "location": "Capital Federal", "logo_url": "/samsung-logo.png", "sales_count": "+5mil ventas", "created_at": "2024-01-01T00:00:00"},
    {"id": 2, "name": "TechWorld", "is_official": False, "reputation": "MercadoLíder Gold", "location": "Buenos Aires, Argentina", "logo_url": "/techworld.png", "sales_count": "+2mil ventas", "created_at": "2024-01-15T00:00:00"},
    {"id": 3, "name": "Global Electronics", "is_official": True, "reputation": "MercadoLíder Platinum", "location": "Santiago, Chile", "logo_url": "/global.png", "sales_count": "+3mil ventas", "created_at": "2024-02-01T00:00:00"},
]

# ── Products ──────────────────────────────────────────────────

PRODUCTS = [
    {
        "id": 1,
        "title": "Samsung Galaxy A55 5G Dual SIM 256 GB azul oscuro 8 GB RAM",
        "description": "Capacidad y eficiencia\nCon su potente procesador y 8 GB de RAM, su computadora logrará un alto rendimiento con una alta velocidad de transmisión de contenido y ejecutará varias aplicaciones al mismo tiempo, sin demoras.\n\nCapacidad de almacenamiento ilimitada\nOlvídate de borrar. Con su memoria interna de 256 GB puedes descargar todos los archivos y aplicaciones que necesites, guardar fotos y almacenar tus películas, series y videos favoritos para reproducirlos cuando quieras.",
        "price": 439.00,
        "original_price": 499.00,
        "currency": "US$",
        "discount_percentage": 12,
        "category": "Celulares y Smartphones",
        "subcategory": "Samsung",
        "stock": 50,
        "rating_avg": 4.8,
        "rating_count": 769,
        "free_shipping": True,
        "warranty_months": 12,
        "seller_id": 1,
        "color": "Azul oscuro",
        "sold_count": 500,
        "installments": {"count": 10, "amount": 191.40, "interest_free": True},
        "category_path": [
            {"id": 1, "name": "Volver al listado", "slug": "listado"},
            {"id": 2, "name": "Celulares y Telefonía", "slug": "celulares-telefonia"},
            {"id": 3, "name": "Celulares y Smartphones", "slug": "celulares-smartphones"},
            {"id": 4, "name": "Samsung", "slug": "samsung"},
        ],
        "created_at": "2024-01-15T10:00:00",
        "updated_at": "2025-01-15T10:00:00",
    },
    {
        "id": 2,
        "title": "Apple iPhone 15 128GB Negro",
        "description": "Pantalla Super Retina XDR\nDescubre una pantalla de 6.1 pulgadas con tecnología Super Retina XDR, con brillo de hasta 2000 nits al aire libre. Dynamic Island te mantiene conectado con actividades en tiempo real.\n\nChip A16 Bionic\nEl chip A16 Bionic ofrece un rendimiento increíble. Sistema de cámara avanzado con la nueva resolución de 48MP para fotos con un nivel de detalle excepcional.",
        "price": 799.00,
        "original_price": 899.00,
        "currency": "US$",
        "discount_percentage": 11,
        "category": "Celulares y Smartphones",
        "subcategory": "Apple",
        "stock": 8,
        "rating_avg": 4.9,
        "rating_count": 1200,
        "free_shipping": True,
        "warranty_months": 12,
        "seller_id": 2,
        "color": "Negro",
        "sold_count": 350,
        "installments": {"count": 10, "amount": 348.20, "interest_free": True},
        "category_path": [
            {"id": 1, "name": "Volver al listado", "slug": "listado"},
            {"id": 2, "name": "Celulares y Telefonía", "slug": "celulares-telefonia"},
            {"id": 3, "name": "Celulares y Smartphones", "slug": "celulares-smartphones"},
            {"id": 5, "name": "Apple", "slug": "apple"},
        ],
        "created_at": "2024-03-01T10:00:00",
        "updated_at": "2025-01-15T10:00:00",
    },
    {
        "id": 3,
        "title": "Samsung Galaxy Tab S9 128GB WiFi Grafito",
        "description": "Creatividad sin límites\nLa Galaxy Tab S9 cuenta con una pantalla Dynamic AMOLED 2X de 11 pulgadas, procesador Snapdragon 8 Gen 2 y S Pen incluido. Resistente al agua IP68, almacenamiento de 128GB expandible hasta 1TB.\n\nPerfecta para trabajo y entretenimiento\nCon DeX Mode transforma tu tablet en una experiencia de escritorio completa. Ideal para productividad, dibujo y multimedia.",
        "price": 549.00,
        "original_price": 699.00,
        "currency": "US$",
        "discount_percentage": 21,
        "category": "Tablets",
        "subcategory": "Samsung",
        "stock": 12,
        "rating_avg": 4.7,
        "rating_count": 340,
        "free_shipping": True,
        "warranty_months": 12,
        "seller_id": 1,
        "color": "Grafito",
        "sold_count": 180,
        "installments": {"count": 10, "amount": 239.00, "interest_free": True},
        "category_path": [
            {"id": 1, "name": "Volver al listado", "slug": "listado"},
            {"id": 6, "name": "Computación", "slug": "computacion"},
            {"id": 7, "name": "Tablets", "slug": "tablets"},
            {"id": 4, "name": "Samsung", "slug": "samsung"},
        ],
        "created_at": "2024-02-01T10:00:00",
        "updated_at": "2025-01-15T10:00:00",
    },
    {
        "id": 4,
        "title": "Sony WH-1000XM5 Auriculares Inalámbricos con Cancelación de Ruido Negro",
        "description": "Cancelación de ruido líder en la industria\nCon Auto NC Optimizer que ajusta la cancelación de ruido automáticamente según tu entorno. 30 horas de batería, conexión multipunto y función speak-to-chat.\n\nCalidad de sonido excepcional\nLlamadas manos libres nítidas con 4 micrófonos beamforming. Diseño ultraligero y cómodo de solo 250g.",
        "price": 299.00,
        "original_price": 399.00,
        "currency": "US$",
        "discount_percentage": 25,
        "category": "Electrónica",
        "subcategory": "Audio",
        "stock": 25,
        "rating_avg": 4.6,
        "rating_count": 580,
        "free_shipping": True,
        "warranty_months": 12,
        "seller_id": 3,
        "color": "Negro",
        "sold_count": 420,
        "installments": {"count": 10, "amount": 130.20, "interest_free": True},
        "category_path": [
            {"id": 1, "name": "Volver al listado", "slug": "listado"},
            {"id": 8, "name": "Electrónica", "slug": "electronica"},
            {"id": 9, "name": "Audio", "slug": "audio"},
        ],
        "created_at": "2024-04-01T10:00:00",
        "updated_at": "2025-01-15T10:00:00",
    },
    {
        "id": 5,
        "title": "MacBook Air M3 13 pulgadas 256GB Medianoche",
        "description": "Superpotenciado por M3\nLa MacBook Air increíblemente delgada ofrece un rendimiento potente con el chip M3, hasta 18 horas de batería y una impresionante pantalla Liquid Retina de 13.6 pulgadas.\n\nDiseño premium\n8GB de memoria unificada, 256GB SSD, carga MagSafe y dos puertos Thunderbolt. Con solo 1.24 kg, es la laptop perfecta para el día a día.",
        "price": 999.00,
        "original_price": 1099.00,
        "currency": "US$",
        "discount_percentage": 9,
        "category": "Computación",
        "subcategory": "Laptops",
        "stock": 6,
        "rating_avg": 4.9,
        "rating_count": 720,
        "free_shipping": True,
        "warranty_months": 12,
        "seller_id": 2,
        "color": "Medianoche",
        "sold_count": 280,
        "installments": {"count": 10, "amount": 435.20, "interest_free": True},
        "category_path": [
            {"id": 1, "name": "Volver al listado", "slug": "listado"},
            {"id": 6, "name": "Computación", "slug": "computacion"},
            {"id": 10, "name": "Laptops", "slug": "laptops"},
            {"id": 5, "name": "Apple", "slug": "apple"},
        ],
        "created_at": "2024-05-01T10:00:00",
        "updated_at": "2025-01-15T10:00:00",
    },
    {
        "id": 6,
        "title": "Logitech MX Master 3S Mouse Inalámbrico Grafito",
        "description": "Rendimiento avanzado\nEl MX Master 3S es un mouse inalámbrico avanzado con seguimiento de 8000 DPI, tecnología de clic silencioso y desplazamiento electromagnético MagSpeed. Funciona en casi cualquier superficie, incluido el vidrio.\n\nBatería de larga duración\nCarga rápida USB-C: 1 minuto = 3 horas de uso. Carga completa dura 70 días.",
        "price": 79.00,
        "original_price": 99.00,
        "currency": "US$",
        "discount_percentage": 20,
        "category": "Computación",
        "subcategory": "Accesorios",
        "stock": 40,
        "rating_avg": 4.7,
        "rating_count": 450,
        "free_shipping": False,
        "warranty_months": 24,
        "seller_id": 3,
        "color": "Grafito",
        "sold_count": 650,
        "installments": {"count": 3, "amount": 34.40, "interest_free": True},
        "category_path": [
            {"id": 1, "name": "Volver al listado", "slug": "listado"},
            {"id": 6, "name": "Computación", "slug": "computacion"},
            {"id": 11, "name": "Accesorios", "slug": "accesorios"},
        ],
        "created_at": "2024-06-01T10:00:00",
        "updated_at": "2025-01-15T10:00:00",
    },
]

# ── Product Images (Local static files) ───────────────────────

IMAGES = [
    # Samsung Galaxy A55
    {"id": 1, "product_id": 1, "url": "/static/images/products/samsung-a55/front.jpg", "alt_text": "Samsung Galaxy A55 frontal", "sort_order": 0},
    {"id": 2, "product_id": 1, "url": "/static/images/products/samsung-a55/back.jpg", "alt_text": "Samsung Galaxy A55 trasero", "sort_order": 1},
    {"id": 3, "product_id": 1, "url": "/static/images/products/samsung-a55/side.jpg", "alt_text": "Samsung Galaxy A55 lateral", "sort_order": 2},
    {"id": 4, "product_id": 1, "url": "/static/images/products/samsung-a55/detail.jpg", "alt_text": "Samsung Galaxy A55 detalle", "sort_order": 3},
    # iPhone 15
    {"id": 5, "product_id": 2, "url": "/static/images/products/iphone-15/front.jpg", "alt_text": "iPhone 15 frontal", "sort_order": 0},
    {"id": 6, "product_id": 2, "url": "/static/images/products/iphone-15/back.jpg", "alt_text": "iPhone 15 trasero", "sort_order": 1},
    {"id": 7, "product_id": 2, "url": "/static/images/products/iphone-15/side.jpg", "alt_text": "iPhone 15 lateral", "sort_order": 2},
    # Galaxy Tab S9
    {"id": 8, "product_id": 3, "url": "/static/images/products/galaxy-tab-s9/front.jpg", "alt_text": "Galaxy Tab S9 frontal", "sort_order": 0},
    {"id": 9, "product_id": 3, "url": "/static/images/products/galaxy-tab-s9/back.jpg", "alt_text": "Galaxy Tab S9 trasero", "sort_order": 1},
    {"id": 10, "product_id": 3, "url": "/static/images/products/galaxy-tab-s9/pen.jpg", "alt_text": "Galaxy Tab S9 con S Pen", "sort_order": 2},
    # Sony WH-1000XM5
    {"id": 11, "product_id": 4, "url": "/static/images/products/sony-xm5/front.jpg", "alt_text": "Sony WH-1000XM5 frontal", "sort_order": 0},
    {"id": 12, "product_id": 4, "url": "/static/images/products/sony-xm5/side.jpg", "alt_text": "Sony WH-1000XM5 lateral", "sort_order": 1},
    {"id": 13, "product_id": 4, "url": "/static/images/products/sony-xm5/case.jpg", "alt_text": "Sony WH-1000XM5 caso", "sort_order": 2},
    # MacBook Air M3
    {"id": 14, "product_id": 5, "url": "/static/images/products/macbook-air/open.jpg", "alt_text": "MacBook Air abierto", "sort_order": 0},
    {"id": 15, "product_id": 5, "url": "/static/images/products/macbook-air/closed.jpg", "alt_text": "MacBook Air cerrado", "sort_order": 1},
    {"id": 16, "product_id": 5, "url": "/static/images/products/macbook-air/angle.jpg", "alt_text": "MacBook Air ángulo", "sort_order": 2},
    # Logitech MX Master 3S
    {"id": 17, "product_id": 6, "url": "/static/images/products/mx-master/top.jpg", "alt_text": "MX Master 3S superior", "sort_order": 0},
    {"id": 18, "product_id": 6, "url": "/static/images/products/mx-master/side.jpg", "alt_text": "MX Master 3S lateral", "sort_order": 1},
]

# ── Product Specs ─────────────────────────────────────────────

SPECS = [
    {"id": 1, "product_id": 1, "spec_key": "Tamaño de la pantalla", "spec_value": '6.6 "', "sort_order": 0},
    {"id": 2, "product_id": 1, "spec_key": "Memoria interna", "spec_value": "256 GB", "sort_order": 1},
    {"id": 3, "product_id": 1, "spec_key": "Cámara trasera principal", "spec_value": "50 Mpx", "sort_order": 2},
    {"id": 4, "product_id": 1, "spec_key": "Con NFC", "spec_value": "Sí", "sort_order": 3},
    {"id": 5, "product_id": 1, "spec_key": "Memoria RAM", "spec_value": "8 GB", "sort_order": 4},
    {"id": 6, "product_id": 1, "spec_key": "Cámara frontal principal", "spec_value": "32 Mpx", "sort_order": 5},
    {"id": 7, "product_id": 1, "spec_key": "Desbloqueo", "spec_value": "Huella dactilar y reconocimiento facial", "sort_order": 6},
    {"id": 8, "product_id": 1, "spec_key": "Batería", "spec_value": "5000 mAh", "sort_order": 7},
    {"id": 9, "product_id": 2, "spec_key": "Tamaño de la pantalla", "spec_value": '6.1 "', "sort_order": 0},
    {"id": 10, "product_id": 2, "spec_key": "Memoria interna", "spec_value": "128 GB", "sort_order": 1},
    {"id": 11, "product_id": 2, "spec_key": "Cámara trasera principal", "spec_value": "48 Mpx", "sort_order": 2},
    {"id": 12, "product_id": 2, "spec_key": "Con NFC", "spec_value": "Sí", "sort_order": 3},
    {"id": 13, "product_id": 2, "spec_key": "Chip", "spec_value": "A16 Bionic", "sort_order": 4},
    {"id": 14, "product_id": 3, "spec_key": "Tamaño de la pantalla", "spec_value": '11 "', "sort_order": 0},
    {"id": 15, "product_id": 3, "spec_key": "Memoria interna", "spec_value": "128 GB", "sort_order": 1},
    {"id": 16, "product_id": 3, "spec_key": "Procesador", "spec_value": "Snapdragon 8 Gen 2", "sort_order": 2},
    {"id": 17, "product_id": 3, "spec_key": "Lápiz óptico", "spec_value": "S Pen incluido", "sort_order": 3},
    {"id": 18, "product_id": 4, "spec_key": "Tipo", "spec_value": "Over-ear Inalámbrico", "sort_order": 0},
    {"id": 19, "product_id": 4, "spec_key": "Duración de batería", "spec_value": "30 horas", "sort_order": 1},
    {"id": 20, "product_id": 4, "spec_key": "Cancelación de ruido", "spec_value": "Sí (Auto NC)", "sort_order": 2},
    {"id": 21, "product_id": 4, "spec_key": "Peso", "spec_value": "250g", "sort_order": 3},
    {"id": 22, "product_id": 5, "spec_key": "Tamaño de la pantalla", "spec_value": '13.6 "', "sort_order": 0},
    {"id": 23, "product_id": 5, "spec_key": "Chip", "spec_value": "Apple M3", "sort_order": 1},
    {"id": 24, "product_id": 5, "spec_key": "Memoria", "spec_value": "8 GB", "sort_order": 2},
    {"id": 25, "product_id": 5, "spec_key": "Almacenamiento", "spec_value": "256 GB SSD", "sort_order": 3},
    {"id": 26, "product_id": 5, "spec_key": "Batería", "spec_value": "Hasta 18 horas", "sort_order": 4},
    {"id": 27, "product_id": 6, "spec_key": "DPI", "spec_value": "8000", "sort_order": 0},
    {"id": 28, "product_id": 6, "spec_key": "Duración de batería", "spec_value": "70 días", "sort_order": 1},
    {"id": 29, "product_id": 6, "spec_key": "Conectividad", "spec_value": "Bluetooth + USB", "sort_order": 2},
    {"id": 30, "product_id": 6, "spec_key": "Peso", "spec_value": "141g", "sort_order": 3},
]

# ── Reviews ───────────────────────────────────────────────────

REVIEWS_RAW = {
    1: [("Juan P.", 5, "Excelente teléfono!", "Relación calidad-precio excelente. La cámara es increíble y la batería dura todo el día. Lo recomiendo."), ("Maria L.", 5, "Me encanta!", "Diseño hermoso, rendimiento rápido y el 5G es rapidísimo. El mejor teléfono que he tenido."), ("Carlos R.", 4, "Muy buen teléfono", "Casi perfecto. Gran pantalla, buenas cámaras. Solo un pequeño problema: es un poco pesado."), ("Ana S.", 5, "Regalo perfecto", "Se lo compré a mi hija y le encanta. El color es precioso."), ("Pedro M.", 5, "Calidad Samsung", "Otro gran teléfono Samsung. Experiencia fluida, sin lag, pantalla excelente."), ("Lucia G.", 4, "Gran gama media", "Excelente para el precio. Hace todo lo que necesito y más."), ("Roberto F.", 5, "Cámara impresionante", "La cámara de 50MP toma fotos impresionantes incluso con poca luz."), ("Elena V.", 4, "Bueno pero grande", "Gran teléfono en general, pero es bastante grande. Difícil de usar con una mano.")],
    2: [("Miguel A.", 5, "El mejor iPhone", "Las mejoras en la cámara son notables. Dynamic Island es realmente útil."), ("Laura B.", 5, "Fluidísimo", "iOS funciona perfectamente. USB-C por fin y es genial."), ("Fernando C.", 5, "Vale la actualización", "Vengo del iPhone 13, las mejoras son significativas."), ("Isabella D.", 4, "Genial pero caro", "Teléfono increíble pero el precio es alto."), ("Andres E.", 5, "Experiencia premium", "Cada detalle está pulido. La calidad de construcción es inigualable.")],
    3: [("Gabriel G.", 5, "Tablet perfecta", "El S Pen es responsivo, la pantalla es preciosa. Genial para dibujar."), ("Valentina H.", 4, "Casi perfecta", "Gran tablet por el precio. Ojalá tuviera más RAM."), ("Ricardo I.", 5, "Alternativa a iPad", "Tan buena como iPad Pro por la mitad del precio.")],
    4: [("Patricia J.", 5, "Mejores auriculares NC", "La cancelación de ruido es alucinante. No escucho nada en el metro."), ("Alejandro K.", 5, "Vale cada centavo", "Calidad de sonido superb. Batería eterna. Súper cómodos."), ("Sebastian M.", 5, "Sony lo hace de nuevo", "XM4 era genial, XM5 es mejor en todo.")],
    5: [("Daniela N.", 5, "Laptop perfecta", "El chip M3 es increíblemente rápido. Batería que dura todo el día."), ("Javier O.", 5, "Ligera y potente", "No puedo creer tanto poder en un dispositivo tan delgado."), ("Camila P.", 5, "Vale el cambio", "Vine de Windows. macOS es fluido, el hardware es hermoso."), ("Tomas Q.", 4, "Genial pero cara", "Laptop increíble pero cara para 256GB.")],
    6: [("Martin S.", 5, "El mejor mouse", "La rueda de desplazamiento es mágica. Scroll infinito es un game changer."), ("Adriana T.", 5, "Perfección ergonómica", "Sin dolor de muñeca después de largas sesiones de código."), ("Felipe U.", 4, "Genial para productividad", "Botones personalizables me ahorran muchísimo tiempo.")],
}

REVIEWS = []
review_id = 1
for product_id, reviews_list in REVIEWS_RAW.items():
    for user_name, rating, title, content in reviews_list:
        REVIEWS.append({"id": review_id, "product_id": product_id, "user_name": user_name, "rating": rating, "title": title, "content": content, "created_at": "2025-03-15T10:00:00"})
        review_id += 1

# ── Payment Methods ───────────────────────────────────────────

PAYMENT_METHODS = [
    {"id": 1, "name": "Visa", "type": "credit_card", "icon_url": "/visa.svg", "max_installments": 12, "sort_order": 0},
    {"id": 2, "name": "Mastercard", "type": "credit_card", "icon_url": "/mastercard.svg", "max_installments": 12, "sort_order": 1},
    {"id": 3, "name": "OCA", "type": "credit_card", "icon_url": "/oca.svg", "max_installments": 6, "sort_order": 2},
    {"id": 4, "name": "Visa Débito", "type": "debit_card", "icon_url": "/visa-debit.svg", "max_installments": 1, "sort_order": 3},
    {"id": 5, "name": "Mastercard Débito", "type": "debit_card", "icon_url": "/mc-debit.svg", "max_installments": 1, "sort_order": 4},
    {"id": 6, "name": "Abitab", "type": "cash", "icon_url": "/abitab.svg", "max_installments": 1, "sort_order": 5},
]

# ── Related Products ──────────────────────────────────────────

RELATED_PRODUCTS = [
    {"id": 1, "product_id": 1, "related_id": 2, "title": "Samsung Galaxy M55 5g 8/256gb Dual Sim Teslazero", "price": 421, "original_price": 485, "currency": "US$", "discount_percentage": 13, "image_url": "https://http2.mlstatic.com/D_NQ_NP_2X_679917-MLU75601892489_042024-F.webp", "installments": {"count": 10, "amount": 183.9, "interest_free": True}, "free_shipping": True},
    {"id": 2, "product_id": 1, "related_id": 3, "title": "Motorola Edge 50 Fusion 5g 256 Gb Azul Ártico 8 Gb Ram", "price": 419, "original_price": 493, "currency": "US$", "discount_percentage": 15, "image_url": "https://http2.mlstatic.com/D_NQ_NP_2X_738694-MLU75287269009_032024-F.webp", "installments": {"count": 10, "amount": 182.6, "interest_free": True}, "free_shipping": True},
    {"id": 3, "product_id": 1, "related_id": 4, "title": "Samsung Galaxy A16 5g 8gb 256gb Negro Tranza", "price": 326, "original_price": 337, "currency": "US$", "discount_percentage": 3, "image_url": "https://http2.mlstatic.com/D_NQ_NP_2X_657117-MLA79055270653_092024-F.webp", "installments": {"count": 10, "amount": 142.4, "interest_free": True}, "free_shipping": True},
    {"id": 4, "product_id": 1, "related_id": 5, "title": "Motorola G85 5g 256gb Gris Bram", "price": 329, "original_price": 366, "currency": "US$", "discount_percentage": 10, "image_url": "https://http2.mlstatic.com/D_NQ_NP_2X_712509-MLU75529749901_042024-F.webp", "installments": {"count": 10, "amount": 143.4, "interest_free": True}, "free_shipping": True},
]

# ── Brand Products (Samsung) ─────────────────────────────────

BRAND_PRODUCTS = [
    {"id": 1, "brand": "Samsung", "product_id": 6, "title": "Samsung Galaxy S25 256 Go Garantía Oficial", "price": 959, "original_price": 1299, "currency": "US$", "discount_percentage": 26, "image_url": "https://http2.mlstatic.com/D_NQ_NP_2X_622582-MLA81359159761_122024-F.webp", "installments": {"count": 10, "amount": 418.1, "interest_free": True}, "free_shipping": True},
    {"id": 2, "brand": "Samsung", "product_id": 7, "title": "Samsung Galaxy S25 Plus 512 Go Garantía Oficial", "price": 1379, "original_price": 1699, "currency": "US$", "discount_percentage": 18, "image_url": "https://http2.mlstatic.com/D_NQ_NP_2X_722103-MLA81359142949_122024-F.webp", "installments": {"count": 10, "amount": 601.2, "interest_free": True}, "free_shipping": True},
]


def seed():
    _write("sellers", SELLERS)
    _write("products", PRODUCTS)
    _write("product_images", IMAGES)
    _write("product_specs", SPECS)
    _write("reviews", REVIEWS)
    _write("payment_methods", PAYMENT_METHODS)
    _write("related_products", RELATED_PRODUCTS)
    _write("brand_products", BRAND_PRODUCTS)
    logger.info("Seed complete: %d sellers, %d products, %d images, %d specs, %d reviews, %d payment methods, %d related, %d brand",
                len(SELLERS), len(PRODUCTS), len(IMAGES), len(SPECS), len(REVIEWS), len(PAYMENT_METHODS), len(RELATED_PRODUCTS), len(BRAND_PRODUCTS))


if __name__ == "__main__":
    seed()
