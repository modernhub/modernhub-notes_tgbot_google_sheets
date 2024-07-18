import asyncio
from tgbot.main import main
from loguru import logger
from settings import PATH_LOG_BOT_FILE

logger.add(
    PATH_LOG_BOT_FILE,
    format='{time} {level} {message}',
    level='DEBUG',
    rotation='1 week',
    compression='zip'
)

if __name__ == '__main__':
    asyncio.run(main())
#botname in telegram - tabletestbot