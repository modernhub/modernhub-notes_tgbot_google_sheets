from aiogram import Bot, types
from tgbot import utils
from settings import CFG_PATHS
from tables.connector import ConnectorWithTable

TOKEN = utils.get_token_from_json(CFG_PATHS.get_bot_settings())


class TGBot(Bot):
    def __init__(self,
                 token,
                 parse_mode=types.ParseMode.HTML,
                 connector=None
                 ):
        super().__init__(
            token,
            parse_mode=parse_mode
        )
        self.connector = connector


bot = TGBot(
    token=TOKEN,
    parse_mode=types.ParseMode.HTML,
    connector=ConnectorWithTable()
)
