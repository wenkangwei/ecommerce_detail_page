# Frontend Style & UI Design Specification

> This document defines the exact visual design of the e-commerce product detail page, derived from the MercadoLibre reference screenshot.

---

## 1. Color Palette

### Primary Colors
| Token | Hex | Usage |
|-------|-----|-------|
| `--color-bg` | `#FFFFFF` | Page background |
| `--color-surface` | `#F5F5F5` | Section backgrounds, alternating rows |
| `--color-primary` | `#3483FA` | Primary buttons, links, active states |
| `--color-primary-hover` | `#2968C8` | Button hover state |
| `--color-secondary` | `#E3F2FD` | Secondary button background |

### Text Colors
| Token | Hex | Usage |
|-------|-----|-------|
| `--color-text-primary` | `#333333` | Headings, product title, body text |
| `--color-text-secondary` | `#666666` | Secondary info, breadcrumb, descriptions |
| `--color-text-muted` | `#999999` | Placeholder, disabled text |
| `--color-text-link` | `#3483FA` | All clickable links |

### Semantic Colors
| Token | Hex | Usage |
|-------|-----|-------|
| `--color-success` | `#00A650` | "In Stock", "Free Shipping", positive badges |
| `--color-warning` | `#FF9800` | Discount badges |
| `--color-price` | `#000000` | Current price text |
| `--color-original-price` | `#999999` | Strikethrough original price |
| `--color-star` | `#FFD700` | Rating stars (filled) |
| `--color-star-empty` | `#E0E0E0` | Rating stars (empty) |

### Border & Shadow
| Token | Value | Usage |
|-------|-------|-------|
| `--color-border` | `#E6E6E6` | Card borders, dividers |
| `--shadow-card` | `0 1px 2px 0 rgba(0,0,0,0.12)` | Cards |
| `--shadow-elevated` | `0 4px 8px 0 rgba(0,0,0,0.1)` | Hover states |

---

## 2. Typography

| Element | Size | Weight | Line Height | Color |
|---------|------|--------|-------------|-------|
| Product Title | `24px` | 400 | 1.25 | `#333333` |
| Section Title | `18px` | 400 | 1.4 | `#333333` |
| Body Text | `14px` | 400 | 1.6 | `#333333` |
| Small / Caption | `12px` | 400 | 1.4 | `#666666` |
| **Current Price** | `36px` | 400 | 1.1 | `#000000` |
| Original Price | `16px` | 400 | 1.4 | `#999999` (strikethrough) |
| Discount Badge | `14px` | 400 | 1.2 | `#00A650` |
| Installment Text | `14px` | 400 | 1.4 | `#666666` |
| Breadcrumb | `12px` | 400 | 1.4 | `#666666` |
| Rating Number | `14px` | 400 | 1.2 | `#666666` |
| Spec Key | `14px` | 400 | 1.4 | `#999999` |
| Spec Value | `14px` | 400 | 1.4 | `#333333` |

**Font Family**: `-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif`

---

## 3. Layout Structure

### Page Layout (Desktop > 1024px)
```
┌──────────────────────────────────────────────────────┐
│  Breadcrumb (12px, #666666)                          │
├────────────────────────────┬─────────────────────────┤
│                            │                         │
│  Image Gallery (480px)     │  Price Block            │
│  - Main image              │  - Current price 36px   │
│  - Thumbnail strip         │  - Original price       │
│                            │  - Discount badge        │
│                            │  - Installment info      │
│                            ├─────────────────────────┤
│                            │  Stock & Shipping        │
│                            │  - Green "In Stock"      │
│                            │  - Free Shipping badge   │
│                            ├─────────────────────────┤
│                            │  Seller Card             │
│                            │  - Official badge        │
│                            │  - Seller name           │
│                            ├─────────────────────────┤
│                            │  Payment Methods         │
│                            │  - Card icons            │
│                            │  - Installment options   │
│                            │                         │
├────────────────────────────┴─────────────────────────┤
│                                                      │
│  Product Description                                  │
│  - Title 18px                                         │
│  - Full description text 14px                         │
│                                                      │
├──────────────────────────────────────────────────────┤
│                                                      │
│  Product Specifications (key-value table)             │
│                                                      │
├──────────────────────────────────────────────────────┤
│                                                      │
│  Reviews Section                                      │
│  - Average rating + star distribution                 │
│  - Individual review cards                            │
│                                                      │
└──────────────────────────────────────────────────────┘
```

