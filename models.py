import pytz
from datetime import datetime


class Model():
    def __init__(self, title: str):
        self.title = title


class Note(Model):
    @staticmethod
    def set_foo_note():
        note = Note('')
        note.data = ''
        note.date = ''
        return note

    def update_title(self, title):
        self.title = title
        self.set_date_update_auto()

    def set_data(self, data: str):
        self.data = data

    def get_all(self):  # title, data, date
        return [self.title, self.data, self.date]

    def add_data(self, data: str):
        "\n".join([self.data, data])
        self.set_date_update_auto()

    def set_date_update_auto(self):
        tz_msc = pytz.timezone('Europe/Moscow')
        dt = datetime.now(tz_msc).strftime('%d.%m.%Y %H:%M')
        self.date = dt

    def set_date_update(self, date):
        self.date = date

    def __str__(self):
        return '{0}\n{1}\n{2}\n'.format(self.title, self.data, self.date)
