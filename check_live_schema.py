import re
import json
import sys

def parse_jsonld_from_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Match script tags with application/ld+json
    pattern = r'<script[^>]*type=application/ld\+json[^>]*>(.*?)</script>'
    matches = re.findall(pattern, html, re.DOTALL)

    print(f"=== {filepath} ===")
    print(f"JSON-LD blocks: {len(matches)}")

    for i, m in enumerate(matches, 1):
        try:
            # Remove outer quotes if present
            if m.startswith('"') and m.endswith('"'):
                m = m[1:-1]
            # Decode double-encoded JSON
            m = m.encode().decode('unicode_escape')
            d = json.loads(m)

            print(f"  Block {i}: @type = {d.get('@type')}")

            # Special handling for BreadcrumbList
            if d.get('@type') == 'BreadcrumbList':
                items = d.get('itemListElement', [])
                names = [it.get('name') for it in items]
                print(f"    Breadcrumb: {' -> '.join(names)}")

            # Special handling for BlogPosting
            if d.get('@type') == 'BlogPosting':
                print(f"    headline: {d.get('headline', 'N/A')[:50]}...")
                print(f"    datePublished: {d.get('datePublished', 'N/A')}")

        except Exception as e:
            print(f"  Block {i}: Error - {e}")
    print()

if __name__ == "__main__":
    parse_jsonld_from_file("homepage.html")
    parse_jsonld_from_file("article.html")