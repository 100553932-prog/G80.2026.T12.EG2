from datetime import datetime, timezone


class EnterpriseProject:
    """Represent a project registered in the system."""

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
        """Build a project entity."""
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
        """Create a project with the current UTC timestamp."""
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
        """Return the company CIF."""
        return self.__company_cif

    @property
    def project_acronym(self):
        """Return the project acronym."""
        return self.__project_acronym

    @property
    def project_description(self):
        """Return the project description."""
        return self.__project_description

    @property
    def department(self):
        """Return the department name."""
        return self.__department

    @property
    def starting_date(self):
        """Return the starting date."""
        return self.__starting_date

    @property
    def project_budget(self):
        """Return the project budget."""
        return self.__project_budget

    @property
    def time_stamp(self):
        """Return the creation timestamp."""
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
        """Build the textual identifier of the project."""
        return (
            f"{company_cif}_{project_acronym}_{project_description}_"
            f"{department}_{starting_date}_{project_budget:.2f}"
        )

    @property
    def project_id(self):
        """Return the computed project identifier."""
        return self.compute_project_id(
            self.company_cif,
            self.project_acronym,
            self.project_description,
            self.department,
            self.starting_date,
            self.project_budget,
        )

    def to_json(self):
        """Serialize the project as a JSON-compatible dictionary."""
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
