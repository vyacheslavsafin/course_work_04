from classes.vacancy import Vacancy
from datetime import datetime


def all_vacancies(hh_vacancies, superjob_vacancies):
    """
    Возвращает список вакансий по ключам из двух баз данных по API
    :param hh_vacancies: база данных из HeadHunter API в JSON формате
    :param superjob_vacancies: база данных из SuperJob API в JSON формате
    :return:
    """
    all_vacancies = []

    for vacancy in hh_vacancies:
        hh_vacancy = Vacancy(vacancy['name'],
                             vacancy['published_at'],
                             vacancy['salary']['from'],
                             vacancy['salary']['to'],
                             vacancy['salary']['currency'],
                             vacancy['snippet']['requirement'],
                             vacancy['snippet']['responsibility'],
                             vacancy['employer']['name'],
                             vacancy['alternate_url']
                             )
        all_vacancies.append(hh_vacancy)

    for vacancy in superjob_vacancies:
        sj_vacancy = Vacancy(vacancy['profession'],
                             vacancy['date_published'],
                             vacancy['payment_from'],
                             vacancy['payment_to'],
                             vacancy['currency'],
                             vacancy['candidat'],
                             'text',
                             vacancy['client'].get('title'),
                             vacancy['link']
                             )
        all_vacancies.append(sj_vacancy)

    vacs = []

    for vac in all_vacancies:
        vacs.append(vac.__dict__)
    return all_vacancies


def filtered_vacancies(all_vacs, words):
    """
    Функция для отбора вакансий по дополнительным ключевым словам
    :param all_vacs: список вакансий
    :param words: ключевые слова
    :return:
    """
    filtered_vacs = []
    for vac in all_vacs:
        for word in words:
            if word.lower() in vac['profession'].lower():
                filtered_vacs.append(vac)
                break
            elif word.lower() in vac['description'].lower():
                filtered_vacs.append(vac)
                break
            elif word.lower() in vac['responsibility'].lower():
                filtered_vacs.append(vac)
                break
    return filtered_vacs


def filtered_by_salary(all_vacs, salary):
    """
    Функция фильтрующая отобранные вакансии по зарплате
    Не включает в список вакансии с валютой отличной от Российского рубля
    :param all_vacs: список отфильтрованных по ключевым словам вакансий
    :param salary: указанная от пользователя желаемая зарплата
    :return:
    """
    filtered_vacs = []
    for vac in all_vacs:
        if vac['currency'] == "RUR" or vac['currency'] == "rub":
            if vac['salary_from']:
                if vac['salary_from'] >= salary:
                    filtered_vacs.append(vac)
            elif vac['salary_to']:
                if vac['salary_to'] >= salary:
                    filtered_vacs.append(vac)
    return filtered_vacs


def sorted_by_published_date(filtered_list):
    """
    Функция форматирования даты публикации к ISO формату, а так же
    сортировки вакансий по дате публикации и выводу списка
    начиная с самой свежей вакансии
    :param filtered_list: список отфильтрованных по зарплате вакансий
    :return:
    """
    for vac in filtered_list:
        if "superjob.ru" in vac["url"]:
            vac["published_date"] = datetime.fromtimestamp(vac["published_date"])
            vac["published_date"] = vac["published_date"].strftime("%d-%m-%Y %H:%M:%S")
            vac["published_date"] = datetime.strptime(vac["published_date"], "%d-%m-%Y %H:%M:%S")
        else:
            vac["published_date"] = datetime.fromisoformat(vac["published_date"])
            vac["published_date"] = vac["published_date"].strftime("%d-%m-%Y %H:%M:%S")
            vac["published_date"] = datetime.strptime(vac["published_date"], "%d-%m-%Y %H:%M:%S")
    sorted_list = sorted(filtered_list, key=lambda x: x["published_date"], reverse=True)
    for vac in sorted_list:
        vac["published_date"] = vac["published_date"].strftime("%d-%m-%Y")
    return sorted_list


def print_info(top_n_vacancies, vacancies_list):
    """
    Вывод информации о вакансиях в консоль
    :param top_n_vacancies:
    :param vacancies_list:
    :return:
    """
    counter = 0
    print("-" * 170)
    for vac in vacancies_list:
        vac.description = vac.description.replace("\n", "")
        print(f"Должность: {vac.profession}\n"
              f"Компания: {vac.company}\n"
              f"Зарплата: {formatted_salary(vac)}\n"
              f"Описание: {vac.description[:150]}\n"
              f"Дата публикации: {vac.published_date}\n"
              f"Ссылка: {vac.url}")
        counter += 1
        if counter == top_n_vacancies:
            break
        print("-" * 170)


def formatted_salary(vac):
    """
    Функция для корректного отображения зарплаты
    """
    if vac.salary_from and vac.salary_to:
        if vac.salary_from != 0 and vac.salary_to != 0:
            return f"от {vac.salary_from} до {vac.salary_to} рублей"
    if vac.salary_from is None or vac.salary_from == 0:
        return f"до {vac.salary_to} рублей"
    if vac.salary_to is None or vac.salary_to == 0:
        return f"от {vac.salary_from} рублей"
