import functools
import requests
from typing import Dict
from typing import List
from typing import Tuple


base_path: str = 'https://growpublicschools.bamboohr.com'
log_url: str = f'{base_path}/login.php'


def exec(
        session: requests.Session,
        query: str,
        headers: Dict[str, str],
        form: List[Tuple[str, str]]) -> None:
    param = {
        'r': query
    }

    session.post(
        log_url,
        params=param,
        data=form,
        headers=headers
    )
