from aiogram import types

def make_start_keyboard():
    buttons = [
        types.InlineKeyboardButton(text='Начать работу с ботом', callback_data='start_work'),
    ]

    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


def make_menu_keyboard():
    buttons = [
        types.InlineKeyboardButton(text='Создать\Обновить заметку', callback_data='create_note'),
        types.InlineKeyboardButton(text='Список заметок', callback_data='get_list_notes'),
        types.InlineKeyboardButton(text='Удалить заметку', callback_data='delete_note'),

    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


def make_cancel_keyboard():
    buttons = [
        types.InlineKeyboardButton(text='Отменить', callback_data='cancel'),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard