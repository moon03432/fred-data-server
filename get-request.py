import requests
import json

no_text = "monetary"

payload = {
    "search_text": "healthcare equipement",
    "api_key": '686499b1e93cfa261ddef9faa553f4b9',
    "file_type": 'json'
}

url = 'https://api.stlouisfed.org/fred/series/search'

response = requests.get(url, params=payload, verify=False)

data = json.dumps(response.text)

print(data)
