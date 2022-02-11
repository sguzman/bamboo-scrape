from . import __log as log
from . import __exit as exit
from . import __greet as greet
from . import __json as json


def exec() -> None:
    log.exec()
    greet.exec()
    exit.exec()
    json.json()
