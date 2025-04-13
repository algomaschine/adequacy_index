import requests
from datetime import datetime
import csv
import json

# API endpoint
url = 'https://api.alternative.me/fng/?limit=3000'  # Removed format=csv since we want JSON

# Fetch the data
response = requests.get(url)
if response.status_code != 200:
    print(f"Error fetching data: {response.status_code}")
    exit()

try:
    # Parse JSON response
    data = response.json()
    
    # Process the data
    processed_data = []
    for item in data['data']:
        try:
            # Extract timestamp and value
            timestamp = int(item['timestamp'])
            value = item['value']
            
            # Convert timestamp to date
            date_obj = datetime.fromtimestamp(timestamp)
            formatted_date = date_obj.strftime('%Y-%m-%d')
            
            # Store as tuple (date, value)
            processed_data.append((formatted_date, value))
        except (ValueError, KeyError) as e:
            print(f"Skipping entry due to error: {e}")
            continue

    # Sort by date in ascending order
    sorted_data = sorted(processed_data, key=lambda x: x[0])

    # Write to CSV
    with open('crypto_fear_and_greed_index.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # Write header
        writer.writerow(['date', 'value'])
        # Write sorted data
        for date, value in sorted_data:
            writer.writerow([date, value])

    print("CSV file 'crypto_fear_and_greed_index.csv' has been created successfully.")

except json.JSONDecodeError as e:
    print(f"Error decoding JSON response: {e}")
    print("Response content:", response.text[:200])  # Print first 200 chars of response for debugging
    exit(1)