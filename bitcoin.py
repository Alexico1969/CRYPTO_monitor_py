import apikey
import requests

headers = {
    'X-CMC_PRO_API_KEY' : apikey.key,
    'Accepts' : 'application/json'
}

params = {
    'start' : '1', 
    'limit' : '15', 
    'convert' : 'EUR'
}

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

json = requests.get(url, params=params, headers=headers).json()

#print(json)