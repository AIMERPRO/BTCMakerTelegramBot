from aiogram.dispatcher.filters.state import StatesGroup, State


class MainStates(StatesGroup):
    main_menu = State()
    balance = State()
    service = State()
    settings = State()
    settings_lang = State()
    calculator = State()
    calculator1 = State()
    lang_choose = State()

    earn = State()

    btc_calc = State()
    usdt_calc = State()
    eth_calc = State()
    usdc_calc = State()
    dai_calc = State()

    payments = State()

    not_enough_money = State()
