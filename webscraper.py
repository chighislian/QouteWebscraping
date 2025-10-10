from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Chrome()  # or use Edge/Firefox if you prefer
quotes = []
authors = []

for page in range(1, 21):  # scrape 5 pages (~150 quotes)
    url = f"https://www.goodreads.com/quotes/tag/motivational?page={page}"
    print(f"Scraping page {page}...")
    driver.get(url)
    time.sleep(3)  # let it load fully

    quote_divs = driver.find_elements(By.CLASS_NAME, "quoteText")
    for div in quote_divs:
        text = div.text.strip()
        if "―" in text:
            quote_part, author_part = text.split("―", 1)
            quote = quote_part.strip("“” ").replace("\n", " ")
            author = author_part.strip().split(",")[0]
            quotes.append(quote)
            authors.append(author)

driver.quit()

df = pd.DataFrame({"Quote": quotes, "Author": authors})
df.to_csv("motivational_quotes.csv", index=False)
print(f"Saved {len(df)} quotes to motivational_quotes.csv!")