import gspread
from tables import exceptions
from models import Note
from settings import CFG_PATHS, TABLE_URL, PATH_LOG_TABLE_FILE

from loguru import logger

logger.add(
    PATH_LOG_TABLE_FILE,
    format='{time} {level} {message}',
    level='DEBUG',
    rotation='1 week',
    compression='zip'
)

"""!!!ATTENTION
    ID юзера в тг - тайтл рабочего листа в таблице
"""

# коннектор переписать, потому что при нормальной нагрузке он будет работать медленее черепахи, т.к. синхронный,
# активный рабочий лист меняется с разных корутин, поэтому вообще беда, надо либо список рабочих листов хранить (затратно по памяти),
# либо локать активный лист, что сделает эту беднягу еще медленнее
#в асинхронной разработке я не силен, поэтому костыльнем списком листов рабочих P.S. вот такой вот я молодец :)


class Connector():
    def __init__(self):
        self.url = TABLE_URL
        self.__open_table()

    def __open_table(self):
        self.gc = gspread.service_account(filename=CFG_PATHS.get_admin_settings())
        self.sheet = self.gc.open_by_url(self.url)


class WorksheetsEditor(Connector):
    def __init__(self):
        super().__init__()
        self.__active_worksheet = self.sheet.worksheets()[0]

    def get_worksheets_list(self):
        return self.sheet.worksheets()

    def add_worksheet(self, title):
        title = str(title)
        worksheet = self.find_worksheet_with_title(title)
        if worksheet is None:
            self.sheet.add_worksheet(title=title, rows=256, cols=3)


    def delete_worksheet(self):
        self.sheet.del_worksheet()


    def find_worksheet_with_title(self, title):
        title = str(title)
        worksheets = self.sheet.worksheets()
        for worksheet in worksheets:
            if str(worksheet.title) == title:
                return worksheet
        return None


class ConnectorWithTable(Connector):
    notes = []

    def __init__(self):
        super().__init__()
        self.worksheets_editor = WorksheetsEditor()

    def set_note(self, note:Note, worksheet_title:str)->bool:
        self.get_all_notes(worksheet_title)
        for i in range(len(self.notes)):
            if self.notes[i].title == note.title:
                return self.__push_to_table(note, position=i+1, title_worksheet=worksheet_title)
        return self.__push_to_table(note, position=len(self.notes)+1, title_worksheet=worksheet_title)

    def get_all_notes(self, title_worksheet)->list:
        self.notes = self.__load_from_table(title_worksheet)
        notes = []
        for note in self.notes:
            if not note.title == '':
                notes.append(note)
        return notes

    def get_note(self, title, title_worksheet):
        self.get_all_notes(title_worksheet)
        for note in self.notes:
            if note.title == title:
                return note
        raise exceptions.NoteNotFound(title)

    def delete_note(self, title, title_worksheet):
        self.get_all_notes(title_worksheet)
        note = Note.set_foo_note()

        for i in range(len(self.notes)):
            if self.notes[i].title == title:
                self.__push_to_table(note, position=i+1, title_worksheet=title_worksheet)
                return True
        raise exceptions.NoteNotFound(title)

    def __push_to_table(self, note:Note, position, title_worksheet)->bool:
        title_worksheet = str(title_worksheet)
        try:
            worksheet = self.worksheets_editor.find_worksheet_with_title(title_worksheet)
            worksheet.update('A{0}'.format(position), note.title) #колонка в таблице тайтл
            worksheet.update('B{0}'.format(position), note.data) #колонка в таблице данные
            worksheet.update('C{0}'.format(position), note.date) #колонка в таблице дата
            return True
        except Exception as err:
            logger.debug(str(err))
            return False

    def __load_from_table(self, title_worksheet)->list:
        notes = []
        title_worksheet = str(title_worksheet)
        worksheet = self.worksheets_editor.find_worksheet_with_title(title_worksheet)
        if worksheet:
            records = worksheet.get_all_values()
        else:
            return []
        for item in records:
            note = Note(item[0])
            note.set_data(item[1])
            note.set_date_update(item[2])
            notes.append(note)

        self.notes = notes
        return self.notes

#в общем, коннектор - инвалид
