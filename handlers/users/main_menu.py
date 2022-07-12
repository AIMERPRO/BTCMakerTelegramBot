import pyqrcode
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.markdown import hlink, hcode
from blockcypher import from_base_unit

from data import config
from keyboards.default.mainKBS import menu_keyboard_eng, menu_keyboard_esp, menu_keyboard_port
from keyboards.inline.main_INL_KBS import balance_inline, settings_lang_inline, \
    calculator_inline, crypto_list_inline, paid_keyboard, balance_inline_eng, balance_inline_esp, service_inline_eng, \
    service_inline_esp, service_inline_port, settings_inline_eng, settings_inline_esp, settings_inline_port, \
    balance_inline_port
from langs.LANG_TABLE import verif_text, verif_text1, back_to_menu_text, not_enough_money_text, start_invest_text, \
    active_invest_text, withdraw_funds_text, currency_earn_text, how_much_USD, active_loans_text
from loader import dp, bot
from states.AllStates import MainStates
from utils.db_api import quick_commands as commands
from utils.misc.bitcoin_payments import Payment, NotConfirmed, NoPaymentFound


@dp.message_handler(text="Wallet", state=MainStates.main_menu)
async def balance(message: types.Message, state: FSMContext):
    user = await commands.select_user(message.from_user.id)

    await state.update_data(menu=menu_keyboard_eng)

    link = hlink("Yes" if user.verification else "No", 't.me/CryptoMoneyBotSupport')

    await message.answer(f"Your ID: {user.id} \n"
                         f"\n"
                         f"\n"
                         f"Your Balance: {float('{:.3f}'.format(user.balance))} USD\n"
                         f"\n"
                         f"Issued: {user.withdraw} \n"
                         f"\n"
                         f"\n"
                         f"\n"
                         f"Earned: {float('{:.3f}'.format(user.earn))} USD"
                         f"\n"
                         f"\n"
                         f"\n"
                         f"Your referals: {user.referral} \n"
                         f"\n"
                         f"\n"
                         f"\n"
                         f"\n"
                         f"\n"
                         f"\n"
                         f"Verification: {link}                                                                       .",
                         reply_markup=balance_inline_eng)

    await state.update_data(id=message.from_user.id)

    await MainStates.balance.set()


@dp.message_handler(text="Billetera", state=MainStates.main_menu)
async def balance(message: types.Message, state: FSMContext):
    user = await commands.select_user(message.from_user.id)

    await state.update_data(menu=menu_keyboard_esp)

    link = hlink("Si" if user.verification else "No", 't.me/CryptoMoneyBotSupport')

    await message.answer(f"Tu ID: {user.id} \n"
                         f"\n"
                         f"\n"
                         f"Tu Balance: {float('{:.3f}'.format(user.balance))} USD\n"
                         f"\n"
                         f"Emitido: {user.withdraw} \n"
                         f"\n"
                         f"\n"
                         f"\n"
                         f"Ganado: {float('{:.3f}'.format(user.earn))} USD"
                         f"\n"
                         f"\n"
                         f"\n"
                         f"Tus referidos: {user.referral} \n"
                         f"\n"
                         f"\n"
                         f"\n"
                         f"\n"
                         f"\n"
                         f"\n"
                         f"Verificación: {link}                                                                       .",
                         reply_markup=balance_inline_esp)

    await state.update_data(id=message.from_user.id)

    await MainStates.balance.set()


@dp.message_handler(text="Carteira", state=MainStates.main_menu)
async def balance(message: types.Message, state: FSMContext):
    user = await commands.select_user(message.from_user.id)

    await state.update_data(menu=menu_keyboard_port)

    link = hlink("Sim" if user.verification else "Nao", 't.me/CryptoMoneyBotSupport')

    await message.answer(f"Sua ID: {user.id} \n"
                         f"\n"
                         f"\n"
                         f"Seu Balanço: {float('{:.3f}'.format(user.balance))} USD\n"
                         f"\n"
                         f"Emitido: {user.withdraw} \n"
                         f"\n"
                         f"\n"
                         f"\n"
                         f"Ganhou: {float('{:.3f}'.format(user.earn))} USD"
                         f"\n"
                         f"\n"
                         f"\n"
                         f"Suas referências:: {user.referral} \n"
                         f"\n"
                         f"\n"
                         f"\n"
                         f"\n"
                         f"\n"
                         f"\n"
                         f"Verificação: {link}                                                                       .",
                         reply_markup=balance_inline_port)

    await state.update_data(id=message.from_user.id)

    await MainStates.balance.set()


