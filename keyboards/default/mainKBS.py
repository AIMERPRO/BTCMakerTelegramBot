from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

menu_keyboard_eng = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("Wallet"),
            KeyboardButton("Loans"),
        ],
        [
            KeyboardButton("About Service"),
            KeyboardButton("Settings"),
        ],
        [
            KeyboardButton("Calculate"),
            KeyboardButton("Make money"),
        ],
    ], resize_keyboard=True, one_time_keyboard=True
)


menu_keyboard_esp = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("Billetera"),
            KeyboardButton("Préstamos"),
        ],
        [
            KeyboardButton("Sobre el servicio"),
            KeyboardButton("Ajustes"),
        ],
        [
            KeyboardButton("Calcular"),
            KeyboardButton("Ganar dinero"),
        ],
    ], resize_keyboard=True, one_time_keyboard=True
)


menu_keyboard_port = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("Carteira"),
            KeyboardButton("Empréstimos"),
        ],
        [
            KeyboardButton("Sobre o serviço"),
            KeyboardButton("Configurações"),
        ],
        [
            KeyboardButton("Calculadora"),
            KeyboardButton("Ganhe dinheiro"),
        ],
    ], resize_keyboard=True, one_time_keyboard=True
)