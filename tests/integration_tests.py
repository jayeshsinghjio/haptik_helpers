import unittest
import math
from haptik_helpers import Integrations


class IntegrationsTestCase(unittest.TestCase):

    def setUp(self):
        test_enity = {
            "kli_policy_number": [],
            "kli_client_id": [],
            "phone_number": [
            {
                "detection": "message",
                "original_text": "8826755968",
                "entity_value": "8826755968",
                "language": "en"
            }
            ],
            "kli_otp": [
            {
                "detection": "message",
                "original_text": "986265",
                "entity_value": {
                "value": "986265"
                },
                "regex": "\\\\b\\\\d{6}\\\\b"
            }
            ],
            "kli_dummy_date_year": [],
            "kli_dummy_date": [],
            "kli_policy_statement_type": [],
            "kli_policy_value_type": []
        }
        self.integration = Integrations(test_enity)

    def test_phone_entity(self):
        """Test phone number entity"""

        result = self.integration.get_entity("phone_number")
        self.assertEqual(result, "8826755968")

    def test_otp_entity(self):
        """Test otp number entity"""

        result = self.integration.get_entity("kli_otp")
        self.assertEqual(result, "986265")

    def test_not_found_entity(self):
        """Test entity wich is not available in entity list"""

        result = self.integration.get_entity("xyz")
        self.assertEqual(result, '')



if __name__ == '__main__':
    unittest.main()