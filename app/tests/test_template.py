import requests

BASE_URL = "http://127.0.0.1:8000"


def test_valid_request():
    payload = {
        "fields": {
            "user_email": "example@example.com",
            "user_phone": "+7 123 456 78 90"
        }
    }
    response = requests.post(f"{BASE_URL}/get_form", json=payload)
    print("Valid Request:", response.json())


def test_invalid_request():
    payload = {
        "fields": {
            "user_email": "not-an-email",
            "unknown_field": "some text"
        }
    }
    response = requests.post(f"{BASE_URL}/get_form", json=payload)
    print("Invalid Request:", response.json())


if __name__ == "__main__":
    test_valid_request()
    test_invalid_request()
