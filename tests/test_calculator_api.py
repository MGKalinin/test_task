import allure
import pytest
from helpers.api_client import send_calculator_request


@allure.feature("WEB Calculator API")
class TestCalculatorAPI:

    ##### Позитивные тесты #####

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

    @allure.story("Exponentiate two numbers")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("num1,num2,expected", [
        (4,2,"<h1>16</h1>"),
        (5,3,"<h1>125</h1>"),
        (6,0,"<h1>1</h1>"),
        (0,5,"<h1>0</h1>"),
    ])
    def test_exponent(self, base_url, num1, num2, expected):
        send_calculator_request(base_url, "exponent", num1, num2, expected_status=200, expected_body=expected)

    ##### Негативные тесты: деление не ноль #####

    @allure.story("Divide by zero")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("num1,num2,expected", [
        (4, 0, "<h1>Internal Server Error</h1>"),
    ])
    def test_division_negative(self, base_url, num1, num2, expected):
        response = send_calculator_request(base_url, "division", num1, num2, expected_status=500)
        with allure.step("Verify response body"):
            assert expected in response.text

    ##### Негативные тесты: не числовой ввод #####

    @allure.story("Concatenate with non-numeric input")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("num1,num2", [
        ("abc", 2),
        (1, "xyz"),
        ("foo", "bar"),
    ])
    def test_concate_invalid_input(self, base_url, num1, num2):
        send_calculator_request(base_url, "concate", num1, num2, expected_status=400)

    @allure.story("Division with non-numeric input")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("num1,num2", [
        ("abc", 2),
        (1, "xyz"),
        ("foo", "bar"),
    ])
    def test_division_invalid_input(self, base_url, num1, num2):
        send_calculator_request(base_url, "division", num1, num2, expected_status=400)

    @allure.story("Subtraction with non-numeric input")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("num1,num2", [
        ("abc", 2),
        (1, "xyz"),
        ("foo", "bar"),
    ])
    def test_subtract_invalid_input(self, base_url, num1, num2):
        send_calculator_request(base_url, "subtract", num1, num2, expected_status=400)

    @allure.story("Multiplication with non-numeric input")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("num1,num2", [
        ("abc", 2),
        (1, "xyz"),
        ("foo", "bar"),
    ])
    def test_multiple_invalid_input(self, base_url, num1, num2):
        send_calculator_request(base_url, "multiple", num1, num2, expected_status=400)

    @allure.story("Exponentiation with non-numeric input")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("num1,num2", [
        ("abc", 2),
        (1, "xyz"),
        ("foo", "bar"),
    ])
    def test_exponent_invalid_input(self, base_url, num1, num2):
        send_calculator_request(base_url, "exponent", num1, num2, expected_status=400)

    ##### Негативные тесты: пустой ввод

    @allure.story("Concatenate with empty input")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("num1,num2", [
        ("", 2),
        (1, ""),
        ("", ""),
    ])
    def test_concate_empty_input(self, base_url, num1, num2):
        send_calculator_request(base_url, "concate", num1, num2, expected_status=400)

    @allure.story("Division with empty input")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("num1,num2", [
        ("", 2),
        (1, ""),
        ("", ""),
    ])
    def test_division_empty_input(self, base_url, num1, num2):
        send_calculator_request(base_url, "division", num1, num2, expected_status=400)

    @allure.story("Subtraction with empty input")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("num1,num2", [
        ("", 2),
        (1, ""),
        ("", ""),
    ])
    def test_subtract_empty_input(self, base_url, num1, num2):
        send_calculator_request(base_url, "subtract", num1, num2, expected_status=400)

    @allure.story("Multiplication with empty input")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("num1,num2", [
        ("", 2),
        (1, ""),
        ("", ""),
    ])
    def test_multiple_empty_input(self, base_url, num1, num2):
        send_calculator_request(base_url, "multiple", num1, num2, expected_status=400)

    @allure.story("Exponentiation with empty input")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("num1,num2", [
        ("", 2),
        (1, ""),
        ("", ""),
    ])
    def test_exponent_empty_input(self, base_url, num1, num2):
        send_calculator_request(base_url, "exponent", num1, num2, expected_status=400)
