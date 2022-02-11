import requests


base_path: str = 'https://growpublicschools.bamboohr.com'
dir_url: str = f'{base_path}/employee_directory/ajax/get_directory_info'


def exec() -> str:
    resp = requests.get(dir_url)
    return resp.text
