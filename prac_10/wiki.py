"""
CP1404 Practical
Testing the wikipedia package
"""

import wikipedia

search_query = input("Search phrase: ")
while search_query != '':
    try:
        searched_page = wikipedia.page(search_query)
        print(f"Title: {searched_page.title}\nSummary: {wikipedia.summary(search_query)}URL: {searched_page.url}\n")
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    search_phrase = input("Search phrase: ")