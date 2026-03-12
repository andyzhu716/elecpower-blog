# Hugo Website Audit Findings

Generated: 2026-03-12

---

## 1. Current Chinese Residue Audit

### Configuration Layer Chinese

**File**: `hugo.toml`
- Lines 31-35: `[languages.zh-cn]` section exists
  ```toml
  [languages.zh-cn]
    languageName = '中文'
    weight = 2
    title = 'ElecPower - 工业电力设备解决方案'
    languageDirection = 'ltr'
  ```

### Template Layer Chinese

**File**: `layouts/partials/site-header.html`
- Lines 36-47: Language switcher implementation (will be removed)
- This is functional code, not hardcoded Chinese strings

**Theme i18n**: hugo-geekdoc theme has language switcher functionality

### Content Layer Chinese

**Chinese Files Found**:
1. `content/zh-cn/_index.md` - Chinese homepage
2. `content/zh-cn/about/_index.md` - Chinese about page
3. `content/zh-cn/contact/_index.md` - Chinese contact page
4. `content/_index.md` (English) - Contains "Industrial Power Equipment Solutions"
5. `content/about.md` - Contains "About Wetown" (different brand name from title)

**Note**: Chinese content is complete and structured, ready for removal

### Navigation/Button/UI Chinese

**Header**: Language switcher in header shows "English | 中文" buttons
**Built URLs**: Public/ directory contains `/zh-cn/` subdirectory with Chinese pages

---

## 2. Current Homepage Structure Diagnosis

**File**: `content/_index.md`
**Current Structure**:
1. Hero: "Industrial Power Equipment Solutions"
2. Intro paragraph: "ElecPower supplies busbar systems..."
3. Section 1: "Busbar Systems" with 3 bullet points
4. Section 2: "Supporting Equipment" with 2 bullet points  
5. Section 3: "Contact" with 4 contact details
6. Call-to-action: Blockquote with contact message

**Visual Style from custom.css**:
- Dark gradient header (#1a1a1a to #2c3e50)
- Blue industrial theme (#0056b3)
- Card-style bullet lists with left border
- Professional color scheme applied

**Issues Identified**:
- Homepage is very basic, lacks visual hierarchy
- No product categories visualization
- No Latest Articles section
- No FAQ preview
- No Applications/Use Cases section
- No "Why Choose / Technical Strength" section

---

## 3. Current Navigation Structure

**Based on hugo-geekdoc theme + content structure**:

Current Navigation:
```
[Home (implied)]
Blog
About
Contact
```

**Language Switcher**:
- English (default)
- 中文

**Missing**:
- Products section (no dedicated page)
- Applications section (no dedicated page)
- FAQ section (no dedicated page)

---

## 4. Recommended New Navigation Structure

**Option A - Comprehensive**:
```
Home
Products
Applications
Blog
FAQ
About
```

**Option B - Minimal**:
```
Home
Products
Blog
FAQ
About
```

**Recommendation**: Option A (Comprehensive)
- Adds Applications to connect products with use cases
- Creates complete content structure
- Better for SEO/GEO value

---

## 5. Recommended New Homepage Module Order

1. **Hero** (Simplified)
   - Clear value proposition
   - 1-2 CTAs maximum
   - Remove generic "leading/innovative" claims

2. **Core Product Categories**
   - Visual cards for IPB, Enclosed Busbar, Common Enclosure Bus
   - Links to product detail pages
   - Short descriptions

3. **Why Choose / Technical Strength**
   - IEC/GB standard compliance
   - Factory acceptance testing
   - Industry experience

4. **Latest Articles / Technical Insights**
   - 3-6 most recent blog posts
   - Categories visible
   - Link to full Blog section

5. **Applications / Use Cases**
   - Power plants, industrial facilities, commercial buildings
   - Visual representation
   - Connect products to scenarios

6. **FAQ Preview**
   - 3-5 most common questions
   - Link to full FAQ section

7. **Final CTA**
   - Contact button
   - Specific CTA text

---

## 6. Internal Linking Strategy

### Current State: Minimal Linking
- No related content on pages
- No article-product connections
- No FAQ-to-article connections

### Proposed Linking Network

**Product Pages** (to be created):
- Bottom: Related Articles, FAQs, Applications

**Article Pages**:
- Bottom: Related Products, Related Articles, Contact CTA

**FAQ Pages** (to be created):
- Links: Related products, Related articles

**This transforms site from "page stack" to "content network"**

---

## 7. Risk Assessment

### High-Risk Template Files (DO NOT MODIFY)

1. `layouts/partials/microformats/schema.html` - Custom schema implementation
   - Contains Chinese comments
   - Working correctly
   - **Action**: Leave as-is, will update comments to English separately

2. `themes/hugo-geekdoc/` - Theme files
   - Do not modify theme files
   - Use overrides in `layouts/` directory

3. `.github/workflows/hugo.yml` - Deployment workflow
   - Not verified yet, assume working
   - **Action**: Do not touch

4. `CNAME` - Domain configuration
   - Not verified yet
   - **Action**: Do not touch

### Medium-Risk Files

1. `hugo.toml` - Remove zh-cn language section
2. `content/zh-cn/` directory - Delete Chinese content
3. Homepage template - If customizations exist

### Low-Risk Files

1. `content/_index.md` - Update homepage structure
2. `content/blog/_index.md` - Already English
3. `content/blog/*.md` - Already English
4. `assets/css/custom.css` - Visual enhancements

---

## 8. File Change Summary

### Configuration Layer
- `hugo.toml`: Remove zh-cn language section

### Content Layer
- `content/_index.md`: Restructure homepage
- `content/zh-cn/` directory: DELETE
- `content/products/` directory: CREATE (new)
- `content/faq/` directory: CREATE (new)
- `content/applications/` directory: CREATE (new)

### Template Layer
- `layouts/index.html`: CREATE (custom homepage layout)
- `layouts/partials/`: Create homepage section partials if needed

### Style Layer
- `assets/css/custom.css`: Enhance visuals

---

## 9. Visual System Recommendations

### Current Colors (from custom.css)
- `--industrial-blue: #0056b3`
- `--industrial-dark: #1a1a1a`
- `--industrial-light: #f8f9fa`
- `--industrial-gray: #6c757d`
- `--industrial-accent: #28a745`

### Recommended Enhancements
1. Add card hover effects
2. Standardize card heights (products, blog posts)
3. Improve article page typography (line-height, readability)
4. Add section padding consistency
5. Unify button styles across all CTAs
