from haptik_helpers import Integrations

# Instantiate a Multiplication object
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
integrate = Integrations(test_enity)

# Call the multiply method
print(integrate.get_entity("kli_otp"))