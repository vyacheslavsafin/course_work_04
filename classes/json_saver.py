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
        """Метод, сохраняющий в файл значения атрибутов экземпляра класса"""
        with open(file, 'w', encoding='UTF-8') as fp:
            fp.write(json.dumps(dict_, indent=4, ensure_ascii=False))
