import allure
import pytest
import requests


@allure.feature("WEB Calculator API")
class TestCalculatorAPI:

    @allure.story("Concatenate two numbers")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("num1,num2,expected", [
        (1,2,"<h1>12</h1>"),
        (3,4,"<h1>34</h1>"),
        (4,5,"<h1>45</h1>"),
    ])
    def test_concate(self, base_url,num1, num2, expected):
        url=f"{base_url}/concate/{num1}/{num2}"
        with allure.step(f"Send GET request to {url}"):
            response = requests.get(url)
        with allure.step("Verify status code is 200"):
            assert response.status_code == 200
        with allure.step("Verify response body"):
            assert response.text.strip() == expected
# TODO негативный test_concate-

