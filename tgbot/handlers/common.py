from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

from tgbot.keyboards import menu_keyboard
from tgbot.default_messages import DEFAULT_MESSAGES
from tgbot.user_states import UserStates
from tgbot.bot import bot


async def cmd_start(msg_from: types.Message, state: FSMContext):
    await state.finish()
    await msg_from.answer(
        DEFAULT_MESSAGES.start(),
        reply_markup=menu_keyboard.make_start_keyboard()
    )
#команду хелп я выпилил, потому что интерфейс элементарный, и я не придумал, что написать в хелпе
async def callback_help(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(UserStates.default_state.state)
    await call.answer()
    await bot.send_message(
        call.from_user.id,
        DEFAULT_MESSAGES.help(),
        reply_markup=menu_keyboard.make_menu_keyboard()
    )


async def callback_cancel(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(UserStates.default_state.state)
    await call.answer()
    await bot.send_message(
        chat_id=call.from_user.id,
        text=DEFAULT_MESSAGES.cancel(),
        reply_markup=menu_keyboard.make_menu_keyboard()
    )


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands='start', state='*')
    dp.register_callback_query_handler(callback_cancel, text='cancel', state='*')
