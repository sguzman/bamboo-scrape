import atexit
import json
import logging
import os
import requests
import typing
from typing import Dict
from typing import Optional


class Init:
    json_path: str = './.env.json'
    data: Optional[Dict] = None

    @staticmethod
    def __logging() -> None:
        logging.basicConfig(
            format='[%(asctime)s] [%(levelname)-8s] %(message)s',
            level=logging.DEBUG,
            datefmt='%Y-%m-%d %H:%M:%S')

    @staticmethod
    def __greet() -> None:
        logging.info('hi')

    @staticmethod
    def __exit() -> None:
        atexit.register(lambda: logging.info('hi'))

    @staticmethod
    def __json() -> None:
        path: str = Init.json_path
        logging.info('Loaded %s', path)

        fs = open(path, 'r')

        obj: Dict = json.load(fs)
        Init.data = obj

    @staticmethod
    def exec() -> None:
        Init.__logging()
        Init.__greet()
        Init.__exit()
        Init.__json()


class Util:
    @staticmethod
    def __pretty_print(d: Dict) -> str:
        return json.dumps(d, indent=2)

    @staticmethod
    def data() -> None:
        print(Util.__pretty_print(Init.data))


def main() -> None:
    Init.exec()


if __name__ == '__main__':
    main()