@dp.callback_query_handler(text="withdraw_money", state=MainStates.balance)
async def create_invoice(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=5)

    data = await state.get_data()

    user = await commands.select_user(data['id'])

    if not user.verification:
        await call.message.answer(f"{verif_text[f'{user.lang}']}", reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text=f"{verif_text1[f'{user.lang}']}", url="t.me/CryptoMoneyBotSupport")
                ],
                [
                    InlineKeyboardButton(text=f"{back_to_menu_text[f'{user.lang}']}", callback_data="back_to_menu")
                ]
            ]
        ))

        await call.message.delete()

    elif 0 <= user.balance <= 100:
        await call.message.answer(f"{not_enough_money_text[f'{user.lang}']}", reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text=f"{start_invest_text[f'{user.lang}']}", callback_data="start_invest")
                ],
                [
                    InlineKeyboardButton(text=f"{active_invest_text[f'{user.lang}']}", callback_data="active_payments")
                ],
                [
                    InlineKeyboardButton(text=f"{back_to_menu_text[f'{user.lang}']}", callback_data="back_to_menu")
                ]
            ]
        ))

        await call.message.delete()

    else:
        await call.message.answer(f"{withdraw_funds_text[f'{user.lang}']}", reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text=f"{withdraw_funds_text[f'{user.lang}']}", url="t.me/CryptoMoneyBotSupport")
                ],
                [
                    InlineKeyboardButton(text=f"{back_to_menu_text[f'{user.lang}']}", callback_data="back_to_menu")
                ]
            ]
        ))

        await call.message.delete()


@dp.callback_query_handler(text="start_invest", state=MainStates.balance)
async def calculator(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=15)
    data = await state.get_data()

    user = await commands.select_user(data['id'])

    await call.message.answer(f"{currency_earn_text[f'{user.lang}']}", reply_markup=calculator_inline)

    await state.update_data(earnMoney=True)

    await call.message.delete()

    await MainStates.calculator.set()


@dp.callback_query_handler(text="active_payments", state=MainStates.balance)
async def back_to_menu(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=15)

    data = await state.get_data()

    user = await commands.select_user(data['id'])
    cryptos = user.cryptos.split(",")[0:-1]

    await call.message.answer(f"{active_invest_text[f'{user.lang}']}", reply_markup=crypto_list_inline(cryptos))

    await call.message.delete()

    await MainStates.payments.set()


@dp.callback_query_handler(text="add_money", state=MainStates.balance)
async def create_invoice(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)

    data = await state.get_data()

    user = await commands.select_user(data['id'])

    await call.message.answer(f"{how_much_USD[f'{user.lang}']}", reply_markup=InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=f"{back_to_menu_text[f'{user.lang}']}", callback_data="back_to_menu")
            ]
        ]
    ))

    await state.set_state("add_money_add")

    await call.message.delete()


@dp.message_handler(state="add_money_add")
async def create_invoice(message: types.Message, state: FSMContext):
    data = await state.get_data()

    await state.update_data(money_add=float(message.text))

    show_amount = float(message.text)

    payment = Payment(amount=show_amount)
    payment.create()

    await message.answer(f"Pay {show_amount} on this USDT wallet:\n\n" +
                              hcode(config.WALLET_BTC),
                              reply_markup=paid_keyboard)

    await state.set_state("btc")
    await state.update_data(payment=payment)


@dp.callback_query_handler(text="cancel", state="btc")
async def cancel_payment(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=15)

    data = await state.get_data()

    await call.message.answer("Canceled", reply_markup=data['menu'])

    data = await state.get_data()

    await bot.delete_message(chat_id=data["id"], message_id=call.message.message_id - 2)
    await bot.delete_message(chat_id=data["id"], message_id=call.message.message_id + 1)

    await MainStates.main_menu.set()

    await call.message.delete()


@dp.callback_query_handler(text="paid", state="btc")
async def approve_payment(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=15)

    data = await state.get_data()
    user = await commands.select_user(data['id'])

    await bot.send_message(chat_id=config.admins[0], text=  f"Пользователь с id: {user.id} \n"
                                                            f"Оплатил: {data['money_add']} \n"
                                                            f"\n"
                                                            f"Проверьте оплату и нажмите на одну из кнопок", reply_markup=InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Пользователь оплатил", callback_data=f"user_paid_{user.id}_{data['money_add']}"),
                InlineKeyboardButton(text="Пользователь не оплатил", callback_data="user_not_pay"),
            ]
        ]
    ))

    if user.lang == "ENG":
        await call.message.answer("Soon technical support will check the payment and confirm its completion", reply_markup=menu_keyboard_eng)

    if user.lang == "ESP":
        await call.message.answer("Pronto el soporte técnico verificará el pago y confirmará su finalización", reply_markup=menu_keyboard_esp)

    if user.lang == "PORT":
        await call.message.answer("Em breve o suporte técnico irá verificar o pagamento e confirmar o seu preenchimento", reply_markup=menu_keyboard_port)

    await call.message.delete()

    await MainStates.main_menu.set()


@dp.callback_query_handler(text_contains="user_paid_", state="*")
async def approve_payment(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=15)

    callback = call.data.split("_")

    user = await commands.select_user(int(callback[2]))
    await commands.add_balance(user.id, float(callback[3]))

    await bot.send_message(chat_id=user.id, text=f"Your account has been credited to {callback[3]} USD")

    await call.message.delete()

    await MainStates.main_menu.set()


@dp.callback_query_handler(text="back_to_menu", state="*")
async def back_to_menu(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=15)

    data = await state.get_data()

    await call.message.answer("Menu", reply_markup=data['menu'])
    await call.message.delete()

    await MainStates.main_menu.set()


@dp.callback_query_handler(text="active_payments", state=MainStates.balance)
async def back_to_menu(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=15)

    data = await state.get_data()

    user = await commands.select_user(data['id'])
    cryptos = user.cryptos.split(",")[0:-1]

    await call.message.answer(f"{active_invest_text[f'{user.lang}']}", reply_markup=crypto_list_inline(cryptos))

    await call.message.delete()

    await MainStates.payments.set()


