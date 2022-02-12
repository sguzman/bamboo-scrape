import logging
import os
import os.path
from typing import Dict
from typing import List

from . import __write_person_dir as write_person_dir


dir: str = './.env/state/data'


def exec(data: List[Dict[str, str]]) -> None:
    if not os.path.exists(dir):
        logging.debug('Creating data dir')
        os.mkdir(dir)

    for obj in data:
        last_name: str = obj['lastName']
        first_name: str = obj['firstName']
        key_id: str = str(obj['id'])

        filename: str = f'{last_name}_{first_name}_{key_id}'
        write_person_dir.exec(dir, filename, obj)
