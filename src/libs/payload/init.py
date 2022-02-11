import requests

from typing import Dict
from typing import List
from typing import Tuple

from . import __login as login
from . import __get as get

import libs
import libs.form


def exec(data: Dict) -> str:
    query: str = data['query']
    headers: Dict[str, str] = data['headers']
    form_data: List[Tuple[str, str]] = libs.form.exec(data)

    session: requests.Session = requests.Session()

    login.exec(session, query, headers, form_data)

    return get.exec(session)