@dp.message_handler(text="About Service", state=MainStates.main_menu)
async def service(message: types.Message, state: FSMContext):
    await message.answer("Text......................\n"
                         "\n"
                         "\n"
                         "\n"
                         "\n"
                         "\n"
                         "\n"
                         "\n"
                         "............................", reply_markup=service_inline_eng)

    await state.update_data(id=message.from_user.id)

    await MainStates.service.set()


@dp.message_handler(text="Sobre el servicio", state=MainStates.main_menu)
async def service(message: types.Message, state: FSMContext):
    await message.answer("Text......................\n"
                         "\n"
                         "\n"
                         "\n"
                         "\n"
                         "\n"
                         "\n"
                         "\n"
                         "............................", reply_markup=service_inline_esp)

    await state.update_data(id=message.from_user.id)

    await MainStates.service.set()


@dp.message_handler(text="Sobre o serviço", state=MainStates.main_menu)
async def service(message: types.Message, state: FSMContext):
    await message.answer("Text......................\n"
                         "\n"
                         "\n"
                         "\n"
                         "\n"
                         "\n"
                         "\n"
                         "\n"
                         "............................", reply_markup=service_inline_port)

    await state.update_data(id=message.from_user.id)

    await MainStates.service.set()


@dp.message_handler(text="Settings", state=MainStates.main_menu)
async def settings(message: types.Message, state: FSMContext):
    cryptos = await commands.select_all_crypto()

    prices = {}
    for crypto in cryptos:
        price = {crypto.name: str(crypto.price)}
        prices.update(price)

    await message.answer(f"BTC/USD = {prices['BTC']} \n"
                         f"ETH/USD = {prices['ETH']} \n"
                         f"USDT/USD = {prices['USDT']} \n"
                         f"DAI/USD = {prices['DAI']}"
                         , reply_markup=settings_inline_eng)

    await state.update_data(id=message.from_user.id)

    await MainStates.settings.set()


@dp.message_handler(text="Ajustes", state=MainStates.main_menu)
async def settings(message: types.Message, state: FSMContext):
    cryptos = await commands.select_all_crypto()

    prices = {}
    for crypto in cryptos:
        price = {crypto.name: str(crypto.price)}
        prices.update(price)

    await message.answer(f"BTC/USD = {prices['BTC']} \n"
                         f"ETH/USD = {prices['ETH']} \n"
                         f"USDT/USD = {prices['USDT']} \n"
                         f"DAI/USD = {prices['DAI']}"
                         , reply_markup=settings_inline_esp)

    await state.update_data(id=message.from_user.id)

    await MainStates.settings.set()


@dp.message_handler(text="Configurações", state=MainStates.main_menu)
async def settings(message: types.Message, state: FSMContext):
    cryptos = await commands.select_all_crypto()

    prices = {}
    for crypto in cryptos:
        price = {crypto.name: str(crypto.price)}
        prices.update(price)

    await message.answer(f"BTC/USD = {prices['BTC']} \n"
                         f"ETH/USD = {prices['ETH']} \n"
                         f"USDT/USD = {prices['USDT']} \n"
                         f"DAI/USD = {prices['DAI']}"
                         , reply_markup=settings_inline_port)

    await state.update_data(id=message.from_user.id)

    await MainStates.settings.set()


@dp.callback_query_handler(text="change_lang", state=MainStates.settings)
async def settings_lang(call: types.CallbackQuery):
    await call.answer(cache_time=15)

    await call.message.answer("Choose language", reply_markup=settings_lang_inline)
    await call.message.delete()

    await MainStates.settings_lang.set()


@dp.callback_query_handler(text="eng_lang", state=MainStates.settings_lang)
async def settings_lang(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=15)

    data = await state.get_data()

    await commands.edit_Lang(data['id'], "ENG")

    await call.message.answer("You changed your language to English", reply_markup=menu_keyboard_eng)

    await call.message.delete()
    await MainStates.main_menu.set()


@dp.callback_query_handler(text="esp_lang", state=MainStates.settings_lang)
async def settings_lang(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=15)

    data = await state.get_data()

    await commands.edit_Lang(data['id'], "ESP")

    await call.message.answer("Cambiaste tu idioma al español", reply_markup=menu_keyboard_esp)

    await call.message.delete()
    await MainStates.main_menu.set()


@dp.callback_query_handler(text="port_lang", state=MainStates.settings_lang)
async def settings_lang(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=15)

    data = await state.get_data()

    await commands.edit_Lang(data['id'], "PORT")

    await call.message.answer("Voce mudou seu idioma para portugues", reply_markup=menu_keyboard_port)

    await call.message.delete()
    await MainStates.main_menu.set()


@dp.message_handler(text="Calculate", state=MainStates.main_menu)
async def calculator(message: types.Message, state: FSMContext):
    await message.answer("Choose what you would like to calculate", reply_markup=calculator_inline)

    await state.update_data(earnMoney=False)
    await state.update_data(id=message.from_user.id)

    await MainStates.calculator.set()


