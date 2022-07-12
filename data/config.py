import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
PGUSER = str(os.getenv("PGUSER"))
PGPASSWORD = str(os.getenv("PGPASSWORD"))
DATABASE = str(os.getenv("DATABASE"))

admins = [
    1644708646
]

BLOCKCYPHER_TOKEN = os.getenv("BLOCKCYPHER")
WALLET_BTC = os.getenv("wallet")
REQUEST_LINK = "bitcoin:{address}?" \
               "amount={amount}" \
               "&label={message}"

BTC_PROCENT = int(os.getenv("BTC_PROCENT"))
USDT_PROCENT = int(os.getenv("USDT_PROCENT"))
ETH_PROCENT = int(os.getenv("ETH_PROCENT"))
MCR_PROCENT = int(os.getenv("MCR_PROCENT"))
USDC_PROCENT = int(os.getenv("USDC_PROCENT"))
DAI_PROCENT = int(os.getenv("DAI_PROCENT"))

PROCENTS = {
    "BTC": BTC_PROCENT,
    "USDT": USDT_PROCENT,
    "ETH": ETH_PROCENT,
    "MCR": MCR_PROCENT,
    "USDC": USDC_PROCENT,
    "DAI": DAI_PROCENT,
}

ip = os.getenv("ip")

db_host = ip  # Если вы запускаете базу не через докер!
# db_host = "db"  # Если вы запускаете базу через докер и у вас в services стоит название базы db

aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}


POSTGRES_URI = f"postgresql://{PGUSER}:{PGPASSWORD}@{db_host}/{DATABASE}"
