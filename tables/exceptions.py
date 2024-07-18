

class WorksheetNotFound(Exception):
    def __init__(self, title, message='title not found'):
        self.title = title
        self.message = message

    def __str__(self):
        return '{0} {1}'.format(self.title, self.message)

class NoteNotFound(Exception):
    def __init__(self, title, message='Note not found'):
        self.title = title
        self.message = message

    def __str__(self):
        return '{0} {1}'.format(self.title, self.message)