@dp.message_handler(text="Calcular", state=MainStates.main_menu)
async def calculator(message: types.Message, state: FSMContext):
    await message.answer("Elija lo que le gustaría calcular", reply_markup=calculator_inline)

    await state.update_data(earnMoney=False)
    await state.update_data(id=message.from_user.id)

    await MainStates.calculator.set()


@dp.message_handler(text="Calculadora", state=MainStates.main_menu)
async def calculator(message: types.Message, state: FSMContext):
    await message.answer("Escolha o que você quer contar", reply_markup=calculator_inline)

    await state.update_data(earnMoney=False)
    await state.update_data(id=message.from_user.id)

    await MainStates.calculator.set()


@dp.callback_query_handler(text="btc_calc", state=MainStates.calculator)
async def btc_calc(call: types.CallbackQuery):
    await call.answer(cache_time=15)

    await call.message.answer("Enter the amount:")
    await call.message.delete()

    await MainStates.btc_calc.set()


@dp.callback_query_handler(text="usdt_calc", state=MainStates.calculator)
async def btc_calc(call: types.CallbackQuery):
    await call.answer(cache_time=15)

    await call.message.answer("Enter the amount:")
    await call.message.delete()

    await MainStates.usdt_calc.set()


@dp.callback_query_handler(text="eth_calc", state=MainStates.calculator)
async def btc_calc(call: types.CallbackQuery):
    await call.answer(cache_time=15)

    await call.message.answer("Enter the amount:")
    await call.message.delete()

    await MainStates.eth_calc.set()


@dp.callback_query_handler(text="usdc_calc", state=MainStates.calculator)
async def btc_calc(call: types.CallbackQuery):
    await call.answer(cache_time=15)

    await call.message.answer("Enter the amount:")
    await call.message.delete()

    await MainStates.usdc_calc.set()


@dp.callback_query_handler(text="dai_calc", state=MainStates.calculator)
async def btc_calc(call: types.CallbackQuery):
    await call.answer(cache_time=15)

    await call.message.answer("Enter the amount:")
    await call.message.delete()

    await MainStates.dai_calc.set()


@dp.message_handler(state=MainStates.btc_calc)
async def btc_calc(message: types.Message, state: FSMContext):
    data = await state.get_data()

    await state.update_data(id=message.from_user.id)

    btc = await commands.select_crypto_by_name("BTC")

    if data["earnMoney"]:
        await message.answer(f"💸 Inscribed amount: {message.text} ({float(message.text) * btc.price} USD)\n"
                             f"📅 Term range: 24 hours\n"
                             f"📈 Interest rate: {config.BTC_PROCENT}x\n"
                             f"💵 Estimated income: {float(message.text) * config.BTC_PROCENT}",
                             reply_markup=InlineKeyboardMarkup(
                                 inline_keyboard=
                                 [
                                     [
                                         InlineKeyboardButton(text="All okay", callback_data="all_okay"),
                                         InlineKeyboardButton(text="Retry", callback_data="retry"),
                                     ],
                                     [
                                         InlineKeyboardButton(text="Back To The Menu", callback_data="back_to_menu")
                                     ]
                                 ]
                             ))

        await state.update_data(sum=float(message.text))
        await state.update_data(percent=int(config.BTC_PROCENT))
        await state.update_data(crypto="BTC")

        await MainStates.earn.set()

    else:
        await message.answer(f"💸 Inscribed amount: {message.text} ({float(message.text) * btc.price} USD)\n"
                             f"📅 Term range: 24 hours\n"
                             f"📈 Interest rate: {config.BTC_PROCENT}x\n"
                             f"💵 Estimated income: {float(message.text) * config.BTC_PROCENT}"
                             f"\n"
                             f"\n"
                             f"\n"
                             f"\n"
                             f"\n"
                             f"\n"
                             f"\n"
                             f"\n"
                             f"Ready to start making money?",
                             reply_markup=InlineKeyboardMarkup(
                                 inline_keyboard=
                                 [
                                     [
                                         InlineKeyboardButton(text="Earn BTC", callback_data="earn")
                                     ],
                                     [
                                         InlineKeyboardButton(text="Back To The Menu", callback_data="back_to_menu")
                                     ]
                                 ]
                             ))

        await state.update_data(sum=float(message.text))
        await state.update_data(percent=int(config.BTC_PROCENT))
        await state.update_data(crypto="BTC")


