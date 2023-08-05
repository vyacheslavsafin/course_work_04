from classes.vacancy import Vacancy


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