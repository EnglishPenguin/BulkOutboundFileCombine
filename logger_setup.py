from loguru import logger

logger.add("M:/CPP-Data/Sutherland RPA/Coding/CSE1236/References/Monthly Combined/Logs/{time:YYYY-MM-DD}.log",
           format="{time:YYYY-MM-DD at HH:mm:ss} | {level} - {message}",
           colorize=True, backtrace=True, diagnose=True, level='INFO', retention='90 days')