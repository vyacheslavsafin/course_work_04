from abc import ABC, abstractmethod
import json


class Saver(ABC):
    """
    Абстрактный класс для работы с JSON файлами.
    """

    @abstractmethod
    def to_json(self, file):
        pass


class JSONSaver(Saver):
    """
    Класс позволяющий работать с данными для чтения/записи в JSON
    """

    def to_json(self, file, dict_):
        with open(file, 'w', encoding='UTF-8') as fp:
            fp.write(json.dumps(dict_, indent=4, ensure_ascii=False))

    def load_from_json(self, file):
        with open(file, 'r') as fp:
            return json.load(fp)

    def vacancies_to_json(self, file, vacancies):
        dict_vacancies = []
        for vacancy in vacancies:
            if vacancy.responsibility is None:
                vacancy.responsibility = ''
            if vacancy.description is None:
                vacancy.description = ''
            dict_vacancies.append(vacancy.__dict__)
        with open(file, 'w', encoding='UTF-8') as fp:
            fp.write(json.dumps(dict_vacancies, indent=4, ensure_ascii=False))
