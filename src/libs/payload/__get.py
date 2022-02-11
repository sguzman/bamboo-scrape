import requests


base_path: str = 'https://growpublicschools.bamboohr.com'
dir_url: str = f'{base_path}/employee_directory/ajax/get_directory_info'


def exec(session: requests.Session) -> str:
    resp = session.get(dir_url)
    return resp.text
