Bookspace — каталог книг
API: https://openlibrary.org/search.json
Документация: https://openlibrary.org/dev/docs/api/search
Сайт получает JSON через requests.get(), передаёт книги в Django-шаблон
и выводит их циклом for: название, авторы, год первого издания, число изданий.
Данные не заменяются вручную заданным списком. При ошибке API показывается сообщение.

Запуск из папки bookspace (Python 3.10+):
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python manage.py check
.venv\Scripts\python manage.py runserver
Откройте http://127.0.0.1:8000/ и сделайте скриншот страницы.
Настройки предназначены для локальной учебной работы.
Роль менеджера в консольной работе выбирается при регистрации по условию задания.
