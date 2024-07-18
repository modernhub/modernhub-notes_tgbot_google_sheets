from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

from tgbot.bot import bot
from tgbot.user_states import UserStates
from tgbot.default_messages import DEFAULT_MESSAGES
from tgbot.keyboards import menu_keyboard

from models import Note

from tables.exceptions import NoteNotFound


async def start_work(call: types.CallbackQuery, state: FSMContext):
    bot.connector.worksheets_editor.add_worksheet(call.from_user.id)
    await state.set_state(UserStates.default_state.state)
    await call.answer()
    await bot.send_message(
        chat_id=call.from_user.id,
        text=DEFAULT_MESSAGES.start_work(),
        reply_markup=menu_keyboard.make_menu_keyboard()
    )


async def create_note(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(UserStates.waiting_title_note.state)
    await call.answer()
    await bot.send_message(
        chat_id=call.from_user.id,
        text=DEFAULT_MESSAGES.wait_title_note(),
        reply_markup=menu_keyboard.make_cancel_keyboard()
    )


async def wait_title_note(msg_from: types.Message, state: FSMContext):
    await state.update_data(title_note=msg_from.text)
    await state.set_state(UserStates.waiting_data_note.state)
    await msg_from.answer(
        DEFAULT_MESSAGES.wait_data_note(),
        reply_markup=menu_keyboard.make_cancel_keyboard()
    )


async def wait_data_note(msg_from: types.Message, state: FSMContext):
    await state.update_data(data_note=msg_from.text)

    user_note = await state.get_data()
    note = Note(user_note['title_note'])
    note.set_data(user_note['data_note'])
    note.set_date_update_auto()

    await state.set_state(UserStates.default_state.state)
    is_created = bot.connector.set_note(note, worksheet_title=msg_from.from_id)

    await msg_from.answer(
        DEFAULT_MESSAGES.note_is_created(is_created),
        reply_markup=menu_keyboard.make_menu_keyboard()
    )


async def get_list_notes(call: types.CallbackQuery, state: FSMContext):
    notes = bot.connector.get_all_notes(call.from_user.id)
    msg = ''
    if notes:
        for note in notes:
            msg += '{0}{1}\n'.format(str(note), '-' * 10)
    else:
        msg = DEFAULT_MESSAGES.empy_notes_list()
    await call.answer()
    await bot.send_message(
        chat_id=call.from_user.id,
        text=msg,
        reply_markup=menu_keyboard.make_menu_keyboard()
    )
    await state.set_state(UserStates.default_state.state)


async def delete_note(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(UserStates.waiting_title_note_to_delete.state)
    await call.answer()
    await bot.send_message(
        chat_id=call.from_user.id,
        text=DEFAULT_MESSAGES.wait_title_note(),
        reply_markup=menu_keyboard.make_cancel_keyboard()
    )


async def wait_title_note_to_delete(msg_from: types.Message, state: FSMContext):
    await state.update_data(title_note=msg_from.text)
    title_note = await state.get_data()
    title_note = title_note['title_note']

    try:
        is_deleted = bot.connector.delete_note(title=title_note, title_worksheet=msg_from.from_id)
    except NoteNotFound:
        is_deleted = False

    await state.set_state(UserStates.default_state.state)
    await msg_from.answer(
        DEFAULT_MESSAGES.note_is_deleted(is_deleted),
        reply_markup=menu_keyboard.make_menu_keyboard()
    )


def register_handlers_notes(dp: Dispatcher):
    dp.register_callback_query_handler(start_work, text='start_work', state='*')
    dp.register_callback_query_handler(create_note, text='create_note', state=UserStates.default_state)
    dp.register_callback_query_handler(get_list_notes, text='get_list_notes', state=UserStates.default_state)
    dp.register_callback_query_handler(delete_note, text='delete_note', state=UserStates.default_state)

    dp.register_message_handler(wait_title_note_to_delete, state=UserStates.waiting_title_note_to_delete)
    dp.register_message_handler(wait_title_note, state=UserStates.waiting_title_note)
    dp.register_message_handler(wait_data_note, state=UserStates.waiting_data_note)
