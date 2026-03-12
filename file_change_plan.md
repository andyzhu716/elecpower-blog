# File-Level Change Plan

Generated for: Hugo Only English + Structure Optimization + Visual Enhancement Transformation

---

## CHANGE CATEGORY 1: CONFIGURATION (Low Risk)

### File: `hugo.toml`

**Changes Required**:
1. REMOVE lines 31-35 (zh-cn language section):
   ```toml
   [languages.zh-cn]
     languageName = '中文'
     weight = 2
     title = 'ElecPower - 工业电力设备解决方案'
     languageDirection = 'ltr'
   ```

2. VERIFY line 3: `defaultContentLanguage = 'en'` (already correct)
3. VERIFY line 4: `defaultContentLanguageInSubdir = false` (already correct)

**Impact**: Site becomes English-only
**Risk**: LOW
**Backup Required**: YES

---

## CHANGE CATEGORY 2: CONTENT REMOVAL (Medium Risk)

### Directory: `content/zh-cn/`

**Files to DELETE**:
1. `content/zh-cn/_index.md` - Chinese homepage
2. `content/zh-cn/about/_index.md` - Chinese about page
3. `content/zh-cn/contact/_index.md` - Chinese contact page

**Action**: Delete entire `content/zh-cn/` directory
**Impact**: Removes all Chinese content
**Risk**: MEDIUM
**Backup Required**: YES
**Post-Action**: Clear public/zh-cn/ with `hugo --gc`

---

## CHANGE CATEGORY 3: CONTENT CREATION (Medium Risk)

### File: `content/products/_index.md`

**Purpose**: New Products section hub
**Suggested Content**:
```markdown
---
title: "Products"
geekdocNav: true
description: "Busbar systems, transformers, and power distribution equipment for industrial applications."
---

# Products

Our complete range of power distribution equipment for industrial and power generation applications.

## Product Categories

{{/* This will be populated when product pages are created */}}
```

**Action**: CREATE
**Risk**: MEDIUM
**Priority**: Phase 3

---

### Files: `content/products/ipb.md`, `content/products/enclosed-busbar.md`, etc.

**Purpose**: Individual product detail pages
**Action**: CREATE (multiple)
**Risk**: MEDIUM
**Priority**: Phase 3

---

### File: `content/faq/_index.md`

**Purpose**: FAQ section with common questions
**Suggested Content**:
```markdown
---
title: "FAQ"
geekdocNav: true
description: "Frequently asked questions about busbar systems, IPB, and power equipment."
---

# Frequently Asked Questions

Common questions about our products and services.

{{/* FAQ items to be added */}}
```

**Action**: CREATE
**Risk**: MEDIUM
**Priority**: Phase 3

---

### File: `content/applications/_index.md`

**Purpose**: Applications/Use Cases section
**Suggested Content**:
```markdown
---
title: "Applications"
geekdocNav: true
description: "Real-world applications of busbar systems and power equipment across industries."
---

# Applications

How our equipment is used across different industries and facilities.

## Industry Applications

{{/* Application categories to be added */}}
```

**Action**: CREATE
**Risk**: MEDIUM
**Priority**: Phase 3

---

## CHANGE CATEGORY 4: TEMPLATE REMOVAL (Low Risk)

### File: `layouts/partials/site-header.html`

**Changes Required**:
1. REMOVE lines 36-47 (language switcher):
   ```html
   <!-- Language Switcher -->
   {{ if hugo.IsMultilingual }}
   <div class="language-switcher">
     {{ $currentLang := .Root.Site.Language.Lang }}
     {{ range .Root.AllTranslations }}
       {{ if eq .Language.Lang $currentLang }}
         <span class="current-language">{{ .Language.LanguageName }}</span>
       {{ else }}
         <a href="{{ .Permalink }}" class="language-link">{{ .Language.LanguageName }}</a>
       {{ end }}
     {{ end }}
   </div>
   {{ end }}
   ```

2. REMOVE lines 87-119 (language switcher CSS styles):
   ```css
   .language-switcher { ... }
   .current-language { ... }
   .language-link { ... }
   @media (max-width: 768px) { ... }
   ```

**Impact**: Removes language switcher from header
**Risk**: LOW
**Backup Required**: YES

---

## CHANGE CATEGORY 5: HOMEPAGE OVERHAUL (Medium Risk)

