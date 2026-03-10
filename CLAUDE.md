# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Hugo-based bilingual industrial B2B website for ElecPower, providing power equipment solutions (busbar systems, transformers, energy storage) for overseas customers.

## Build Commands

```bash
# Build the site with garbage collection and minification
hugo --gc --minify

# Run local development server
hugo server

# Build for production (outputs to public/)
hugo
```

## Architecture

- **Framework**: Hugo static site generator
- **Theme**: hugo-geekdoc (git submodule at `themes/hugo-geekdoc`)
- **Content Structure**:
  - English content: `content/*.md` (home, about, contact)
  - Chinese content: `content/zh-cn/*.md`
- **Multilingual Routing**: English at `/`, Chinese at `/zh-cn/`
- **Customizations**: `layouts/partials/site-header.html` for language switcher, `assets/css/custom.css` for styling

## Key Configuration (hugo.toml)

- `defaultContentLanguage = "en"` - English is default
- `defaultContentLanguageInSubdir = false` - English at root, not /en/
- `baseURL = "https://www.elecpower.cn/"`

## Adding New Pages

1. Create English content at `content/<page>.md`
2. Create Chinese translation at `content/zh-cn/<page>.md`
3. Include translation links between languages

## Language Switcher

The language switcher is implemented in `layouts/partials/site-header.html`. It uses `.AllTranslations` to link between English and Chinese versions of the current page.