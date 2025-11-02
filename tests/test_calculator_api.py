import allure
import pytest
from helpers.api_client import send_calculator_request


@allure.feature("WEB Calculator API")
class TestCalculatorAPI:

    @allure.story("Concatenate two numbers")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("num1,num2,expected", [
        (1,2,"<h1>12</h1>"),
        (-3,4,"<h1>-34</h1>"),
        (4,-5,"<h1>4-5</h1>"),
        (-6,-7,"<h1>-6-7</h1>"),
    ])
    def test_concate(self, base_url,num1, num2, expected):
        send_calculator_request(base_url, "concate", num1, num2, expected_status=200, expected_body=expected)

    @allure.story("Divide two numbers")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("num1,num2,expected", [
        (4,2,"<h1>2.0</h1>"),
        (9,3,"<h1>3.0</h1>"),
    ])
    def test_division(self, base_url, num1, num2, expected):
        send_calculator_request(base_url, "division", num1, num2, expected_status=200, expected_body=expected)

    @allure.story("Divide two numbers negative scenario")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("num1,num2,expected", [
        (4,0,"<h1>Internal Server Error</h1>"),
    ])
    def test_division_negative(self, base_url, num1, num2, expected):
        response = send_calculator_request(base_url, "division", num1, num2, expected_status=500)
        with allure.step("Verify response body"):
            assert expected in response.text

    @allure.story("Subtract two numbers")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("num1,num2,expected", [
        (4,2,"<h1>2</h1>"),
        (9,3,"<h1>6</h1>"),
    ])
    def test_subtract(self, base_url, num1, num2, expected):
        send_calculator_request(base_url, "subtract", num1, num2, expected_status=200, expected_body=expected)

    @allure.story("Multiply two numbers")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("num1,num2,expected", [
        (4,2,"<h1>8</h1>"),
        (5,3,"<h1>15</h1>"),
        (0,5,"<h1>0</h1>"),
    ])
    def test_multiple(self, base_url, num1, num2, expected):
        send_calculator_request(base_url, "multiple", num1, num2, expected_status=200, expected_body=expected)

    @allure.story("Exponent two numbers")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("num1,num2,expected", [
        (4,2,"<h1>16</h1>"),
        (5,3,"<h1>125</h1>"),
        (6,0,"<h1>1</h1>"),
        (0,5,"<h1>0</h1>"),
    ])
    def test_exponent(self, base_url, num1, num2, expected):
        send_calculator_request(base_url, "exponent", num1, num2, expected_status=200, expected_body=expected)
