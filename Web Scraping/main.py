import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = 'https://www.bbc.com/news'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/127.0.0.74 Safari/537.36'
}


def fetch_html(url):
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        print("Fetched HTML content successfully.")
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None


def parse_html(html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        print("Parsed HTML content successfully.")
        return soup
    except Exception as e:
        print(f"Error parsing HTML content: {e}")
        return None


def extract_headlines(soup):
    headlines = []
    if soup:
        try:
            items = soup.select('.sc-4fedabc7-3.zTZri')
            if not items:
                print("Warning: No items found with the selector '.sc-4fedabc7-3.zTZri'.")
            for item in items:
                headline = item.get_text(strip=True)  # Strip extra whitespace
                link = item.find_parent('a')['href'] if item.find_parent('a') else 'No link'
                headlines.append({'Headline': headline, 'Link': link})
        except Exception as e:
            print(f"Error extracting headlines: {e}")
    else:
        print("No valid soup object to extract from.")
    return headlines


def save_to_csv(data, filename='headlines.csv'):
    if data:
        try:
            df = pd.DataFrame(data)
            df.to_csv(filename, index=False)
            print(f"Saved data to {filename}")
        except Exception as e:
            print(f"Error saving data to CSV: {e}")
    else:
        print("No data to save.")


def main():
    html_content = fetch_html(URL)
    if html_content:
        soup = parse_html(html_content)
        if soup:
            headlines = extract_headlines(soup)
            if headlines:
                save_to_csv(headlines)


if __name__ == "__main__":
    main()