@dp.message_handler(state=MainStates.usdt_calc)
async def btc_calc(message: types.Message, state: FSMContext):
    data = await state.get_data()

    await state.update_data(id=message.from_user.id)

    usdt = await commands.select_crypto_by_name("USDT")

    if data["earnMoney"]:
        await message.answer(f"💸 Inscribed amount: {message.text} ({float(message.text) * usdt.price} USD)\n"
                             f"📅 Term range: 24 hours\n"
                             f"📈 Interest rate: {config.USDT_PROCENT}x\n"
                             f"💵 Estimated income: {float(message.text) * config.USDT_PROCENT}",
                             reply_markup=InlineKeyboardMarkup(
                                 inline_keyboard=
                                 [
                                     [
                                         InlineKeyboardButton(text="All okay", callback_data="all_okay"),
                                         InlineKeyboardButton(text="Retry", callback_data="retry"),
                                     ],
                                     [
                                         InlineKeyboardButton(text="Back To The Menu", callback_data="back_to_menu")
                                     ]
                                 ]
                             ))

        await state.update_data(sum=float(message.text))
        await state.update_data(percent=int(config.USDT_PROCENT))
        await state.update_data(crypto="USDT")

        await MainStates.earn.set()

    else:
        await message.answer(f"💸 Inscribed amount: {message.text} ({float(message.text) * usdt.price} USD)\n"
                             f"📅 Term range: 24 hours\n"
                             f"📈 Interest rate:  {config.USDT_PROCENT}x\n"
                             f"💵 Estimated income: {float(message.text) * config.USDT_PROCENT}"
                             f"\n"
                             f"\n"
                             f"\n"
                             f"\n"
                             f"\n"
                             f"\n"
                             f"\n"
                             f"\n"
                             f"Ready to start making money?",
                             reply_markup=InlineKeyboardMarkup(
                                 inline_keyboard=
                                 [
                                     [
                                         InlineKeyboardButton(text="Earn USDT", callback_data="earn")
                                     ],
                                     [
                                         InlineKeyboardButton(text="Back To The Menu", callback_data="back_to_menu")
                                     ]
                                 ]
                             ))

        await state.update_data(sum=float(message.text))
        await state.update_data(percent=int(config.USDT_PROCENT))
        await state.update_data(crypto="USDT")

        await MainStates.earn.set()


@dp.message_handler(state=MainStates.usdc_calc)
async def btc_calc(message: types.Message, state: FSMContext):
    data = await state.get_data()

    await state.update_data(id=message.from_user.id)

    usdc = await commands.select_crypto_by_name("USDC")

    if data["earnMoney"]:
        await message.answer(f"💸 Inscribed amount: {message.text} ({float(message.text) * usdc.price} USD)\n"
                             f"📅 Term range: 24 hours\n"
                             f"📈 Interest rate:  {config.USDC_PROCENT}x\n"
                             f"💵 Estimated income: {float(message.text) * config.USDC_PROCENT}",
                             reply_markup=InlineKeyboardMarkup(
                                 inline_keyboard=
                                 [
                                     [
                                         InlineKeyboardButton(text="All okay", callback_data="all_okay"),
                                         InlineKeyboardButton(text="Retry", callback_data="retry"),
                                     ],
                                     [
                                         InlineKeyboardButton(text="Back To The Menu", callback_data="back_to_menu")
                                     ]
                                 ]
                             ))

        await state.update_data(sum=float(message.text))
        await state.update_data(percent=int(config.USDC_PROCENT))
        await state.update_data(crypto="USDC")

        await MainStates.earn.set()

    else:
        await message.answer(f"💸 Inscribed amount: {message.text} ({float(message.text) * usdc.price} USD)\n"
                             f"📅 Term range: 24 hours\n"
                             f"📈 Interest rate: {config.USDC_PROCENT}x\n"
                             f"💵 Estimated income: {float(message.text) * config.USDC_PROCENT}"
                             f"\n"
                             f"\n"
                             f"\n"
                             f"\n"
                             f"\n"
                             f"\n"
                             f"\n"
                             f"\n"
                             f"Ready to start making money?",
                             reply_markup=InlineKeyboardMarkup(
                                 inline_keyboard=
                                 [
                                     [
                                         InlineKeyboardButton(text="Earn USDC", callback_data="earn")
                                     ],
                                     [
                                         InlineKeyboardButton(text="Back To The Menu", callback_data="back_to_menu")
                                     ]
                                 ]
                             ))

        await state.update_data(sum=float(message.text))
        await state.update_data(percent=int(config.USDC_PROCENT))
        await state.update_data(crypto="USDC")


@dp.message_handler(state=MainStates.eth_calc)
async def btc_calc(message: types.Message, state: FSMContext):
    data = await state.get_data()

    await state.update_data(id=message.from_user.id)

    eth = await commands.select_crypto_by_name("ETH")

    if data["earnMoney"]:
        await message.answer(f"💸 Inscribed amount: {message.text} ({float(message.text) * eth.price} USD)\n"
                             f"📅 Term range: 24 hours\n"
                             f"📈 Interest rate: {config.ETH_PROCENT}x\n"
                             f"💵 Estimated income: {float(message.text) * config.ETH_PROCENT}",
                             reply_markup=InlineKeyboardMarkup(
                                 inline_keyboard=
                                 [
                                     [
                                         InlineKeyboardButton(text="All okay", callback_data="all_okay"),
                                         InlineKeyboardButton(text="Retry", callback_data="retry"),
                                     ],
                                     [
                                         InlineKeyboardButton(text="Back To The Menu", callback_data="back_to_menu")
                                     ]
                                 ]
                             ))

        await state.update_data(sum=float(message.text))
        await state.update_data(percent=int(config.ETH_PROCENT))
        await state.update_data(crypto="ETH")

        await MainStates.earn.set()

    else:
        await message.answer(f"💸 Inscribed amount: {message.text} ({float(message.text) * eth.price} USD)\n"
                             f"📅 Term range: 24 hours\n"
                             f"📈 Interest rate: {config.ETH_PROCENT}x\n"
                             f"💵 Estimated income: {float(message.text) * config.ETH_PROCENT}"
                             f"\n"
                             f"\n"
                             f"\n"
                             f"\n"
                             f"\n"
                             f"\n"
                             f"\n"
                             f"\n"
                             f"Ready to start making money?",
                             reply_markup=InlineKeyboardMarkup(
                                 inline_keyboard=
                                 [
                                     [
                                         InlineKeyboardButton(text="Earn ETH", callback_data="earn")
                                     ],
                                     [
                                         InlineKeyboardButton(text="Back To The Menu", callback_data="back_to_menu")
                                     ]
                                 ]
                             ))

        await state.update_data(sum=float(message.text))
        await state.update_data(percent=int(config.ETH_PROCENT))
        await state.update_data(crypto="ETH")


