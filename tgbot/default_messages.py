
class DEFAULT_MESSAGES():
    @staticmethod
    def start():
        msg = 'Привет! Я бот для создания заметок, помогу тебе сохранить важные мыслишки и вообще все что угодно.\n P.S. я создан в учебных целях,' \
              'поэтому не ругайтесь сильно'

        return msg
    @staticmethod
    def help():
        msg = 'help'
        return msg

    @staticmethod
    def start_work():
        msg = 'Все готово, можешь начинать редактировать заметки'
        return msg

    @staticmethod
    def wait_title_note():
        msg = 'Введите название заметки'
        return msg

    @staticmethod
    def wait_data_note():
        msg = 'Введите заметку'
        return msg

    @staticmethod
    def note_is_created(successful_request:bool):
        if successful_request:
            msg = 'Заметка создана'
        else:
            msg = 'Не удалось создать заметку, попробуйте еще раз'
        return msg
    @staticmethod
    def note_is_updated(successful_request:bool):
        if successful_request:
            msg = 'Заметка обновлена'
        else:
            msg = 'Не удалось обновить заметку, попробуйте еще раз'
        return msg
    @staticmethod
    def note_is_deleted(successful_request:bool):
        if successful_request:
            msg = 'Заметка удалена'
        else:
            msg = 'Не удалось удалить заметку, попробуйте еще раз'
        return msg
    @staticmethod
    def cancel():
        return 'Действие отменено'

    @staticmethod
    def empy_notes_list():
        return 'У вас нет заметок'
