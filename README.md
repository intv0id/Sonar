📡 WebSonar
===

SEO tool for e-commerce
---

WebSonar identifies websites providers within the first results of popular search engines.

---

## ⚙ Setup

1. Setup python >= 3.9

2. Run

``` bash
python -m pip install WebSonar
```

## Examples

See full range of examples in the `Examples` folder.

### Sample code:

``` python
from WebSonar.Common.Enums.SearchEngines import SearchEngines
from WebSonar.Engine.SonarEngine import SonarEngine

query = "Shopify"
search_engines=[SearchEngines.Google]
number = 10

WebSonar = SonarEngine()
WebSonar_results = WebSonar.IdentifySitesFromSearchQuery(
    query=query, 
    search_engines=[SearchEngines.Google],
    number=number)

for search_engine, results in WebSonar_results.items():
    print(f"Search engine: {search_engine.name}\n")
    for n, (url, site_type) in enumerate(results.items()):
        print(f"\t{1+n}\t{url}")
        print(f"\t\t\t{site_type.name}")
    print("\n" + " - " * 10 + "\n")
```