@dp.message_handler(state=MainStates.dai_calc)
async def btc_calc(message: types.Message, state: FSMContext):
    data = await state.get_data()

    await state.update_data(id=message.from_user.id)
    dai = await commands.select_crypto_by_name("DAI")

    if data["earnMoney"]:
        await message.answer(f"💸 Inscribed amount: {message.text} ({float(message.text) * dai.price} USD)\n"
                             f"📅 Term range: 24 hours\n"
                             f"📈 Interest rate: {config.DAI_PROCENT}x\n"
                             f"💵 Estimated income: {float(message.text) * config.DAI_PROCENT} DAI",
                             reply_markup=InlineKeyboardMarkup(
                                 inline_keyboard=
                                 [
                                     [
                                         InlineKeyboardButton(text="All okay", callback_data="all_okay"),
                                         InlineKeyboardButton(text="Retry", callback_data="retry"),
                                     ],
                                     [
                                         InlineKeyboardButton(text="back To The Menu", callback_data="back_to_menu")
                                     ]
                                 ]
                             ))

        await state.update_data(sum=float(message.text))
        await state.update_data(percent=int(config.DAI_PROCENT))
        await state.update_data(crypto="DAI")

        await MainStates.earn.set()

    else:
        await message.answer(f"💸 Inscribed amount: {message.text} ({float(message.text) * dai.price} USD)\n"
                             f"📅 Term range: 24 hours\n"
                             f"📈 Interest rate: {config.DAI_PROCENT}x\n"
                             f"💵 Estimated income: {float(message.text) * config.DAI_PROCENT} DAI"
                             f"\n"
                             f"\n"
                             f"\n"
                             f"\n"
                             f"\n"
                             f"\n"
                             f"\n"
                             f"\n"
                             f"Ready to start making money?",
                             reply_markup=InlineKeyboardMarkup(
                                 inline_keyboard=
                                 [
                                     [
                                         InlineKeyboardButton(text="Earn DAI", callback_data="earn")
                                     ],
                                     [
                                         InlineKeyboardButton(text="Back To The Menu", callback_data="back_to_menu")
                                     ]
                                 ]
                             ))

        await state.update_data(sum=float(message.text))
        await state.update_data(percent=int(config.DAI_PROCENT))
        await state.update_data(crypto="DAI")


@dp.message_handler(text="Make money", state=MainStates.main_menu)
async def calculator(message: types.Message, state: FSMContext):
    await message.answer("Choose what currency you would like to earn", reply_markup=calculator_inline)

    await state.update_data(earnMoney=True)
    await state.update_data(id=message.from_user.id)

    await MainStates.calculator.set()


@dp.message_handler(text="Ganar dinero", state=MainStates.main_menu)
async def calculator(message: types.Message, state: FSMContext):
    await message.answer("Elija qué moneda le gustaría ganar", reply_markup=calculator_inline)

    await state.update_data(earnMoney=True)
    await state.update_data(id=message.from_user.id)

    await MainStates.calculator.set()


@dp.message_handler(text="Ganhe dinheiro", state=MainStates.main_menu)
async def calculator(message: types.Message, state: FSMContext):
    await message.answer("Escolha a moeda que você gostaria de ganhar", reply_markup=calculator_inline)

    await state.update_data(earnMoney=True)
    await state.update_data(id=message.from_user.id)

    await MainStates.calculator.set()


@dp.callback_query_handler(text="earn", state="*")
async def earn(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=15)

    data = await state.get_data()

    crypto = await commands.select_crypto_by_name(data['crypto'])

    await call.message.answer(f"💸 Inscribed amount: {data['sum']} ({data['sum'] * crypto.price} USD)\n"
                              f"📅 Term range: 24 hours\n"
                              f"📈 Interest rate: {config.PROCENTS[data['crypto']]}x\n"
                              f"💵 Estimated income: {data['sum'] * config.PROCENTS[data['crypto']]} {data['crypto']}",
                              reply_markup=InlineKeyboardMarkup(
                                  inline_keyboard=
                                  [
                                      [
                                          InlineKeyboardButton(text="All okay", callback_data="all_okay"),
                                          InlineKeyboardButton(text="Retry", callback_data="retry"),
                                      ],
                                      [
                                          InlineKeyboardButton(text="Back To The Menu", callback_data="back_to_menu")
                                      ]
                                  ]
                              ))

    await call.message.delete()

    await MainStates.earn.set()


