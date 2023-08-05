from classes.api_classes import HeadHunterAPI, SuperJobAPI
from classes.json_saver import JSONSaver
from src.utils import *


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
    superjob_vacancies = superjob_api.get_vacancies(search_query)

    json_vacancies = JSONSaver()  # Создаем экземпляр класса для сохранения в JSON файл

    json_vacancies.to_json("hh_vacancies.json", hh_vacancies)  # Сохраняем в JSON файл вакансии с HH.ru
    json_vacancies.to_json("superjob_vacancies.json", superjob_vacancies) # Сохраняем в JSON файл вакансии с SuperJob

    all = all_vacancies(hh_vacancies, superjob_vacancies)  # Формируем единый список всех вакансий

    if not all:  # Исключаем неверный ввод ключевого значения поиска
        print("Нет вакансий, соответствующих заданным критериям.")
        return

    json_vacancies.vacancies_to_json("all_vacancies.json", all)  # Сохраняем в JSON файл список всех вакансий

    all_vacs = json_vacancies.load_from_json("all_vacancies.json")  # Получаем список всех вакансий с нужными полями
    print(f"Найдено {len(all_vacs)} вакансий")

    # Фильтрация вакансий по дополнительным ключевым словам
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    if filter_words:
        filtered_vacs = filtered_vacancies(all_vacs, filter_words)
    else:
        filtered_vacs = all_vacs

    if not filtered_vacs:
        print("Нет вакансий, соответствующих заданным критериям.")
        return

    print(f"Отфильтрованных вакансий {len(filtered_vacs)}")

    # Фильтрация вакансий по зарплате
    while True:
        salary = input("Введите желаемую зарплату: ")
        if salary.isdigit():
            salary = int(salary)
            break
    salary_vacs = filtered_by_salary(filtered_vacs, salary)

    print(f"Отфильтрованных вакансий {len(salary_vacs)}")

    sorted_by_date = sorted_by_published_date(salary_vacs)

    while True:
        top_n = input("Введите количество вакансий для вывода в топ N: ")
        if top_n.isdigit():
            top_n = int(top_n)
            break

    finally_vacs = Vacancy.finally_sorted(sorted_by_date)  # Список отсортированных вакансий по дате

    print_info(top_n, finally_vacs)


if __name__ == "__main__":
    user_interaction()
