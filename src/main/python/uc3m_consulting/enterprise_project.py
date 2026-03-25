from __future__ import annotations
import hashlib
from dataclasses import dataclass
from datetime import datetime, timezone

@dataclass(frozen=True)
class EnterpriseProject:
    company_cif: str
    project_acronym: str
    project_description: str
    department: str
    starting_date: str
    project_budget: float
    time_stamp: float

    @staticmethod
    def compute_project_id(company_cif, project_acronym, project_description, department, starting_date, project_budget) -> str:
        stable = f"{company_cif}|{project_acronym}|{project_description}|{department}|{starting_date}|{project_budget:.2f}"
        return hashlib.md5(stable.encode("utf-8")).hexdigest()

    @classmethod
    def create(cls, company_cif, project_acronym, project_description, department, starting_date, project_budget):
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
    def project_id(self):
        return self.compute_project_id(
            self.company_cif,
            self.project_acronym,
            self.project_description,
            self.department,
            self.starting_date,
            self.project_budget,
        )
