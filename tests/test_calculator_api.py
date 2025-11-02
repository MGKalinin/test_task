import allure
import pytest
import requests


@allure.feature("WEB Calculator API")
class TestCalculatorAPI:

    @allure.story("Concatenate two numbers")
    @allure.severity(allure.severity_level.NORMAL) # TODO каков уровень важности?
    @pytest.mark.parametrize("num1,num2,expected", [
        (1,2,"<h1>12</h1>"),
        (-3,4,"<h1>-34</h1>"),
        (4,-5,"<h1>4-5</h1>"),
        (-6,-7,"<h1>-6-7</h1>"),
    ])
    def test_concate(self, base_url,num1, num2, expected):
        url=f"{base_url}/concate/{num1}/{num2}"
        with allure.step(f"Send GET request to {url}"):
            response = requests.get(url)
        with allure.step("Verify status code is 200"):
            assert response.status_code == 200
        with allure.step("Verify response body"):
            assert response.text.strip() == expected

    @allure.story("Division two numbers")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("num1,num2,expected", [
        (4,2,"<h1>2.0</h1>"),
        (9,3,"<h1>3.0</h1>"),
    ])
    def test_division(self, base_url, num1, num2, expected):
        url=f"{base_url}/division/{num1}/{num2}"
        response = requests.get(url)
        assert response.status_code == 200
        assert response.text.strip() == expected

    @allure.story("Dividing two numbers negative scenario")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("num1,num2,expected", [
        (4,0,"<h1>Internal Server Error</h1>"),
    ])
    def test_division_negative(self, base_url, num1, num2, expected):
        url=f"{base_url}/division/{num1}/{num2}"
        response = requests.get(url)
        assert response.status_code == 500
        assert expected in response.text
