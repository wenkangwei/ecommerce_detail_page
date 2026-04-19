from datetime import datetime

from sqlalchemy import Float, ForeignKey, Integer, String, Text, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Seller(Base):
    __tablename__ = "sellers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(200))
    is_official: Mapped[bool] = mapped_column(Boolean, default=False)
    reputation: Mapped[str] = mapped_column(String(100))
    location: Mapped[str] = mapped_column(String(200))
    logo_url: Mapped[str] = mapped_column(String(500))
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    products: Mapped[list["Product"]] = relationship(back_populates="seller")


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(500))
    description: Mapped[str] = mapped_column(Text)
    price: Mapped[float] = mapped_column(Float)
    original_price: Mapped[float] = mapped_column(Float)
    currency: Mapped[str] = mapped_column(String(10), default="US$")
    category: Mapped[str] = mapped_column(String(200))
    subcategory: Mapped[str] = mapped_column(String(200))
    stock: Mapped[int] = mapped_column(Integer, default=0)
    rating_avg: Mapped[float] = mapped_column(Float, default=0.0)
    rating_count: Mapped[int] = mapped_column(Integer, default=0)
    free_shipping: Mapped[bool] = mapped_column(Boolean, default=False)
    warranty_months: Mapped[int] = mapped_column(Integer, default=12)
    seller_id: Mapped[int] = mapped_column(ForeignKey("sellers.id"))
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.utcnow, onupdate=datetime.utcnow)

    seller: Mapped["Seller"] = relationship(back_populates="products")
    images: Mapped[list["ProductImage"]] = relationship(
        back_populates="product", order_by="ProductImage.sort_order"
    )
    specs: Mapped[list["ProductSpec"]] = relationship(
        back_populates="product", order_by="ProductSpec.sort_order"
    )
    reviews: Mapped[list["Review"]] = relationship(back_populates="product")


class ProductImage(Base):
    __tablename__ = "product_images"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    url: Mapped[str] = mapped_column(String(500))
    alt_text: Mapped[str] = mapped_column(String(200))
    sort_order: Mapped[int] = mapped_column(Integer, default=0)

    product: Mapped["Product"] = relationship(back_populates="images")


class ProductSpec(Base):
    __tablename__ = "product_specs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    spec_key: Mapped[str] = mapped_column(String(200))
    spec_value: Mapped[str] = mapped_column(String(500))
    sort_order: Mapped[int] = mapped_column(Integer, default=0)

    product: Mapped["Product"] = relationship(back_populates="specs")


class Review(Base):
    __tablename__ = "reviews"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    user_name: Mapped[str] = mapped_column(String(100))
    rating: Mapped[int] = mapped_column(Integer)
    title: Mapped[str] = mapped_column(String(200))
    content: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    product: Mapped["Product"] = relationship(back_populates="reviews")


class PaymentMethod(Base):
    __tablename__ = "payment_methods"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    type: Mapped[str] = mapped_column(String(50))
    icon_url: Mapped[str] = mapped_column(String(500))
    max_installments: Mapped[int] = mapped_column(Integer, default=1)
    sort_order: Mapped[int] = mapped_column(Integer, default=0)
