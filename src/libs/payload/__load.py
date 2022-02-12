import pickle
import requests
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple

import libs
import libs.load_session
import libs.save_session
import libs.payload
import libs.payload.__login as login


def exec(
        query: str,
        headers: Dict[str, str],
        data: List[Tuple[str, str]]) -> requests.Session:

    s: Optional[requests.Session] = libs.load_session.exec()
    if s is None:
        session: requests.Session = login.exec(query, headers, data)
        libs.save_session.exec(session)

        return session
    else:
        return s
