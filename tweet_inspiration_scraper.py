import requests
from bs4 import BeautifulSoup
import csv
import sys
import time

CSV_FILE = 'tweet_inspiration.csv'

# Helper to extract tweet ID from URL
def extract_tweet_id(url):
    if '/status/' in url:
        return url.split('/status/')[-1].split('?')[0]
    return None

# Scrape tweet content and stats (basic public info)
def scrape_tweet(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        print(f'Failed to fetch tweet: {resp.status_code}')
        return None
    soup = BeautifulSoup(resp.text, 'html.parser')
    # Try to find the tweet text (fallback: user pastes manually)
    tweet_text = ''
    for tag in soup.find_all('meta'):
        if tag.get('property') == 'og:description':
            tweet_text = tag.get('content')
    # Stats may not be available without API, set as N/A or parse if visible
    return {
        'url': url,
        'tweet_text': tweet_text,
        'likes': 'N/A',
        'retweets': 'N/A',
        'replies': 'N/A',
        'date': time.strftime('%Y-%m-%d'),
    }

def save_to_csv(data, comment):
    fieldnames = ['url', 'tweet_text', 'likes', 'retweets', 'replies', 'date', 'comment']
    try:
        with open(CSV_FILE, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if csvfile.tell() == 0:
                writer.writeheader()
            data['comment'] = comment
            writer.writerow(data)
    except Exception as e:
        print(f'Error writing to CSV: {e}')

def main():
    if len(sys.argv) < 3:
        print('Usage: python tweet_inspiration_scraper.py <tweet_url> <comment>')
        sys.exit(1)
    url = sys.argv[1]
    comment = sys.argv[2]
    tweet_data = scrape_tweet(url)
    if tweet_data:
        save_to_csv(tweet_data, comment)
        print('Saved inspiration entry!')
    else:
        print('Failed to save tweet.')

if __name__ == '__main__':
    main()
