import unittest
from datetime import datetime, timedelta, timezone

from uc3m_consulting.enterprise_manager import EnterpriseManager
from uc3m_consulting.enterprise_management_exception import EnterpriseManagementException


def _future_date_str(days: int) -> str:
    return (datetime.now() + timedelta(days=days)).strftime("%d/%m/%Y")


class MyTestCase(unittest.TestCase):

    def test_invalid_cif_raises(self):
        with self.assertRaises(EnterpriseManagementException):
            EnterpriseManager.register_project(
                company_cif="B1234567X",
                project_acronym="PRJ01",
                project_description="Proyecto Demo",
                department="HR",
                date=_future_date_str(1),
                budget=50000.00,
            )

    def test_invalid_acronym_length_raises(self):
        with self.assertRaises(EnterpriseManagementException):
            EnterpriseManager.register_project(
                company_cif="B12345674",
                project_acronym="PRJ",
                project_description="Proyecto Demo",
                department="HR",
                date=_future_date_str(1),
                budget=50000.00,
            )

    def test_invalid_acronym_chars_raises(self):
        with self.assertRaises(EnterpriseManagementException):
            EnterpriseManager.register_project(
                company_cif="B12345674",
                project_acronym="PRJ_01",
                project_description="Proyecto Demo",
                department="HR",
                date=_future_date_str(1),
                budget=50000.00,
            )

    def test_invalid_description_length_raises(self):
        with self.assertRaises(EnterpriseManagementException):
            EnterpriseManager.register_project(
                company_cif="B12345674",
                project_acronym="PRJ01",
                project_description="Corto",
                department="HR",
                date=_future_date_str(1),
                budget=50000.00,
            )

    def test_invalid_department_raises(self):
        with self.assertRaises(EnterpriseManagementException):
            EnterpriseManager.register_project(
                company_cif="B12345674",
                project_acronym="PRJ01",
                project_description="Proyecto Demo",
                department="SALES",
                date=_future_date_str(1),
                budget=50000.00,
            )

    def test_invalid_date_format_raises(self):
        with self.assertRaises(EnterpriseManagementException):
            EnterpriseManager.register_project(
                company_cif="B12345674",
                project_acronym="PRJ01",
                project_description="Proyecto Demo",
                department="HR",
                date="2026-01-01",
                budget=50000.00,
            )

    def test_past_date_raises(self):
        past = (datetime.now(timezone.utc).date() - timedelta(days=1)).strftime("%d/%m/%Y")
        with self.assertRaises(EnterpriseManagementException):
            EnterpriseManager.register_project(
                company_cif="B12345674",
                project_acronym="PRJ01",
                project_description="Proyecto Demo",
                department="HR",
                date=past,
                budget=50000.00,
            )


if __name__ == "__main__":
    unittest.main()