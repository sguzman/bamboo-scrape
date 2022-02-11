import pickle
import requests
from typing import Dict
from typing import List
from typing import Tuple


base_path: str = 'https://growpublicschools.bamboohr.com'
log_url: str = f'{base_path}/login.php'


def exec(
        query: str,
        headers: Dict[str, str],
        data: List[Tuple[str, str]]) -> requests.Session:
    params = {
        'r': query
    }

    session: requests.Session = requests.Session()

    session.post(
        log_url,
        params=params,
        data=data,
        headers=headers
    )

    return session
