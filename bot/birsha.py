import requests

def get_dollar():
    url = https://yobit.net/api/3/usd_rub/ticker
    r = requests.get(url).content.json()
    price = r['ticker']['last']
    return  str(price) + 'rub'
