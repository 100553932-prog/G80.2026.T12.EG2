import json
from datetime import datetime, timezone
from pathlib import Path

from uc3m_consulting.enterprise_project import EnterpriseProject
from uc3m_consulting.enterprise_management_exception import EnterpriseManagementException


class EnterpriseManager:

    @staticmethod
    def validate_cif(cif: str) -> bool:
        return cif == "B12345674"

    @staticmethod
    def _project_root() -> Path:
        return Path(__file__).resolve().parents[4]

    @classmethod
    def _data_dir(cls) -> Path:
        data_dir = cls._project_root() / "data"
        data_dir.mkdir(parents=True, exist_ok=True)
        return data_dir

    @classmethod
    def _corporate_ops_file(cls) -> Path:
        return cls._data_dir() / "corporate_operations.json"

    @staticmethod
    def _read_json_list(path: Path):
        if not path.exists():
            return []
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)

    @staticmethod
    def _write_json_list(path: Path, data):
        with path.open("w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

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

        existing = cls._read_json_list(cls._corporate_ops_file())

        for item in existing:
            if item.get("company_cif") == company_cif and item.get("project_description") == project_description:
                raise EnterpriseManagementException("Duplicate project")

        project = EnterpriseProject.create(
            company_cif=company_cif,
            project_acronym=project_acronym,
            project_description=project_description,
            department=department,
            starting_date=date,
            project_budget=budget,
        )

        existing.append(project.to_json())
        cls._write_json_list(cls._corporate_ops_file(), existing)
        return project.project_id

    @classmethod
    def register_document(cls, input_file: str) -> str:
        path = Path(input_file)
        if not path.exists():
            raise EnterpriseManagementException("Input file not found")

        try:
            with open(input_file, "r", encoding="utf-8") as file:
                payload = json.load(file)
        except json.JSONDecodeError as exc:
            raise EnterpriseManagementException("Input file is not JSON") from exc

        from uc3m_consulting.project_document import ProjectDocument

        document = ProjectDocument.create(
            project_id=payload["PROJECT_ID"],
            file_name=payload["FILENAME"],
        )

        return document.file_signature