@dp.callback_query_handler(text="retry", state=MainStates.earn)
async def back_to_menu(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=15)

    data = await state.get_data()
    user = await commands.select_user(data['id'])

    await call.message.answer(f"{currency_earn_text[f'{user.lang}']}", reply_markup=calculator_inline)

    await state.update_data(earnMoney=True)

    await call.message.delete()

    await MainStates.calculator.set()


@dp.callback_query_handler(text="all_okay", state=MainStates.earn)
async def back_to_menu(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=15)

    data = await state.get_data()

    user = await commands.select_user(data['id'])
    crypto = await commands.select_crypto_by_name(data['crypto'])

    if user.balance < data['sum'] * crypto.price:
        await call.message.answer(f"Not enough money, try decreasing the amount or top up account! \n"
                                  f"Your Balance USD: {float('{:.3f}'.format(user.balance))}",
                                  reply_markup=InlineKeyboardMarkup(
                                      inline_keyboard=
                                      [
                                          [
                                              InlineKeyboardButton("Wallet", callback_data="balance")
                                          ],
                                          [
                                              InlineKeyboardButton("Back To The Menu", callback_data="back_to_menu")
                                          ],
                                      ]
                                  ))

        await MainStates.not_enough_money.set()

    else:
        cryptos = user.cryptos.split(",")[0:-1]
        have_crypto = False

        for crypto1 in cryptos:
            if crypto1 == data['crypto']:
                have_crypto = True

        if not have_crypto:
            print(crypto.price)

            await commands.deduct_balance(user.id, data['sum'] * crypto.price)

            await call.message.answer(
                "Processing of your request has begun, your funds will start multiplying soon! You can "
                "see your active multiplications in the Active loans tab.",
                reply_markup=InlineKeyboardMarkup(
                    inline_keyboard=
                    [
                        [
                            InlineKeyboardButton("Active Loans", callback_data="active_payments")
                        ],
                        [
                            InlineKeyboardButton("Back To The Menu", callback_data="back_to_menu")
                        ],
                    ]
                ))

            await commands.add_crypto_to_user(user.id, data['crypto'])

            if data['crypto'] == "BTC":
                await commands.add_to_crypto_balance_btc(user.id, data['sum'])
                await commands.add_withdraw(user.id, data['sum'] * crypto.price)

            if data['crypto'] == "ETH":
                await commands.add_to_crypto_balance_eth(user.id, data['sum'])
                await commands.add_withdraw(user.id, data['sum'] * crypto.price)

            if data['crypto'] == "USDC":
                await commands.add_to_crypto_balance_usdc(user.id, data['sum'])
                await commands.add_withdraw(user.id, data['sum'] * crypto.price)

            if data['crypto'] == "USDT":
                await commands.add_to_crypto_balance_usdt(user.id, data['sum'])
                await commands.add_withdraw(user.id, data['sum'] * crypto.price)

            if data['crypto'] == "DAI":
                await commands.add_to_crypto_balance_dai(user.id, data['sum'])
                await commands.add_withdraw(user.id, data['sum'] * crypto.price)

        else:
            await call.message.answer("You already have this currency multiplied! You can "
                                      "see your active multiplications in the Active loans tab.",
                                      reply_markup=InlineKeyboardMarkup(
                                          inline_keyboard=
                                          [
                                              [
                                                  InlineKeyboardButton("Active Loans",
                                                                       callback_data="active_payments")
                                              ],
                                              [
                                                  InlineKeyboardButton("Back To The Menu", callback_data="back_to_menu")
                                              ],
                                          ]
                                      ))

    await state.update_data(earnMoney=True)

    await call.message.delete()


