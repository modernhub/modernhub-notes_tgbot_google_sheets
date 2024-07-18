import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


TABLE_URL = '#'

PATH_LOG_BOT_FILE = os.path.join(BASE_DIR, 'logs/botlogs.log')
PATH_LOG_TABLE_FILE = os.path.join(BASE_DIR, 'logs/tablelogs.log')


# better save in environment variables
class CFG_PATHS:
    @staticmethod
    def get_admin_settings():
        admin_settings = os.path.join(BASE_DIR, 'tables/cfg/pytables.json')
        return admin_settings
    @staticmethod
    def get_user_info_table_url():
        user_info_table_url = ''
        return user_info_table_url
    @staticmethod
    def get_bot_settings():
        bot_settings = os.path.join(BASE_DIR, 'tgbot/cfg/botcfg.json')
        return bot_settings
