import asyncio

from data import config
from utils.db_api import quick_commands as commands


async def hour_earning():
    while True:
        await asyncio.sleep(3600)

        users = await commands.select_all_users()

        crypto_BTC = await commands.select_crypto_by_name("BTC")
        crypto_ETH = await commands.select_crypto_by_name("ETH")
        crypto_USDT = await commands.select_crypto_by_name("USDT")
        crypto_USDC = await commands.select_crypto_by_name("USDC")
        crypto_DAI = await commands.select_crypto_by_name("DAI")

        for user in users:
            await commands.add_earn_user(user.id, user.earn + user.earn_easy)
            await commands.add_earn1_user(user.id, 0)

            if user.BTC_balance > 0 and user.BTC_hours < 24:
                new_btc_balance = user.BTC_balance_Z + (user.BTC_balance * config.BTC_PROCENT) / 24

                await commands.add_to_crypto_balance_btcz(user.id, new_btc_balance)
                await commands.add_to_crypto_hours_btc(user.id, user.BTC_hours + 1)

                await commands.add_earn1_user(user.id, (user.BTC_balance * config.BTC_PROCENT) / 24 * crypto_BTC.price)

            if user.ETH_balance > 0 and user.ETH_hours < 24:
                new_eth_balance = user.ETH_balance_Z + (user.ETH_balance * config.ETH_PROCENT) / 24

                await commands.add_to_crypto_balance_ethz(user.id, new_eth_balance)
                await commands.add_to_crypto_hours_eth(user.id, user.ETH_hours + 1)

                await commands.add_earn1_user(user.id, (user.ETH_balance * config.ETH_PROCENT) / 24 * crypto_ETH.price)

            if user.USDT_balance > 0 and user.USDT_hours < 24:
                new_usdt_balance = user.USDT_balance_Z + (user.USDT_balance * config.USDT_PROCENT) / 24

                await commands.add_to_crypto_balance_usdtz(user.id, new_usdt_balance)
                await commands.add_to_crypto_hours_usdt(user.id, user.USDT_hours + 1)

                await commands.add_earn1_user(user.id, (user.USDT_balance * config.USDT_PROCENT) / 24 * crypto_USDT.price)

            if user.USDC_balance > 0 and user.USDC_hours < 24:
                new_usdc_balance = user.USDC_balance_Z + (user.USDC_balance * config.USDC_PROCENT) / 24

                await commands.add_to_crypto_balance_usdcz(user.id, new_usdc_balance)
                await commands.add_to_crypto_hours_usdc(user.id, user.USDC_hours + 1)

                await commands.add_earn1_user(user.id, (user.USDC_balance * config.USDC_PROCENT) / 24 * crypto_USDC.price)

            if user.DAI_balance > 0 and user.DAI_hours < 24:
                new_dai_balance = user.DAI_balance_Z + (user.DAI_balance * config.DAI_PROCENT) / 24

                await commands.add_to_crypto_balance_daiz(user.id, new_dai_balance)
                await commands.add_to_crypto_hours_dai(user.id, user.DAI_hours + 1)

                await commands.add_earn1_user(user.id, (user.DAI_balance * config.DAI_PROCENT) / 24 * crypto_DAI.price)

            if user.ETH_hours >= 24:
                await commands.add_to_crypto_hours_eth(user.id, 0)
                await commands.delete_crypto_user(user.id, "ETH")

                await commands.add_withdraw(user.id, - user.ETH_balance * crypto_ETH.price)

                await commands.add_balance(user.id, user.ETH_balance_Z * crypto_ETH.price)
                await commands.add_to_crypto_balance_ethz(user.id, 0)
                await commands.add_to_crypto_balance_eth(user.id, 0)

            if user.BTC_hours >= 24:
                await commands.add_to_crypto_hours_btc(user.id, 0)
                await commands.delete_crypto_user(user.id, "BTC")

                await commands.add_withdraw(user.id, - user.BTC_balance * crypto_BTC.price)

                await commands.add_balance(user.id, user.BTC_balance_Z * crypto_BTC.price)
                await commands.add_to_crypto_balance_btcz(user.id, 0)
                await commands.add_to_crypto_balance_btc(user.id, 0)

            if user.USDT_hours >= 24:
                await commands.add_to_crypto_hours_usdt(user.id, 0)
                await commands.delete_crypto_user(user.id, "USDT")

                await commands.add_withdraw(user.id, - user.USDT_balance * crypto_USDT.price)

                await commands.add_balance(user.id, user.USDT_balance_Z * crypto_USDT.price)
                await commands.add_to_crypto_balance_usdtz(user.id, 0)
                await commands.add_to_crypto_balance_usdt(user.id, 0)

            if user.USDC_hours >= 24:
                await commands.add_to_crypto_hours_usdc(user.id, 0)
                await commands.delete_crypto_user(user.id, "USDC")

                await commands.add_withdraw(user.id, - user.USDC_balance * crypto_USDC.price)

                await commands.add_balance(user.id, user.USDC_balance_Z * crypto_USDC.price)
                await commands.add_to_crypto_balance_usdcz(user.id, 0)
                await commands.add_to_crypto_balance_usdc(user.id, 0)

            if user.DAI_hours >= 24:
                await commands.add_to_crypto_hours_dai(user.id, 0)
                await commands.delete_crypto_user(user.id, "DAI")

                await commands.add_withdraw(user.id, - user.DAI_balance * crypto_DAI.price)

                await commands.add_balance(user.id, user.DAI_balance_Z * crypto_DAI.price)
                await commands.add_to_crypto_balance_daiz(user.id, 0)
                await commands.add_to_crypto_balance_dai(user.id, 0)