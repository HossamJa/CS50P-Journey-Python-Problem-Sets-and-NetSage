import requests
import sys


try:
    if len(sys.argv) != 2:
        sys.exit('Missing command-line argument')

    else:
        respons = requests.get('https://api.coincap.io/v2/assets/bitcoin')
        price = respons.json()
        o = price['data']
        pr = float(o["priceUsd"])
        ask = float(sys.argv[1])
        print(f"${pr*ask:,.4f}")
except ValueError:
    sys.exit('Command-line argument is not a number')
