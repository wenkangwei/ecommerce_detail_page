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
┌──────────────────────────────────────────────────────────────────────────┐
│  Breadcrumb (12px, #666666)                                              │
├─────────────────┬──────────────────────────┬─────────────────────────────┤
│                 │                          │                             │
│  Image Gallery  │  Product Info            │  Purchase Panel             │
│  (440px)        │  (flex-1)                │  (320px)                    │
│                 │                          │                             │
│  ┌────┐ ┌────┐ │  ★ Official Store badge  │  Free Shipping badge (green)│
│  │thumb│ │Main│ │  Product Title 22px      │  Stock indicator (● In Stock)│
│  │ 1  │ │    │ │  Rating ★★★★☆ (4.8)      │  Quantity: 1 unit           │
│  │ 2  │ │    │ │                          │  ┌─────────────────────┐    │
│  │ 3  │ │Img │ │  Price Block:            │  │  [  Buy now  ]      │    │
│  │ 4  │ │    │ │   US$ 499 ─── 12% OFF    │  │  [ Add to cart ]    │    │
│  │ 5  │ │    │ │   US$ 439                │  └─────────────────────┘    │
│  └────┘ └────┘ │   10x US$ 43.90 no int  │  Seller Card                 │
│  (vertical     │                          │  🛡️ Buyer protection         │
│   thumbnails)  │  ✓ Highlight 1           │  🔄 Free returns             │
│                │  ✓ Highlight 2           │  🏆 Factory warranty         │
│                │  ✓ Highlight 3           │  Payment Methods             │
│                │  View characteristics     │  - Credit/debit cards        │
│                │                          │  - Digital wallets           │
├─────────────────┴──────────────────────────┴─────────────────────────────┤
│                                                                          │
│  Characteristics (expandable spec table)                                  │
│                                                                          │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  Product description                                                      │
│                                                                          │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  Reviews Section                                                          │
│  - Average rating + star distribution                                     │
│  - Individual review cards                                                │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

### Grid System
- **Max content width**: `1200px`, centered
- **3-column CSS Grid**: `grid-template-columns: 440px 1fr 320px`
- **Column 1 (Gallery)**: `440px` fixed — vertical thumbnail strip + main image
- **Column 2 (Product Info)**: `flex-1` — title, rating, price, highlights
- **Column 3 (Purchase Panel)**: `320px` fixed — buy buttons, stock, seller, protection, payments
- **Column borders**: `1px solid #E6E6E6` between columns
- **Page padding**: `16px` on each side

### Responsive Breakpoints
| Breakpoint | Layout | Column Behavior |
|------------|--------|-----------------|
| Desktop `>1024px` | Three-column | Gallery 440px / Info flex / Purchase 320px |
| Tablet `768-1024px` | Three-column compressed | Gallery 320px / Info flex / Purchase 260px |
| Mobile `<768px` | Single column | Everything stacks vertically |

---

## 4. Component Specifications

### 4.1 Breadcrumb
- **Position**: Top of content area, above the 3-column layout
- **Style**: Inline text links separated by `›` (chevron)
- **Font**: `12px`, `#666666`
- **Link hover**: `#3483FA` (blue), underline
- **Last item**: Not a link, `#999999`
- **Example**: `Celulares y Smartphones › Celulares Libres › Samsung`

### 4.2 Image Gallery (Column 1)
- **Layout**: Vertical thumbnail strip on the left, main image on the right
- **Main image**:
  - Size: fills remaining space after thumbnails (min-height `400px`)
  - Background: `#FFFFFF`
  - Object-fit: `contain`, max-height `440px`
- **Thumbnail strip**:
  - Position: **Left side** of gallery, vertical (`flex-direction: column`)
  - Width: `52px` strip
  - Thumb size: `48px × 48px`
  - Border: `1px solid #E6E6E6` (default), `2px solid #3483FA` (active/hovered)
  - Gap: `6px`
  - Max height: `440px` with vertical scroll
  - Horizontal scroll on mobile (flex-direction becomes row)
- **Image counter**: Bottom-right corner, `rgba(0,0,0,0.55)` pill, `#FFFFFF`, `11px`
  - Format: `1/5`
- **Thumbnail switch**: `onMouseEnter` and `onClick` — no arrows

### 4.3 Product Info (Column 2)
- **Official badge**: Pill badge with star icon, `--color-primary-light` bg, `12px`
  - Example: `★ Official Samsung Official Store`
- **Title**: `22px`, `#282828`, `font-weight: 400`, wraps to multiple lines
- **Rating**:
  - Stars: `14px`, gold filled `#FFD700`, gray empty `#E0E6ED`
  - Numeric: `14px`, `#666666` (e.g., "4.8")
  - Review count: `14px`, `#3483FA` link (e.g., "(950 reviews)")
- **Price Block**:
  - Current price: `32px`, `#000000`
  - Original price: `14px`, `#999999`, `text-decoration: line-through`
  - Discount badge: `13px`, `#00A650`, `#e8f5e9` background pill, format: "12% OFF"
  - Installment: `14px`, `#666666`, "without interest" in `#00A650` green
- **Highlights**: Below price, top 3 specs as checkmark list
  - Each item: `13px`, `#666666`, with `✓` green icon
- **View characteristics link**: `14px`, `#3483FA`, anchors to specs section

### 4.4 Purchase Panel (Column 3)

#### Stock & Shipping
- **Free shipping badge**:
  - Green background (`#f0faf4`), truck SVG icon + "Free shipping" text
  - `14px`, `#00A650` bold
- **Stock indicator**:
  - Green dot (`8px` circle, `#00A650`) + "In stock" text (`14px`, bold green)
  - Quantity available: `13px`, `#666666`
- **Quantity row**:
  - Separated by top border
  - "Quantity: 1 unit"

#### Buy / Cart Buttons
- **Buy now**: Full width, `background: #3483FA`, `color: #fff`, `16px` bold, `border-radius: 6px`
  - Hover: `background: #2968C8`
- **Add to cart**: Full width, `background: #E3F2FD`, `color: #3483FA`, `16px` bold
  - Hover: `background: #3483FA`, `color: #fff`

#### Seller Card
- **Official store badge**: `background: #3483FA`, `color: #fff`, `10px` bold, uppercase
- **Seller name**: `14px`, `#282828`, bold
- **Sales info**: `12px`, `#666666`
- **Store link**: `13px`, `#3483FA`

#### Buyer Protection
- Three items with emoji icons:
  - 🛡️ Buyer protection — "Receive the product or get your money back"
  - 🔄 Free returns — "30 days to return"
  - 🏆 Factory warranty — "{warranty_months} months"
- Each: icon `18px` + title `13px` bold + desc `12px`

#### Payment Methods
- Section title: `14px` bold
- Installment banner: `13px`, "without interest" in green bold
- Card icons: `44px × 28px` with border, colored by type
  - Credit card: `#f0f4ff` background
  - Debit card: `#f0fff0` background
  - Digital wallet: `#e8f5e9` background
- Expand button: `13px`, `#3483FA`

### 4.5 Product Description (Full Width Below Grid)
- **Section title**: "Product description", `18px`, `#333333`
- **Body text**: `14px`, `#333333`, `line-height: 1.7`

### 4.6 Product Specifications (Full Width Below Grid)
- **Section title**: "Characteristics", `18px`, `#333333`
- **Grid layout**: 2-column grid (`grid-template-columns: 1fr 1fr`)
  - Outer border + border-radius `6px`
  - Odd items: `background: #F5F5F5`
  - Each item: key `12px #999999` + value `14px #282828` bold
  - Border bottom between rows
- **Expandable**: Show first 6 specs, "View all characteristics" button expands full list
- **Expand button**: Full width, border top, `14px`, `#3483FA`

### 4.7 Reviews Section (Full Width Below Grid)
- **Section title**: "Reviews", `18px`, `#333333`
- **2-column layout**: `grid-template-columns: 240px 1fr`
- **Summary bar** (left side, sticky):
  - Average: `48px`, `#282828`, bold
  - Stars: `16px`, gold
  - Total: `14px`, `#666666`
  - Star distribution: horizontal bars
    - Bar color: `#3483FA`, background: `#E6E6E6`
    - Height: `6px`, border-radius `3px`
- **Review cards** (right side):
  - Avatar placeholder: `40px × 40px` circle, `#F5F5F5`
  - User name: `14px`, bold
  - Date: `12px`, `#999999`
  - Rating: stars `14px`, gold
  - Title: `14px`, bold
  - Content: `14px`, `line-height: 1.6`
  - Card: `border: 1px solid #E6E6E6`, `border-radius: 6px`, `box-shadow: 0 1px 2px rgba(0,0,0,0.12)`
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
┌───────────────────────── 1200px max ──────────────────────────┐
│ Breadcrumb                                                     │
├─────────── 440px ──────┬── flex ──┬────── 320px ──────────────┤
│ Image Gallery           │ Product  │ Purchase Panel             │
│ (vertical thumbs +      │ Info     │ - Free Shipping badge      │
│  main image)            │ - Badge  │ - Stock indicator          │
│                         │ - Title  │ - [Buy now]                │
│                         │ - Rating │ - [Add to cart]            │
│                         │ - Price  │ - Seller Card              │
│                         │ - Feats  │ - Buyer Protection         │
│                         │          │ - Payment Methods          │
├─────────────────────────┴──────────┴───────────────────────────┤
│ Characteristics (full width, 2-col grid)                        │
├─────────────────────────────────────────────────────────────────┤
│ Product description (full width)                                 │
├─────────────────────────────────────────────────────────────────┤
│ Reviews (full width, 240px summary + review cards)              │
└─────────────────────────────────────────────────────────────────┘
```

### Tablet (768-1024px)
- Grid: `320px | flex | 260px`
- Smaller image gallery, compressed purchase panel
- Font sizes reduce: title `18px`, price `26px`

### Mobile (<768px)
- Single column, everything stacks vertically
- Image gallery: full width, thumbnails switch to horizontal scroll
- No column borders
- Purchase panel stacks below product info with top border
- Buttons stretch to full width
- Price font size reduces to `26px`
- Product title reduces to `18px`
- Specs grid: single column
- Reviews layout: single column (summary not sticky)
