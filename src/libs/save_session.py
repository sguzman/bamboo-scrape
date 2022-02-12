import logging
import os
import os.path
import pickle
import requests
from typing import Dict
from typing import Optional

import libs
import libs.write_as_bytes


__json_path: str = './.env/state/session.pickled'


def exec(session: requests.Session) -> None:
    path: str = __json_path

    logging.debug('Writing http session %s', path)
    bn: bytes = pickle.dumps(session)
    libs.write_as_bytes.exec(path, bn)
