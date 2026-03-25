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
    from uc3m_consulting.enterprise_project import EnterpriseProject
    project = EnterpriseProject.create(
        company_cif=company_cif,
        project_acronym=project_acronym,
        project_description=project_description,
        department=department,
        starting_date=date,
        project_budget=budget,
    )
    return project.project_id