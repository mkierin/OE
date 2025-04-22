import requests
import csv
import os
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("TYPEFULLY_API_KEY")
if not api_key:
    raise ValueError("TYPEFULLY_API_KEY not set in .env file.")

url = "https://api.typefully.com/v1/drafts/"

csv_path = "tweets/ab_test_tweet_calendar.csv"  # Adjust if needed

def format_tweet(text):
    tweet = text.strip().replace('\n', ' ')
    if len(tweet) > 280:
        tweet = tweet[:277] + '...'
    return tweet

# Read all rows
with open(csv_path, newline='', encoding='utf-8') as csvfile:
    reader = list(csv.DictReader(csvfile))
    fieldnames = reader[0].keys() if reader else []
    if 'Uploaded' not in fieldnames:
        fieldnames = list(fieldnames) + ['Uploaded']

# Process and update
updated_rows = []
for row in reader:
    uploaded = row.get('Uploaded', '').strip().lower()
    if uploaded == 'yes':
        updated_rows.append(row)
        continue
    tweet_text = format_tweet(row["Content Inspiration"])
    date = row["Date"]
    time = row["Scheduled Time"]
    dt_str = f"{date} {time}"
    dt_obj = datetime.strptime(dt_str, "%Y-%m-%d %H:%M")
    scheduled_at = dt_obj.isoformat() + "+02:00"  # Adjust timezone if needed

    payload = {
        "content": tweet_text,
        "scheduledAt": scheduled_at,
        "threadify": False
    }
    headers = {
        "X-API-KEY": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print(f"Tweet scheduled: {tweet_text[:40]}...")
        row['Uploaded'] = 'Yes'
    else:
        print("Failed to schedule tweet:", tweet_text[:40])
        print("Status Code:", response.status_code)
        print("Response:", response.text)
        row['Uploaded'] = row.get('Uploaded', '')  # leave as is
    updated_rows.append(row)

# Write back to CSV
with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(updated_rows)
