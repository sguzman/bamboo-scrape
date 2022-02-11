import atexit
import functools
import json
import logging
import os
import requests
import typing
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple


class Init:
    json_path: str = './.env.json'

    @staticmethod
    def __logging() -> None:
        logging.basicConfig(
            format='[%(asctime)s] [%(levelname)-8s] %(message)s',
            level=logging.INFO,
            datefmt='%Y-%m-%d %H:%M:%S')

    @staticmethod
    def __greet() -> None:
        logging.debug('hi')

    @staticmethod
    def __exit() -> None:
        atexit.register(lambda: logging.debug('hi'))

    @staticmethod
    @functools.cache
    def json() -> Dict:
        path: str = Init.json_path
        logging.debug('Loaded %s', path)

        fs = open(path, 'r')

        obj: Dict = json.load(fs)
        return obj

    @staticmethod
    def exec() -> None:
        Init.__logging()
        Init.__greet()
        Init.__exit()
        Init.json()


def init() -> None:
    Init.exec()


class Util:
    @staticmethod
    def __pretty_print(d) -> str:
        return json.dumps(d, indent=2)

    @staticmethod
    def data(data) -> None:
        print(Util.__pretty_print(data))

    @staticmethod
    def form() -> List[Tuple[str, str]]:
        obj: Dict[str, str] = Init.json()['form']

        return [(x, obj[x]) for x in obj.keys()]


class Payload:
    s: requests.Session = requests.Session()
    base: str = 'https://growpublicschools.bamboohr.com'
    l: str = f'{base}/login.php'
    p: str = f'{base}/employee_directory/ajax/get_directory_info'

    @staticmethod
    def __login() -> None:
        d = Init.json()
        data = Util.form()
        param = {
            'r': d['query']
        }

        Payload.s.post(
            Payload.l,
            params=param,
            data=data,
            headers=d['header']
        )

    @staticmethod
    def get() -> str:
        Payload.__login()

        resp = Payload.s.get(Payload.p)
        return resp.text


def main() -> None:
    init()
    print(Payload.get())


if __name__ == '__main__':
    main()
