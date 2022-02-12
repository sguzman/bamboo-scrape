import functools
import json
import logging
from typing import Dict


__json_path: str = './.env/config/env.json'


@functools.cache
def exec() -> Dict:
    path: str = __json_path
    logging.debug('Loaded %s', path)

    fs = open(path, 'r')

    obj: Dict = json.load(fs)
    return obj
