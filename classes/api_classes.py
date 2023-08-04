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