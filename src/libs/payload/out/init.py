import json

from typing import Dict
from typing import List
from typing import Tuple

from . import __write_data as write_data


def exec(data: Dict) -> None:
    employees: List[Dict[str, str]] = data['employees']
    write_data.exec(employees)
