from abc import ABC, abstractmethod
from os import environ

HEAD_HUNTER_URL = 'https://api.hh.ru/vacancies'
SUPER_JOB_URL = 'https://api.superjob.ru/2.0/vacancies/'
SUPER_JOB_API_KEY = environ.get('SUPERJOB_API_KEY')


class GetAPI(ABC):
    """
    абстрактный класс для работы с API
    """
    def __init__(self):
        self.vacancies = None

    @abstractmethod
    def get_vacancies(self, query: str) -> dict:
        pass

class HeadHunterAPI(GetAPI):
    """
    класс для работы с HeadHunter API
    """

    def get_vacancies(self, query: str) -> dict:
        print(f'\nПолучение данных с {HEAD_HUNTER_URL}...')
        params = {
            'text': f'NAME:{query}',
            'page': 0,
            'per_page': 100,
            'only_with_salary': True
        }
        response = requests.get(HEAD_HUNTER_URL, params)
        result_page = response.json()
        self.vacancies = result_page['items']
        while len(result_page['items']) == 100:
            print(f"Загружено страниц c вакансиями: {params['page'] + 1}")
            params['page'] += 1
            response = requests.get(HEAD_HUNTER_URL, params)
            result_page = response.json()
            if result_page.get('items'):
                self.vacancies.extend(result_page['items'])
            else:
                break
        return self.vacancies