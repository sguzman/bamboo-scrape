from . import log
from . import exit
from . import greet
from . import json


def exec() -> None:
    log.exec()
    greet.exec()
    exit.exec()
    json.exec()
