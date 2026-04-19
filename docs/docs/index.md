# E-Commerce Product Detail Page

A **MercadoLibre-style** e-commerce product detail page built with a modern full-stack architecture.

## Overview

This project implements a responsive product detail page that mimics the look and feel of Mercado Libre's product pages. It features a FastAPI backend serving product data from local JSON files, and a React + TypeScript frontend rendering a polished, responsive UI with real product images.

## Key Features

- **3-column responsive layout** — Gallery | Product Info | Purchase Panel
- **Image gallery** with vertical thumbnails, hover-to-switch, and favorite button
- **Real product images** served from local static files
- **Spanish UI** — MercadoLibre-style with badges, installments, shipping info
- **Dynamic pricing** with discount badges and installment plans
- **Branded payment methods** — VISA, Mastercard, OCA with colored card icons
- **Seller information** with dark "Tienda Oficial" banner and stats grid
- **Related products** carousel and sidebar recommendations
- **Customer reviews** with star distribution charts
- **Stock & shipping** indicators with interactive quantity selector
- **Expandable product specifications** with icons
- **Yellow suggestion bar** matching MercadoLibre's top bar
- **RESTful API** with OpenAPI documentation

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | React 18 + TypeScript + Vite |
| Backend | FastAPI (Python 3.10+) |
| Data Storage | Local JSON files (no database) |
| Images | Static file serving via FastAPI |
| Testing | pytest + httpx (backend) |
| Docs | MkDocs Material |

## Quick Links

- [Quick Start Guide](quickstart.md) — get running in 5 minutes
- [Architecture Overview](architecture.md) — system design and decisions
- [API Reference](api-reference.md) — full endpoint documentation
- [Module Design](modules.md) — component and module details
- [Usage Examples](examples.md) — code samples and interaction
