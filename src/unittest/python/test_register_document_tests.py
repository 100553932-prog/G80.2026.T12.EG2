import unittest
from uc3m_consulting import EnterpriseManager


class TestRegisterDocument(unittest.TestCase):

    def test_valid_document_returns_sha256(self):
        signature = EnterpriseManager.register_document(
            "src/unittest/resources/valid_doc.json"
        )
        self.assertRegex(signature, r"^[0-9a-f]{64}$")