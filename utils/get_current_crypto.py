import asyncio

import requests
import json
from utils.db_api import quick_commands as commands

url_all = "https://api.bittrex.com/api/v1.1/public/getcurrencies"

INTERVAL = 1

j = requests.get(url_all)
data = json.loads(j.text)
allc = [d['Currency'] for d in data['result']]


async def get_price():
    while True:
        await asyncio.sleep(3600)

        url_BTC = f"https://api.bittrex.com/api/v1.1/public/getticker?market=USD-BTC"
        j_BTC = requests.get(url_BTC)
        data_BTC = json.loads(j_BTC.text)
        price_BTC = data_BTC['result']['Ask']

        url_USDT = f"https://api.bittrex.com/api/v1.1/public/getticker?market=USD-USDT"
        j_USDT = requests.get(url_USDT)
        data_USDT = json.loads(j_USDT.text)
        price_USDT = data_USDT['result']['Ask']

        url_ETH = f"https://api.bittrex.com/api/v1.1/public/getticker?market=USD-ETH"
        j_ETH = requests.get(url_ETH)
        data_ETH = json.loads(j_ETH.text)
        price_ETH = data_ETH['result']['Ask']

        url_DAI = f"https://api.bittrex.com/api/v1.1/public/getticker?market=USD-DAI"
        j_DAI = requests.get(url_DAI)
        data_DAI = json.loads(j_DAI.text)
        price_DAI = data_DAI['result']['Ask']

        url_USDC = f"https://api.bittrex.com/api/v1.1/public/getticker?market=USD-USDC"
        j_USDC = requests.get(url_USDC)
        data_USDC = json.loads(j_USDC.text)
        price_USDC = data_USDC['result']['Ask']

        cryptos = {
            "BTC": price_BTC,
            "USDT": price_USDT,
            "ETH": price_ETH,
            "DAI": price_DAI,
            "USDC": price_USDC
        }

        await commands.update_crypto(1, cryptos["BTC"], "BTC")
        await commands.update_crypto(2, cryptos["USDT"], "USDT")
        await commands.update_crypto(3, cryptos["ETH"], "ETH")
        await commands.update_crypto(4, cryptos["DAI"], "DAI")
        await commands.update_crypto(5, cryptos["USDC"], "USDC")

        # await commands.add_crypto(1, cryptos["BTC"], "BTC")
        # await commands.add_crypto(2, cryptos["USDT"], "USDT")
        # await commands.add_crypto(3, cryptos["ETH"], "ETH")
        # await commands.add_crypto(4, cryptos["DAI"], "DAI")
        # await commands.add_crypto(5, cryptos["USDC"], "USDC")