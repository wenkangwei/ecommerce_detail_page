import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import init_store
from app.routers import payments, products, reviews, sellers
from app.schemas import ApiResponse, HealthData

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_store()
    logger.info("Application started")
    yield
    logger.info("Application shutting down")


app = FastAPI(
    title="E-Commerce Detail API",
    version="1.0.0",
    description="Backend API for MercadoLibre-style product detail page",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

app.include_router(products.router, prefix="/api/v1")
app.include_router(sellers.router, prefix="/api/v1")
app.include_router(reviews.router, prefix="/api/v1")
app.include_router(payments.router, prefix="/api/v1")


@app.get("/health", response_model=ApiResponse[HealthData])
async def health_check():
    return ApiResponse(data=HealthData())
