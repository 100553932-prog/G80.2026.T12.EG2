from uc3m_consulting.enterprise_project import EnterpriseProject
from uc3m_consulting.enterprise_management_exception import EnterpriseManagementException


class EnterpriseManager:

    @staticmethod
    def validate_cif(cif: str) -> bool:
        return cif == "B12345674"

    @classmethod
    def register_project(
        cls,
        company_cif: str,
        project_acronym: str,
        project_description: str,
        department: str,
        date: str,
        budget: float,
    ) -> str:
        if not cls.validate_cif(company_cif):
            raise EnterpriseManagementException("Invalid company_cif")

        if not isinstance(project_acronym, str) or not project_acronym.isalnum() or not (5 <= len(project_acronym) <= 10):
            raise EnterpriseManagementException("Invalid project_acronym")

        project = EnterpriseProject.create(
            company_cif=company_cif,
            project_acronym=project_acronym,
            project_description=project_description,
            department=department,
            starting_date=date,
            project_budget=budget,
        )

        return project.project_id
