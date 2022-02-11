import json
from typing import Dict
from typing import List
from typing import Tuple


def exec(data: Dict) -> List[Tuple[str, str]]:
    obj: Dict[str, str] = data.get('form')

    return [(x, obj[x]) for x in obj.keys()]