### Grid System
- **Max content width**: `1200px`, centered
- **Left column**: `~60%` (image gallery + description + specs)
- **Right column**: `~40%` (price, stock, seller, payments — "sidebar")
- **Column gap**: `32px`
- **Page padding**: `16px` on each side

### Responsive Breakpoints
| Breakpoint | Layout | Column Behavior |
|------------|--------|-----------------|
| Desktop `>1024px` | Two-column | Left 60% / Right 40% |
| Tablet `768-1024px` | Two-column compressed | Left 55% / Right 45%, smaller images |
| Mobile `<768px` | Single column | Right column stacks below image |

---

## 4. Component Specifications

### 4.1 Breadcrumb
- **Position**: Top of content area, above the two-column layout
- **Style**: Inline text links separated by `›` (chevron)
- **Font**: `12px`, `#666666`
- **Link hover**: `#3483FA` (blue), underline
- **Last item**: Not a link, `#999999`
- **Example**: `Celulares y Smartphones › Celulares Libres › Samsung`

### 4.2 Image Gallery
- **Main image**:
  - Size: `480px × 480px` (desktop), full-width (mobile)
  - Border: `none`
  - Background: `#F5F5F5` (when image doesn't fill)
  - Object-fit: `contain`
- **Thumbnail strip**:
  - Position: Below main image
  - Size: `56px × 56px` each
  - Border: `1px solid #E6E6E6` (default), `2px solid #3483FA` (selected)
  - Gap: `8px`
  - Horizontal scroll on mobile
- **Image counter**: Top-right corner, `12px`, `#666666`, format: `1/5`
- **No arrows** — thumbnail click only (matching reference)

### 4.3 Product Title & Info
- **Title**: `24px`, `#333333`, wraps to multiple lines
- **Rating**:
  - Stars: `14px`, gold filled `#FFD700`, gray empty `#E0E6ED`
  - Numeric: `14px`, `#666666` (e.g., "4.8")
  - Review count: `14px`, `#3483FA` link (e.g., "950 reviews")
- **Short features**: Below rating, icon + text list
  - Each item: `14px`, `#333333`
  - Bullet points with small icons (checkmark, etc.)

### 4.4 Price Block
- **Current price**: `36px`, `#000000`, no bold
- **Original price**: `16px`, `#999999`, `text-decoration: line-through`
- **Discount badge**:
  - Text: `14px`, `#00A650` (green, not orange), format: "12% OFF"
  - No background, just colored text
- **Installment line**:
  - Text: `14px`, `#666666`
  - Format: "in 10 installments of $43.90 without interest"
  - "without interest" in `#00A650` green

### 4.5 Stock & Shipping
- **Stock badge**:
  - Text: "In Stock", `14px`, `#00A650`
  - Icon: small checkmark circle, green
- **Free shipping badge**:
  - Text: "Free Shipping", `14px`, `#00A650`
  - Icon: small truck icon, green
  - Subtitle: "to all country", `12px`, `#666666`
- **Delivery estimate**:
  - Format: "Estimated delivery between Apr 25 - Apr 28"
  - Font: `14px`, `#666666`
- **Divider**: `1px solid #E6E6E6` between stock/shipping/delivery rows
- **Internal padding**: `16px`
- **Background**: `#FFFFFF`
- **Border**: `1px solid #E6E6E6`, `border-radius: 6px`

### 4.6 Seller Card
- **Official store badge**:
  - Background: `#3483FA` (blue) pill/ribbon shape
  - Text: "Official Store", `12px`, `#FFFFFF`, bold
  - Position: above seller name
- **Seller name**: `16px`, `#333333`, bold
- **Seller info**: `14px`, `#666666`
- **Link**: "See seller's store", `14px`, `#3483FA`
- **Card style**: same as stock card — `border: 1px solid #E6E6E6`, `border-radius: 6px`

### 4.7 Payment Methods
- **Section title**: "Payment methods", `14px`, `#333333`
- **Card icons**: `40px × 24px`, grayscale, with labels below
- **Installment highlight**:
  - Green text: "up to 12 installments without interest"
  - `14px`, `#00A650`
- **Collapsible**: "See all payment methods" link, `14px`, `#3483FA`
- **When expanded**: shows credit cards, debit cards, digital wallets in sections

### 4.8 Product Description
- **Section title**: "Product description", `18px`, `#333333`
- **Body text**: `14px`, `#333333`, `line-height: 1.6`
- **Max height**: `300px` with fade-out overlay, "See more" button
- **When expanded**: full height, "See less" button

### 4.9 Product Specifications
- **Section title**: "Product specifications", `18px`, `#333333`
- **Table layout**:
  - Key column: `40%`, `14px`, `#999999`, `background: #F5F5F5`
  - Value column: `60%`, `14px`, `#333333`
  - Row height: `40px`
  - Alternating row bg: `#F5F5F5` / `#FFFFFF`
  - Row border: `none` (use background color difference)
- **Expandable**: Show first 5 specs, "See all specifications" expands full list
- **Button**: `14px`, `#3483FA`, no background, centered

### 4.10 Reviews Section
- **Section title**: "Reviews", `18px`, `#333333`
- **Summary bar** (left side):
  - Average: `48px`, `#333333`, bold
  - Stars: `16px`, gold
  - Total: "950 reviews", `14px`, `#666666`
  - Star distribution: horizontal bars
    - 5 stars → green bar width proportional
    - 4 stars, 3 stars, etc.
    - Bar color: `#3483FA`
    - Bar background: `#E6E6E6`
- **Review cards** (right side):
  - Avatar placeholder: `40px × 40px` circle, `#E6E6E6`
  - User name: `14px`, `#333333`
  - Date: `12px`, `#999999`
  - Rating: stars `14px`, gold
  - Title: `14px`, `#333333`, bold
  - Content: `14px`, `#333333`, `line-height: 1.6`
  - Card padding: `16px`
  - Card border: `1px solid #E6E6E6`, `border-radius: 6px`
  - Gap between cards: `16px`

---

## 5. Spacing System

| Token | Value | Usage |
|-------|-------|-------|
| `--space-xs` | `4px` | Inline gaps |
| `--space-sm` | `8px` | Small component gaps |
| `--space-md` | `16px` | Card padding, standard gaps |
| `--space-lg` | `24px` | Section gaps |
| `--space-xl` | `32px` | Major section gaps, column gap |
| `--space-2xl` | `48px` | Top-level page margins |

---

## 6. Shadows & Borders

| Element | Shadow | Border | Border Radius |
|---------|--------|--------|---------------|
| Cards (sidebar) | `0 1px 2px rgba(0,0,0,0.12)` | `1px solid #E6E6E6` | `6px` |
| Thumbnail (default) | none | `1px solid #E6E6E6` | `4px` |
| Thumbnail (active) | none | `2px solid #3483FA` | `4px` |
| Buttons (primary) | none | none | `6px` |
| Spec table | none | none | `6px` (outer container) |
| Review card | `0 1px 2px rgba(0,0,0,0.12)` | `1px solid #E6E6E6` | `6px` |

---

## 7. Button Styles

### Primary Button (Buy Now)
```css
background: #3483FA;
color: #FFFFFF;
font-size: 16px;
padding: 12px 32px;
border-radius: 6px;
border: none;
cursor: pointer;
/* Hover */
background: #2968C8;
```

### Secondary Button (Add to Cart)
```css
background: #E3F2FD;
color: #3483FA;
font-size: 16px;
padding: 12px 32px;
border-radius: 6px;
border: none;
cursor: pointer;
/* Hover */
background: #3483FA;
color: #FFFFFF;
```

### Text Link
```css
color: #3483FA;
text-decoration: none;
/* Hover */
text-decoration: underline;
```

---

## 8. Responsive Design Details

### Desktop (>1024px)
```
┌───────────────────── 1200px max ─────────────────────┐
│ Breadcrumb                                           │
├──────────────── 60% ────────┬────── 40% ─────────────┤
│ Image Gallery               │ Price Block            │
│ (480px max)                 │ Stock & Shipping       │
│                             │ Seller Card            │
│                             │ Payment Methods        │
├─────────────────────────────┴────────────────────────┤
│ Description (full width)                              │
├──────────────────────────────────────────────────────┤
│ Specifications (full width)                           │
├──────────────────────────────────────────────────────┤
│ Reviews (full width)                                  │
└──────────────────────────────────────────────────────┘
```

### Tablet (768-1024px)
- Content max-width: `100%` (full width with `16px` padding)
- Left column: `55%`, Right column: `45%`
- Image gallery: `360px` max
- Font sizes stay the same

### Mobile (<768px)
- Single column, everything stacked
- Image gallery: full width, smaller thumbnails
- Right column items become full-width cards
- Buttons stretch to full width
- Price font size reduces to `28px`
- Product title reduces to `20px`
