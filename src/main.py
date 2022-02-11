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

import libs
import libs.init
import libs.init.init

import libs.form


data = libs.init.init.exec()
form = libs.form.exec(data)


class Payload:
    s: requests.Session = requests.Session()
    base: str = 'https://growpublicschools.bamboohr.com'
    l: str = f'{base}/login.php'
    p: str = f'{base}/employee_directory/ajax/get_directory_info'

    @staticmethod
    def __login() -> None:
        global form

        param = {
            'r': data['query']
        }

        Payload.s.post(
            Payload.l,
            params=param,
            data=form,
            headers=data['header']
        )

    @staticmethod
    def get() -> str:
        Payload.__login()

        resp = Payload.s.get(Payload.p)
        return resp.text


def main() -> None:
    print(Payload.get())


if __name__ == '__main__':
    main()
