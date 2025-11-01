# Задача:   
### Нужно использовать сваггер как документацию, на основе него написать автотесты,    
### покрывающие функциональные требования.    
### Из инструментов использовать pytest+allure(библиотека allure-pytest).

## Установить зависимости:   
> ```bash
> pip install -r requirements.txt
> ```

## Запуск pytest   
>```bash
> pytest -v
>```   


## Запуск с Allure 
### Шаг 1: Запуск тестов   
>```bash
> pytest tests/ --alluredir=./allure-results
>```   

### Шаг 2: Просмотр отчёта (нужно allure-cli установить в систему (ОС))
>```bash
> allure serve ./allure-results
>```  
