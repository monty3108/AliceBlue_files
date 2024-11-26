from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from pya3 import *
from Gen_Functions import is_holiday_today, create_dir
from Alice_Module import *

# constants from config files
import config


create_dir(config.dir_name)

# Exit if today is holiday
is_holiday_today()

# Generating Session ID
if config.alice is None:
    logger.info("alice object is None. Calling get_session_id()")
    get_session_id()
    # session_id_generate()
    logging.debug(f'alice obj after calling:{config.alice} ')

# logging balance on csv. Try to maintain only one file
log_trade_book()

# Sending required logs to Telegram
try:
    # docs_to_send = ["app_logs.txt", "data.txt", "logs/trade_log.csv",  "logs/balance.csv"]
    docs_to_send = [config.path_trade_log, config.path_balance]
    bot_token = '5398501864:AAFEn7ljDrKOVkXzhWX4P_khX9Xk-E8FicE'
    url = f"https://api.telegram.org/bot{bot_token}/sendDocument"
    bot_chat_id = ['5162043562']
    for item in docs_to_send:
        document = open(item, "rb")
        response = requests.post(url, data={'chat_id': bot_chat_id}, files={'document': document})
        # logging.info(response.json())
        logging.info(f"{item} sent to Bot.")
except Exception as e:
    text = f"Error: {e}"
    logging.exception(text)