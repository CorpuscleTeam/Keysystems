from keysystems_web.settings import DEBUG

from datetime import datetime

import logging
import os
import traceback
import re


# запись ошибок
def log_error(message, wt: bool = True):
    # now = datetime.now(TIME_ZONE)
    now = datetime.now()
    log_folder = now.strftime ('%m-%Y')
    log_path = os.path.join('logs', log_folder)

    if not os.path.exists(log_path):
        os.makedirs(log_path)

    if DEBUG:
        logging.basicConfig (level=logging.WARNING, encoding='utf-8')
    else:
        log_file_path = os.path.join(log_path, f'{now.day}.log')
        logging.basicConfig (level=logging.WARNING, filename=log_file_path, encoding='utf-8')

    if wt:
        ex_traceback = traceback.format_exc()
        tb = ''
        msg = ''
        start_row = '    File "/app'
        tb_split = ex_traceback.split('\n')
        for row in tb_split:
            if row.startswith(start_row) and not re.search ('venv', row):
                tb += f'{row}\n'

            if not row.startswith(' '):
                msg += f'{row}\n'

        logging.warning(f'{now}\n{tb}\n\n{msg}\n---------------------------------\n')
        return msg
    else:
        logging.warning(f'{now}\n{message}\n\n---------------------------------\n')


# выводит в логи адекватную запись словаря
def log_dict(data: dict):
    data_str = ''
    for k, v in data.items():
        if isinstance(v, dict):
            for k1, v1 in v.items():
                data_str += f'    {k1}: {v1}\n'
        elif isinstance(v, list):
            list_str = ''
            for i in v:
                list_str += f'    {i}\n'
            data_str += f'{k}:\n {list_str}\n'
        else:
            data_str += f'{k}: {v}\n'

    log_error(data_str.strip(), wt=False)