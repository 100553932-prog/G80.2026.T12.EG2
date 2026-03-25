import unittest

from uc3m_consulting import EnterpriseManager
from uc3m_consulting.enterprise_management_exception import EnterpriseManagementException


class TestRegisterDocument(unittest.TestCase):

    def test_valid_document_returns_sha256(self):
        signature = EnterpriseManager.register_document(
            "src/unittest/resources/valid_doc.json"
        )
        self.assertRegex(signature, r"^[0-9a-f]{64}$")

    def test_input_file_not_found_raises(self):
        with self.assertRaises(EnterpriseManagementException):
            EnterpriseManager.register_document("src/unittest/resources/no_file.json")

    def test_input_file_not_json_raises(self):
        with self.assertRaises(EnterpriseManagementException):
            EnterpriseManager.register_document("src/unittest/resources/not_json.json")

    def test_missing_project_id_raises(self):
        with self.assertRaises(EnterpriseManagementException):
            EnterpriseManager.register_document("src/unittest/resources/missing_project_id.json")

    def test_missing_filename_raises(self):
        with self.assertRaises(EnterpriseManagementException):
            EnterpriseManager.register_document("src/unittest/resources/missing_filename.json")

    def test_invalid_project_id_raises(self):
        with self.assertRaises(EnterpriseManagementException):
            EnterpriseManager.register_document("src/unittest/resources/invalid_project_id.json")