@dp.callback_query_handler(text="balance", state=MainStates.not_enough_money)
async def balance(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()

    user = await commands.select_user(data['id'])
    verif = "Да" if user.verification else "Нет"

    link = hlink(f'{verif}', 't.me/CryptoMoneyBotSupport')

    await call.message.answer(f"Your ID: {user.id} \n"
                              f"\n"
                              f"\n"
                              f"Your Balance: {float('{:.3f}'.format(user.balance))} USDT\n"
                              f"\n"
                              f"Issued: {user.withdraw} \n"
                              f"\n"
                              f"\n"
                              f"\n"
                              f"Earned: {float('{:.3f}'.format(user.earn))} USD"
                              f"\n"
                              f"\n"
                              f"\n"
                              f"Your referals: {user.referral} \n"
                              f"\n"
                              f"\n"
                              f"\n"
                              f"\n"
                              f"\n"
                              f"\n"
                              f"Verification: {link}                                                                       .",
                              reply_markup=balance_inline_eng)

    await call.message.delete()

    await MainStates.balance.set()


@dp.message_handler(text="Loans", state=MainStates.main_menu)
async def service(message: types.Message, state: FSMContext):
    await state.update_data(id=message.from_user.id)

    user = await commands.select_user(message.from_user.id)
    cryptos = user.cryptos.split(",")[0:-1]

    await message.answer("Your Active Loans", reply_markup=crypto_list_inline(cryptos))

    await MainStates.payments.set()


@dp.message_handler(text="Préstamos", state=MainStates.main_menu)
async def service(message: types.Message, state: FSMContext):
    await state.update_data(id=message.from_user.id)

    user = await commands.select_user(message.from_user.id)
    cryptos = user.cryptos.split(",")[0:-1]

    await message.answer("Tus préstamos activos", reply_markup=crypto_list_inline(cryptos))

    await MainStates.payments.set()


@dp.message_handler(text="Préstamos", state=MainStates.main_menu)
async def service(message: types.Message, state: FSMContext):
    await state.update_data(id=message.from_user.id)

    user = await commands.select_user(message.from_user.id)
    cryptos = user.cryptos.split(",")[0:-1]

    await message.answer("Seus empréstimos ativos", reply_markup=crypto_list_inline(cryptos))

    await MainStates.payments.set()


@dp.callback_query_handler(text="active_payments", state=MainStates.earn)
async def back_to_menu(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=15)

    data = await state.get_data()

    user = await commands.select_user(data['id'])
    cryptos = user.cryptos.split(",")[0:-1]

    await call.message.answer(f"{active_loans_text[f'{user.lang}']}", reply_markup=crypto_list_inline(cryptos))

    await call.message.delete()

    await MainStates.payments.set()


@dp.callback_query_handler(text="BTC_payment", state=MainStates.payments)
async def back_to_menu(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=15)

    data = await state.get_data()

    user = await commands.select_user(data['id'])

    await call.message.answer(f"📜 BTC\n"
                              f"\n"
                              f"💸 Sum: {user.BTC_balance} BTC \n"
                              f"📅 Term: 24 hours \n"
                              f"📈 Interest rate: {config.BTC_PROCENT}x \n"
                              f"💵 Earned: {float('{:.3f}'.format(user.BTC_balance_Z))} BTC",
                              reply_markup=InlineKeyboardMarkup(
                                          inline_keyboard=
                                          [
                                              [
                                                  InlineKeyboardButton("Back To The Menu", callback_data="back_to_menu")
                                              ],
                                          ]
                                      ))

    await call.message.delete()

    await MainStates.payments.set()


@dp.callback_query_handler(text="USDT_payment", state=MainStates.payments)
async def back_to_menu(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=15)

    data = await state.get_data()

    user = await commands.select_user(data['id'])

    await call.message.answer(f"📜 USDT\n"
                              f"\n"
                              f"💸 Sum: {user.USDT_balance} USDT \n"
                              f"📅 Term: 24 hours \n"
                              f"📈 Interest rate: {config.USDT_PROCENT}x \n"
                              f"💵 Earned: {float('{:.3f}'.format(user.USDT_balance_Z))} USDT",
                              reply_markup=InlineKeyboardMarkup(
                                  inline_keyboard=
                                  [
                                      [
                                          InlineKeyboardButton("Back To The Menu", callback_data="back_to_menu")
                                      ],
                                  ]
                              ))

    await call.message.delete()

    await MainStates.payments.set()


@dp.callback_query_handler(text="ETH_payment", state=MainStates.payments)
async def back_to_menu(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=15)

    data = await state.get_data()

    user = await commands.select_user(data['id'])

    await call.message.answer(f"📜 ETH\n"
                              f"\n"
                              f"💸 Sum: {user.ETH_balance} ETH \n"
                              f"📅 Term: 24 hours \n"
                              f"📈 Interest rate: {config.ETH_PROCENT}x \n"
                              f"💵 Earned: {float('{:.3f}'.format(user.ETH_balance_Z))} ETH",
                              reply_markup=InlineKeyboardMarkup(
                                  inline_keyboard=
                                  [
                                      [
                                          InlineKeyboardButton("Back To The Menu", callback_data="back_to_menu")
                                      ],
                                  ]
                              ))

    await call.message.delete()

    await MainStates.payments.set()


@dp.callback_query_handler(text="USDC_payment", state=MainStates.payments)
async def back_to_menu(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=15)

    data = await state.get_data()

    user = await commands.select_user(data['id'])

    await call.message.answer(f"📜 USDC\n"
                              f"\n"
                              f"💸 Sum: {user.USDC_balance} USDC \n"
                              f"📅 Term: 24 hours \n"
                              f"📈 Interest rate: {config.USDC_PROCENT}x \n"
                              f"💵 Earned: {float('{:.3f}'.format(user.USDC_balance_Z))} USDC",
                              reply_markup=InlineKeyboardMarkup(
                                  inline_keyboard=
                                  [
                                      [
                                          InlineKeyboardButton("Back To The Menu", callback_data="back_to_menu")
                                      ],
                                  ]
                              ))

    await call.message.delete()

    await MainStates.payments.set()


@dp.callback_query_handler(text="DAI_payment", state=MainStates.payments)
async def back_to_menu(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=15)

    data = await state.get_data()

    user = await commands.select_user(data['id'])

    await call.message.answer(f"📜 DAI\n"
                              f"\n"
                              f"💸 Sum: {user.DAI_balance} DAI \n"
                              f"📅 Term: 24 hours \n"
                              f"📈 Interest rate: {config.DAI_PROCENT}x \n"
                              f"💵 Earned: {float('{:.3f}'.format(user.DAI_balance_Z))} DAI",
                              reply_markup=InlineKeyboardMarkup(
                                  inline_keyboard=
                                  [
                                      [
                                          InlineKeyboardButton("Back To The Menu", callback_data="back_to_menu")
                                      ],
                                  ]
                              ))

    await call.message.delete()

    await MainStates.payments.set()