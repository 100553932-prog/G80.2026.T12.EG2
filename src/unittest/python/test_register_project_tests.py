import unittest
from datetime import datetime, timedelta

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


if __name__ == "__main__":
    unittest.main()