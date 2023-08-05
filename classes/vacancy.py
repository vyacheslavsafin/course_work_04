class Vacancy:
    """
    Класс для работы с вакансиями
    """
    def __init__(self, profession, published_date, salary_from, salary_to, currency, description, responsibility, company, url):
        self.profession = profession
        self.published_date = published_date
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.description = description
        self.responsibility = responsibility
        self.company = company
        self.url = url