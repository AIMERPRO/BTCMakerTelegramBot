from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.schemas.Crypto import Crypto
from utils.db_api.schemas.user import User


async def add_user(id: int, name, balance, withdraw, earn, lang, referral, verification, cryptos, BTC_balance, ETH_balance, USDT_balance, USDC_balance, DAI_balance):
    try:
        user = User(id=id, name=name, balance=balance, withdraw=withdraw, earn=earn, lang=lang, referral=referral, verification=verification, cryptos=cryptos,
                    BTC_balance=BTC_balance, ETH_balance=ETH_balance, USDT_balance=USDT_balance, USDC_balance=USDC_balance, DAI_balance=DAI_balance,
                    BTC_balance_Z=0, ETH_balance_Z=0, USDT_balance_Z=0, USDC_balance_Z=0, DAI_balance_Z=0,
                    BTC_hours=0, ETH_hours=0, USDT_hours=0, USDC_hours=0, DAI_hours=0, earn_easy=0)
        await user.create()

    except UniqueViolationError:
        pass


async def add_user_test(id: int, name):
    try:
        user = User(id=id, name=name)
        await user.create()

    except UniqueViolationError:
        pass


async def select_all_users():
    users = await User.query.gino.all()
    return users


async def select_user(id: int):
    user = await User.query.where(User.id == id).gino.first()
    return user


async def count_users():
    total = await db.func.count(User.id).gino.scalar()
    return total


async def update_user_referral(id, referral):
    user = await User.get(id)
    await user.update(referral=referral).apply()


async def add_balance(id, cash):
    user = await User.get(id)
    new_balance = user.balance + cash

    await user.update(balance=new_balance).apply()


async def add_withdraw(id, cash):
    user = await User.get(id)
    new_balance = user.withdraw + cash

    await user.update(withdraw=new_balance).apply()


async def edit_Lang(id, lang):
    user = await User.get(id)

    await user.update(lang=lang).apply()


async def set_withdraw(id, cash):
    user = await User.get(id)
    new_balance = user.withdraw + cash

    await user.update(withdraw=new_balance).apply()


async def deduct_balance(id, cash):
    user = await User.get(id)
    new_balance = user.balance - cash

    await user.update(balance=new_balance).apply()


async def add_crypto(id, price, name):
    try:
        crypto = Crypto(id=id, price=price, name=name)
        await crypto.create()

    except UniqueViolationError:
        pass


async def update_crypto(id, price, name):
    crypto = await Crypto.get(id)
    await crypto.update(price=price).apply()


async def select_all_crypto():
    crypto = await Crypto.query.gino.all()
    return crypto


async def select_crypto_by_name(name):
    crypto = await Crypto.query.where(Crypto.name == name).gino.first()
    return crypto


async def add_crypto_to_user(id, crypto_name):
    user = await User.get(id)
    new_crypto = user.cryptos + crypto_name + ","

    await user.update(cryptos=new_crypto).apply()


async def delete_crypto_user(id, crypto_name):
    user = await User.get(id)
    new_crypto = user.cryptos.replace(crypto_name + ",", " ")
    new_crypto = "".join(new_crypto.split())

    await user.update(cryptos=new_crypto).apply()


async def add_to_crypto_balance_btc(id, balance):
    user = await User.get(id)

    await user.update(BTC_balance=balance).apply()


async def add_earn_user(id, cash):
    user = await User.get(id)

    await user.update(earn=cash).apply()


async def add_earn1_user(id, cash):
    user = await User.get(id)

    await user.update(earn_easy=cash).apply()


async def add_withdraw_user(id, cash):
    user = await User.get(id)

    await user.update(withdraw=cash).apply()


async def add_to_crypto_balance_eth(id, balance):
    user = await User.get(id)

    await user.update(ETH_balance=balance).apply()


async def add_to_crypto_balance_usdc(id, balance):
    user = await User.get(id)

    await user.update(USDC_balance=balance).apply()


async def add_to_crypto_balance_usdt(id, balance):
    user = await User.get(id)

    await user.update(USDT_balance=balance).apply()


async def add_to_crypto_balance_dai(id, balance):
    user = await User.get(id)

    await user.update(DAI_balance=balance).apply()


async def add_to_crypto_balance_btcz(id, balance):
    user = await User.get(id)

    await user.update(BTC_balance_Z=balance).apply()


async def add_to_crypto_balance_ethz(id, balance):
    user = await User.get(id)

    await user.update(ETH_balance_Z=balance).apply()


async def add_to_crypto_balance_usdcz(id, balance):
    user = await User.get(id)

    await user.update(USDC_balance_Z=balance).apply()


async def add_to_crypto_balance_usdtz(id, balance):
    user = await User.get(id)

    await user.update(USDT_balance_Z=balance).apply()


async def add_to_crypto_balance_daiz(id, balance):
    user = await User.get(id)

    await user.update(DAI_balance_Z=balance).apply()


async def add_to_crypto_hours_btc(id, hours):
    user = await User.get(id)

    await user.update(BTC_hours=hours).apply()


async def add_to_crypto_hours_eth(id, hours):
    user = await User.get(id)

    await user.update(ETH_hours=hours).apply()


async def add_to_crypto_hours_usdc(id, hours):
    user = await User.get(id)

    await user.update(USDC_hours=hours).apply()


async def add_to_crypto_hours_usdt(id, hours):
    user = await User.get(id)

    await user.update(USDT_hours=hours).apply()


async def add_to_crypto_hours_dai(id, hours):
    user = await User.get(id)

    await user.update(DAI_hours=hours).apply()