class Vacancy:
    """
    Класс для работы с вакансиями
    """

    def __init__(self, profession, published_date, salary_from, salary_to, currency, description, responsibility,
                 company, url):
        self.profession = profession
        self.published_date = published_date
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.description = description
        self.responsibility = responsibility
        self.company = company
        self.url = url

    @classmethod
    def finally_sorted(cls, vacancies):
        top = []
        for vac in vacancies:
            vacancy = cls(vac["profession"],
                          vac["published_date"],
                          vac["salary_from"],
                          vac["salary_to"],
                          vac["currency"],
                          vac["description"],
                          vac["responsibility"],
                          vac["company"],
                          vac["url"]
                          )
            top.append(vacancy)
        return top

    def __repr__(self):
        return (f"Vacancy(profession='{self.profession}',"
                f"published_date='{self.published_date}',"
                f"salary_from='{self.salary_from}',"
                f"salary_to='{self.salary_to}',"
                f"currency='{self.currency}',"
                f"description='{self.description}',"
                f"responsibility='{self.responsibility}',"
                f"company='{self.company}',"
                f"url='{self.url}')")

    def __str__(self):
        return (f"(profession='{self.profession}',"
                f"published_date='{self.published_date}',"
                f"salary_from='{self.salary_from}',"
                f"salary_to='{self.salary_to}',"
                f"currency='{self.currency}',"
                f"description='{self.description}',"
                f"responsibility='{self.responsibility}',"
                f"company='{self.company}',"
                f"url='{self.url}')")
