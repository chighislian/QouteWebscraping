import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

quotes = []
authors = []

# how many pages to scrape (each has ~30 quotes)
for page in range(1, 11):  # scrape first 10 pages (≈ 300 quotes)
    url = f"https://www.goodreads.com/quotes/tag/motivational?page={page}"
    print(f"Scraping page {page}...")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    for quote_div in soup.find_all("div", class_="quoteText"):
        text = quote_div.get_text(strip=True, separator=" ")
        # clean formatting
        if "―" in text:
            quote_part, author_part = text.split("―", 1)
            quote = quote_part.strip("“” ").replace("\n", " ")
            author = author_part.strip().split(",")[0]
            quotes.append(quote)
            authors.append(author)
    time.sleep(2)  # be polite

# save to CSV
df = pd.DataFrame({"Quote": quotes, "Author": authors})
df.to_csv("motivational_quotes.csv", index=False)
print(f"Saved {len(df)} quotes to motivational_quotes.csv!")