### File: `content/_index.md`

**Current State**: Basic corporate homepage with sections

**Proposed New Content**:
```markdown
---
title: "Industrial Power Equipment Solutions"
geekdocNav: false
---

# New Homepage Structure

## Hero Section
**Simplified value proposition with 1-2 CTAs**

## Core Product Categories
**Cards for IPB, Enclosed Busbar, Common Enclosure Bus**

## Why Choose Us
**Technical strength, standards compliance**

## Latest Articles
**3-6 most recent blog posts**

## Applications
**Power plants, industrial facilities, commercial buildings**

## FAQ Preview
**3-5 most common questions**

## Final CTA
**Contact button with specific messaging**
```

**Action**: COMPLETE REWRITE
**Risk**: MEDIUM
**Priority**: Phase 3 (after structure planning)

---

## CHANGE CATEGORY 6: CSS ENHANCEMENT (Low Risk)

### File: `assets/css/custom.css`

**Current Features**:
- Industrial color scheme
- Header styling
- Content styling
- Card styles for lists
- Contact info styling
- Table styling

**Proposed Enhancements**:

### Add Card Components
```css
/* Product Cards */
.product-card {
  background: var(--industrial-light);
  border-left: 4px solid var(--industrial-blue);
  padding: 1.5rem;
  border-radius: 0 4px 4px 0;
  transition: transform 0.3s, box-shadow 0.3s;
  height: 100%;
}

.product-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

/* Blog Post Cards */
.blog-card {
  background: white;
  border: 1px solid #dee2e6;
  border-radius: 4px;
  padding: 1.5rem;
  transition: box-shadow 0.3s;
}

.blog-card:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}
```

### Improve Article Typography
```css
/* Article Content Width */
.gdoc-markdown {
  max-width: 800px;
  margin: 0 auto;
  line-height: 1.8;
}

/* Better Headings */
.gdoc-markdown h2 {
  margin-top: 2.5rem;
  margin-bottom: 1rem;
}

.gdoc-markdown h3 {
  margin-top: 2rem;
  margin-bottom: 0.75rem;
}
```

### Unify Button Styles
```css
/* CTA Buttons */
.cta-button {
  background: var(--industrial-blue);
  color: white;
  padding: 0.75rem 1.5rem;
  border-radius: 4px;
  font-weight: 600;
  transition: background 0.3s;
}

.cta-button:hover {
  background: #004494;
}
```

**Action**: APPEND new styles
**Risk**: LOW
**Priority**: Phase 4

---

## CHANGE CATEGORY 7: INTERNAL LINKING (Medium Risk)

### Files to be created/modified:

**`layouts/partials/related-products.html`**
**`layouts/partials/related-articles.html`**
**`layouts/partials/related-faqs.html`**

**Action**: CREATE new partials
**Risk**: MEDIUM
**Priority**: Phase 3

---

## FILES TO BACKUP BEFORE CHANGES

1. `hugo.toml`
2. `content/_index.md`
3. `layouts/partials/site-header.html`
4. `assets/css/custom.css`
5. Entire `content/zh-cn/` directory (before deletion)

---

## VERIFICATION STEPS

After all changes, run:

```bash
# Step 1: Clean build
hugo --gc --minify

# Step 2: Check public/ directory
# Should NOT contain /zh-cn/ subdirectory

# Step 3: Test local server
hugo server

# Step 4: Check generated HTML
# No "中文" text
# No language switcher in header
# English-only content

# Step 5: Verify sitemap.xml
# Should only contain English URLs
```

---

## ROLLBACK PLAN

If critical issues occur:

1. Restore from Git:
   ```bash
   git checkout -- hugo.toml content/_index.md layouts/partials/site-header.html
   ```

2. Restore Chinese content (if needed):
   ```bash
   git checkout -- content/zh-cn/
   ```

3. If theme files were modified (SHOULD NOT HAPPEN):
   ```bash
   cd themes/hugo-geekdoc
   git checkout -- .
   ```

---

## SUMMARY

**Total Files to Modify**: 5
**Total Files to Create**: 8+
**Total Files to Delete**: 3 (zh-cn content)

**Risk Distribution**:
- LOW Risk: 3 changes (config, header partial, CSS)
- MEDIUM Risk: 5+ changes (content structure, homepage)
- HIGH Risk: 0 (intentionally excluded)
