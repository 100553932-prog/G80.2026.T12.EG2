from datetime import datetime, timezone


class EnterpriseProject:
    """Class representing a transfer request"""

    def __init__(
        self,
        company_cif: str,
        project_acronym: str,
        project_description: str,
        department: str,
        starting_date: str,
        project_budget: float,
        time_stamp: float,
    ):
        self.__company_cif = company_cif
        self.__project_description = project_description
        self.__project_acronym = project_acronym
        self.__department = department
        self.__starting_date = starting_date
        self.__project_budget = project_budget
        self.__time_stamp = time_stamp

    @classmethod
    def create(
        cls,
        company_cif: str,
        project_acronym: str,
        project_description: str,
        department: str,
        starting_date: str,
        project_budget: float,
    ):
        return cls(
            company_cif=company_cif,
            project_acronym=project_acronym,
            project_description=project_description,
            department=department,
            starting_date=starting_date,
            project_budget=project_budget,
            time_stamp=datetime.now(timezone.utc).timestamp(),
        )

    @property
    def company_cif(self):
        return self.__company_cif

    @property
    def project_acronym(self):
        return self.__project_acronym

    @property
    def project_description(self):
        return self.__project_description

    @property
    def department(self):
        return self.__department

    @property
    def starting_date(self):
        return self.__starting_date

    @property
    def project_budget(self):
        return self.__project_budget

    @property
    def time_stamp(self):
        return self.__time_stamp

    @staticmethod
    def compute_project_id(
        company_cif: str,
        project_acronym: str,
        project_description: str,
        department: str,
        starting_date: str,
        project_budget: float,
    ) -> str:
        return (
            f"{company_cif}_{project_acronym}_{project_description}_"
            f"{department}_{starting_date}_{project_budget:.2f}"
        )

    @property
    def project_id(self):
        return self.compute_project_id(
            self.company_cif,
            self.project_acronym,
            self.project_description,
            self.department,
            self.starting_date,
            self.project_budget,
        )

    def to_json(self):
        return {
            "company_cif": self.company_cif,
            "project_acronym": self.project_acronym,
            "project_description": self.project_description,
            "department": self.department,
            "starting_date": self.starting_date,
            "project_budget": f"{self.project_budget:.2f}",
            "time_stamp": self.time_stamp,
            "project_id": self.project_id,
        }

