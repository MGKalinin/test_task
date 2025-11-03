import allure
import requests


def send_calculator_request(base_url, endpoint, num1, num2, expected_status=200, expected_body=None):
    """Sends a GET request to the calculator endpoint and verifies the response status code and body."""
    url = f"{base_url}/{endpoint}/{num1}/{num2}"
    with allure.step(f"Send GET request to {url}"):
        response = requests.get(url)

    with allure.step(f"Verify status code is {expected_status}"):
        assert response.status_code == expected_status

    if expected_body is not None:
        with allure.step("Verify response body"):
            assert response.text.strip() == expected_body

    return response
