from datetime import datetime, timezone

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

        if not isinstance(project_description, str) or not (10 <= len(project_description) <= 30):
            raise EnterpriseManagementException("Invalid project_description")

        if department not in {"HR", "FINANCE", "LEGAL", "LOGISTICS"}:
            raise EnterpriseManagementException("Invalid department")

        try:
            dt = datetime.strptime(date, "%d/%m/%Y").date()
        except ValueError as exc:
            raise EnterpriseManagementException("Invalid date") from exc

        today = datetime.now(timezone.utc).date()
        if dt < today or dt.year < 2025 or dt.year > 2027:
            raise EnterpriseManagementException("Invalid date")

        if not isinstance(budget, float) or budget < 50000.0 or budget > 1000000.0:
            raise EnterpriseManagementException("Invalid budget")

        project = EnterpriseProject.create(
            company_cif=company_cif,
            project_acronym=project_acronym,
            project_description=project_description,
            department=department,
            starting_date=date,
            project_budget=budget,
        )

        return project.project_id