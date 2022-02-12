import functools
import logging
import os
import os.path
import pickle
import requests
from typing import Dict
from typing import Optional

import libs
import libs.read_as_bytes


__json_path: str = './.env/state/session.pickled'


@functools.cache
def exec() -> Optional[requests.Session]:
    path: str = __json_path

    if os.path.exists(path):
        logging.debug('Loading http session %s', path)
        bn: bytes = libs.read_as_bytes.exec(path)
        obj: requests.Session = pickle.loads(bn)

        return obj

    return None
