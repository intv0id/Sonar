#! /usr/bin/env python3
#coding: utf-8

from src.Common.Enums.SearchEngines import SearchEngines
from src.Engine.SonarEngine import SonarEngine

query = "Shopify"
search_engines=[SearchEngines.Google]
number = 10

sonar = SonarEngine()
sonar_results = sonar.IdentifySitesFromSearchQuery(
    query=query, 
    search_engines=[SearchEngines.Google],
    number=number)

for search_engine, results in sonar_results.items():
    print(f"Search engine: {search_engine.name}\n")
    for n, (url, site_type) in enumerate(results.items()):
        print(f"\t{1+n}\t{url}")
        print(f"\t\t\t{site_type.name}")
    print("\n" + " - " * 10 + "\n")
