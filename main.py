from classes.api_classes import HeadHunterAPI, SuperJobAPI
from classes.json_saver import JSONSaver
import json


def user_interaction():
    """
    Функция для взаимодействия с пользователем
    """
    # Создание экземпляров класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterAPI()
    superjob_api = SuperJobAPI()

    search_query = input("Введите поисковый запрос: ")  # ключевое значение поиска

    # Получение вакансий с разных платформ
    hh_vacancies = hh_api.get_vacancies(search_query)
    print(hh_vacancies)
    superjob_vacancies = superjob_api.get_vacancies(search_query)
    print(superjob_vacancies)


if __name__ == "__main__":
    user_interaction()