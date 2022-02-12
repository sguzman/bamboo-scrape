import json
import requests

from typing import Dict
from typing import List
from typing import Tuple

from . import __load as load
from . import __get as get
from . import out
from .out import init

import libs
import libs.form


def exec(data: Dict) -> str:
    query: str = data['query']
    headers: Dict[str, str] = data['headers']
    form_data: List[Tuple[str, str]] = libs.form.exec(data)

    session: requests.Session = load.exec(query, headers, form_data)
    resp: str = get.exec(session)
    obj: Dict = json.loads(resp)
    out.init.exec(obj)

    return resp
