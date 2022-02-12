import logging
import os
import os.path
from typing import Dict

import libs
import libs.write_as_str


def exec(dir: str, name: str, data: Dict[str, str]) -> None:
    if not os.path.exists(dir):
        logging.debug('Creating dir for %s', name)
        os.mkdir(dir)

    folder: str = os.path.join(dir, name)
    if not os.path.exists(folder):
        os.mkdir(folder)

    for key in data.keys():
        full_path = os.path.join(folder, key)
        libs.write_as_str.exec(full_path, data[key])
