import requests

# response = requests.get('https://c9t12389.itcs.hpecorp.net:35358/', verify=False)
# print(response.text)

payload = {
    "search_text": 'bank',
    "api_key": '686499b1e93cfa261ddef9faa553f4b9',
    "file_type": 'json',
    "limit": 1
}
#url = 'https://api.stlouisfed.org/fred/series/search?search_text=' + 'bank' + '&api_key=686499b1e93cfa261ddef9faa553f4b9&file_type=json'
url = 'https://api.stlouisfed.org/fred/series/search'

response = requests.get(url, params=payload, verify=False)
print(response.text)
