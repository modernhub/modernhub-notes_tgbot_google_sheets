from aiogram.dispatcher.filters.state import State, StatesGroup

class UserStates(StatesGroup):
    default_state = State() # юзер переводится в дефолтное состояние, когда создан рабочий лист с его заметками
    waiting_title_note = State()
    waiting_data_note = State()
    waiting_title_note_to_delete = State()
