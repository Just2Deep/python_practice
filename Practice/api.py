# Reading json from api

import json
from urllib.request import urlopen

with urlopen("https://api.coindesk.com/v1/bpi/currentprice.json") as response:
    source = response.read()

data = json.loads(source)

#print(json.dumps(data, indent=2))
currency_dict = {}

for item in data['bpi']:
    currency = item
    rate = data['bpi'][item]['rate']

    currency_dict[currency] = rate

print(currency_dict)
