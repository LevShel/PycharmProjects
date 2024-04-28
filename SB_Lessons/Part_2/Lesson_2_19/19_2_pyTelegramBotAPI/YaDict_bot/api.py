import requests
from typing import List, Dict

from config import API_BASE_URL, API_KEY


def api_request(endpoint: str, params={}) -> requests.Response:
    params['key'] = API_KEY
    return requests.get(
        f'{API_BASE_URL}/{endpoint}',
        params=params
    )


def get_langs() -> List[str]:
    response = api_request('getLangs');
    return response.json()


def lookup(lang: str, text: str, ui: str = 'ru') -> Dict:
    response = api_request('lookup', params={
        'lang': lang,
        'text': text,
        'ui': ui
    })

    return response.json().get('def', {})
