from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

balance_inline = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text="Пополнение", callback_data="add_money"),
            InlineKeyboardButton(text="Вывод", callback_data="withdraw_money"),
        ],
        [
            InlineKeyboardButton(text="Активные займы", callback_data="active_payments")
        ],
        [
            InlineKeyboardButton(text="Назад в меню", callback_data="back_to_menu")
        ],
    ]
)

balance_inline_eng = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text="Deposit", callback_data="add_money"),
            InlineKeyboardButton(text="Withdraw", callback_data="withdraw_money"),
        ],
        [
            InlineKeyboardButton(text="Active loans", callback_data="active_payments")
        ],
        [
            InlineKeyboardButton(text="Back To The Menu", callback_data="back_to_menu")
        ],
    ]
)

balance_inline_esp = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text="Depositar", callback_data="add_money"),
            InlineKeyboardButton(text="Retirar", callback_data="withdraw_money"),
        ],
        [
            InlineKeyboardButton(text="Préstamos Activos", callback_data="active_payments")
        ],
        [
            InlineKeyboardButton(text="Volver al Menú", callback_data="back_to_menu")
        ],
    ]
)

balance_inline_port = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text="Depósito", callback_data="add_money"),
            InlineKeyboardButton(text="Retirada", callback_data="withdraw_money"),
        ],
        [
            InlineKeyboardButton(text="Empréstimos ativos", callback_data="active_payments")
        ],
        [
            InlineKeyboardButton(text="Voltar ao Menu", callback_data="back_to_menu")
        ],
    ]
)


paid_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Paid", callback_data="paid")
        ],
        [
            InlineKeyboardButton(
                text="Cancel", callback_data="cancel")
        ],
    ]
)

service_inline_eng = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text="Back To The Menu", callback_data="back_to_menu")
        ],
    ]
)

service_inline_esp = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text="Volver al Menú", callback_data="back_to_menu")
        ],
    ]
)

service_inline_port = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text="Voltar ao Menu", callback_data="back_to_menu")
        ],
    ]
)

settings_inline_eng = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text="Change The Language", callback_data="change_lang")
        ],
        [
            InlineKeyboardButton(text="Back To The Menu", callback_data="back_to_menu")
        ]
    ]
)

settings_inline_esp = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text="Cambia el idioma", callback_data="change_lang")
        ],
        [
            InlineKeyboardButton(text="Volver al Menú", callback_data="back_to_menu")
        ]
    ]
)

settings_inline_port = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text="Alterar o idioma", callback_data="change_lang")
        ],
        [
            InlineKeyboardButton(text="Voltar ao Menu", callback_data="back_to_menu")
        ]
    ]
)

settings_lang_inline = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text="English", callback_data="eng_lang"),
            InlineKeyboardButton(text="Español", callback_data="esp_lang"),
            InlineKeyboardButton(text="Português", callback_data="prt_lang")
        ],
        [
            InlineKeyboardButton(text="Back To The Menu", callback_data="back_to_menu")
        ]
    ]
)

calculator_inline = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text="BTC", callback_data="btc_calc"),
        ],
        [
            InlineKeyboardButton(text="USDT", callback_data="usdt_calc"),
        ],
        [
            InlineKeyboardButton(text="ETH", callback_data="eth_calc"),
        ],
        [
            InlineKeyboardButton(text="USDC", callback_data="usdc_calc"),
        ],
        [
            InlineKeyboardButton(text="DAI", callback_data="dai_calc"),
        ],
        [
            InlineKeyboardButton(text="Back To The Menu", callback_data="back_to_menu")
        ]
    ]
)


def crypto_list_inline(cryptos):
    crypto_inline = InlineKeyboardMarkup()

    for crypto in cryptos:
        crypto_inline.add(InlineKeyboardButton(text=crypto, callback_data=f"{crypto}_payment"))

    crypto_inline.add(InlineKeyboardButton(text="Back To The Menu", callback_data="back_to_menu"))

    return crypto_inline