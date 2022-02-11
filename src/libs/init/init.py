import functools
from typing import Dict

from . import __log as log
from . import __exit as exit
from . import __greet as greet
from . import __json as json


@functools.cache
def exec() -> Dict:
    log.exec()
    greet.exec()
    exit.exec()
    return json.exec()
