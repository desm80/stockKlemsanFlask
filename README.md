# KlemsanStockParser

### Технологии:
Python 3.8, Flask, Jinja2


### PET-проект(миниприложение на Flask) в котором на данный момент реализованы основные функции:

1. Загрузка складских остатков продукции фирмы Клемсан с сайтов федерального импортера ООО Глобал-инжиниринг и ведущего дистрибутора ООО ЭПАРХ в формате xls, конвертация файла в формат xlsx для обеспечения возможности обработки его библиотекой openpyxl;
2. Проверка наличия продукции по артикулу, возможен поиск по неполному 
   совпадению 


### Запуск проекта:
Клонировать репозиторий и перейти в него в командной строке:

```
https://github.com/desm80/stockKlemsanFlask.git
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
Выполнить команду
```
flask run
```

### Автор
Смирнов Денис

desm80@yandex.ru

телеграм: @DenisSmirnov80



