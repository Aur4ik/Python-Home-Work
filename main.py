# Выполненные задания. Для запуска блока уберите в нём префикс # .
# Активная самостоятельная работа находится ниже.

# =====Основы=====
# Основы 1. Приветствие
# name = input("Имя: ")
# age = int(input("Возраст: "))
# print(f"Привет, {name}! Через год тебе будет {age + 1} лет")

# 
# 2
# number = int(input("Целое число: "))
# if number > 0:
#     print("Положительное")
# elif number < 0:
#     print("Отрицательное")
# else:
#     print("Ноль")
# print("Чётное" if number % 2 == 0 else "Нечётное")

# 
# 3
# from decimal import Decimal
# count = int(input("Количество товаров: "))
# if count < 0:
#     raise ValueError("Количество не может быть отрицательным")
# products = []
# total = Decimal("0")
# for _ in range(count):
#     name = input("Название: ")
#     price = Decimal(input("Цена: "))
#     if price < 0:
#         raise ValueError("Цена не может быть отрицательной")
#     products.append(name)
#     total += price
# print("Товары:", ", ".join(products))
# print("Общая стоимость:", total)

# 
# 4
# name = input("Имя студента: ")
# grades = [int(value) for value in input("Оценки через пробел: ").split()]
# if not grades or any(grade < 1 or grade > 5 for grade in grades):
#     raise ValueError("Введите хотя бы одну оценку от 1 до 5")
# average = sum(grades) / len(grades)
# print(name, "Средняя:", average, "Максимум:", max(grades), "Минимум:", min(grades))
# print("Хороший результат" if average >= 4 else "Нужно повторить тему")

# 
# 5
# users = {}
# todos = {}
#
# def register():
#     username = input("Логин: ").strip()
#     password = input("Пароль: ")
#     if not username or not password or username in users:
#         print("Пустой логин/пароль или логин уже занят")
#         return
#     users[username] = password
#     todos[username] = []
#     print("Аккаунт создан")
#
# def login():
#     username = input("Логин: ").strip()
#     password = input("Пароль: ")
#     if username in users and users[username] == password:
#         return username
#     print("Неверный логин или пароль")
#
# def add_task(username):
#     text = input("Задача: ").strip()
#     if text:
#         todos[username].append(text)
#
# def show_tasks(username):
#     for number, text in enumerate(todos[username], 1):
#         print(number, text)
#     if not todos[username]:
#         print("Задач нет")
#
# def delete_task(username):
#     show_tasks(username)
#     try:
#         index = int(input("Номер задачи: ")) - 1
#         if not 0 <= index < len(todos[username]):
#             raise ValueError
#         todos[username].pop(index)
#     except ValueError:
#         print("Неверный номер")
#
# while True:
#     choice = input("1 — регистрация, 2 — вход, 0 — выход: ")
#     if choice == "0":
#         break
#     if choice == "1":
#         register()
#     elif choice == "2":
#         username = login()
#         if username:
#             while True:
#                 action = input("1 — добавить, 2 — показать, 3 — удалить, 0 — выйти: ")
#                 if action == "0":
#                     break
#                 if action == "1":
#                     add_task(username)
#                 elif action == "2":
#                     show_tasks(username)
#                 elif action == "3":
#                     delete_task(username)
#                 else:
#                     print("Неверный пункт")
#     else:
#         print("Неверный пункт")

# ======Коллекции======
# 1
# prices = [1200, 3500, 800, 2100, 5000, 1700]
# print(prices[:3])
# print(prices[-2:])
# print(prices[::-1])
# print("Минимум:", min(prices), "Максимум:", max(prices), "Количество:", len(prices))

# 
# 2
# students = [{"name": "Анна", "grade": 5}, {"name": "Иван", "grade": 4}, {"name": "Олег", "grade": 3}]
# students.append({"name": "Мария", "grade": 5})
# for student in students:
#     print(student["name"], student["grade"])
# students[2]["grade"] = 4
# print("После изменения:", students[2])

# 
# 3
# from pathlib import Path
# notes_path = Path(__file__).with_name("notes.txt")
# note = input("Заметка: ")
# with notes_path.open("a", encoding="utf-8") as file:
#     file.write(note + "\n")
# with notes_path.open("r", encoding="utf-8") as file:
#     print(file.read())

# 
# 4
# import json
# from pathlib import Path
# books = [{"title": "Гарри Поттер", "year": 1997}, {"title": "Маленький принц", "year": 1943}]
# books_path = Path(__file__).with_name("books.json")
# with books_path.open("w", encoding="utf-8") as file:
#     json.dump(books, file, ensure_ascii=False, indent=4)
# with books_path.open("r", encoding="utf-8") as file:
#     loaded_books = json.load(file)
# for book in loaded_books:
#     print(book["title"], book["year"])

# 
# 5
# class Film:
#     def __init__(self, title, rating):
#         self.title = title
#         self.set_rating(rating)
#
#     def show_info(self):
#         print(f"{self.title}: {self.__rating}/10")
#
#     def get_rating(self):
#         return self.__rating
#
#     def set_rating(self, rating):
#         if not isinstance(rating, (int, float)) or not 0 <= rating <= 10:
#             raise ValueError("Рейтинг должен быть от 0 до 10")
#         self.__rating = rating
#
# film = Film("Интерстеллар", 8.6)
# film.show_info()
# print(film.get_rating())
# film.set_rating(9)
# film.show_info()
# try:
#     film.set_rating(11)
# except ValueError as error:
#     print(error)

# Самостоятельная
import hashlib
import hmac
import json
import os
from pathlib import Path

DATA_PATH = Path(__file__).with_name("data.json")


def read_text(prompt):
    while True:
        try:
            value = input(prompt).strip()
            if not value:
                raise ValueError("Строка не должна быть пустой")
            return value
        except ValueError as error:
            print(error)


def read_choice(prompt, choices):
    while True:
        try:
            value = int(input(prompt))
            if value not in choices:
                raise ValueError("Нет такого пункта")
            return value
        except ValueError:
            print("Введите номер из меню:", ", ".join(map(str, choices)))


class User:
    def __init__(self, username, password=None, *, salt=None, password_hash=None):
        if not username.strip():
            raise ValueError("Пустой логин")
        self._username = username
        self.__salt = salt if salt is not None else os.urandom(16).hex()
        if password is not None:
            if len(password) < 4:
                raise ValueError("Пароль должен содержать минимум 4 символа")
            self.__password_hash = self._hash(password)
        elif password_hash and salt:
            self.__password_hash = password_hash
        else:
            raise ValueError("Нет данных пароля")

    def _hash(self, password):
        return hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"),
                                   bytes.fromhex(self.__salt), 100000).hex()

    def get_username(self):
        return self._username

    def check_password(self, password):
        return hmac.compare_digest(self.__password_hash, self._hash(password))

    def can_manage_all(self):
        return False

    def get_info(self):
        return f"Пользователь: {self._username}"

    def to_dict(self):
        return {"username": self._username, "role": "manager" if self.can_manage_all() else "user",
                "salt": self.__salt, "password_hash": self.__password_hash}


class Manager(User):
    def can_manage_all(self):
        return True

    def get_info(self):
        return f"Менеджер: {self.get_username()} — просмотр и завершение всех задач"


class Task:
    def __init__(self, task_id, owner, title, completed=False):
        if not title.strip() or task_id < 1:
            raise ValueError("Неверные данные задачи")
        self._id = task_id
        self._owner = owner
        self._title = title
        self.__completed = completed

    def get_id(self):
        return self._id

    def get_owner(self):
        return self._owner

    def is_completed(self):
        return self.__completed

    def complete(self):
        self.__completed = True

    def get_info(self):
        status = "готово" if self.is_completed() else "в работе"
        return f"{self._id}. {self._title} [{status}] — {self._owner}"

    def to_dict(self):
        return {"id": self._id, "owner": self._owner, "title": self._title,
                "completed": self.is_completed(), "kind": "urgent" if isinstance(self, UrgentTask) else "normal"}


class UrgentTask(Task):
    def get_info(self):
        return "СРОЧНО! " + super().get_info()


class TaskTracker:
    def __init__(self, path=DATA_PATH):
        self._path = Path(path)
        self._users = {}
        self._tasks = []
        self._writable = True
        self.load()

    def load(self):
        try:
            with self._path.open(encoding="utf-8") as file:
                data = json.load(file)
            users, tasks = {}, []
            for item in data["users"]:
                if item["role"] not in ("user", "manager"):
                    raise ValueError("Неизвестная роль")
                cls = Manager if item["role"] == "manager" else User
                user = cls(item["username"], salt=item["salt"], password_hash=item["password_hash"])
                if user.get_username() in users:
                    raise ValueError("Повторный логин")
                users[user.get_username()] = user
            task_ids = set()
            for item in data["tasks"]:
                if item["owner"] not in users or item["kind"] not in ("normal", "urgent"):
                    raise ValueError("Неверный владелец или тип задачи")
                if type(item["id"]) is not int or type(item["completed"]) is not bool or item["id"] in task_ids:
                    raise ValueError("Неверный номер или статус задачи")
                task_ids.add(item["id"])
                cls = UrgentTask if item["kind"] == "urgent" else Task
                tasks.append(cls(item["id"], item["owner"], item["title"], item["completed"]))
            self._users, self._tasks = users, tasks
        except FileNotFoundError:
            pass  # Первый запуск: начинаем с пустых данных.
        except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError, AttributeError) as error:
            # Не перезаписываем повреждённый исходный файл пустыми данными.
            self._writable = False
            print(f"Не удалось загрузить {self._path.name}: {error}")
            print("Исправьте файл или переименуйте его перед следующим запуском.")

    def save(self):
        if not self._writable:
            raise OSError("Сохранение отключено из-за ошибки загрузки")
        data = {"users": [user.to_dict() for user in self._users.values()],
                "tasks": [task.to_dict() for task in self._tasks]}
        temporary = self._path.with_suffix(".json.tmp")
        with temporary.open("w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        temporary.replace(self._path)

    def register(self, username, password, role):
        if not self._writable:
            raise ValueError("Сначала исправьте файл данных")
        username = username.strip()
        if username in self._users:
            raise ValueError("Логин уже занят")
        if role not in (1, 2):
            raise ValueError("Неизвестная роль")
        user = (Manager if role == 2 else User)(username, password)
        self._users[username] = user
        try:
            self.save()
        except OSError:
            del self._users[username]
            raise
        return user

    def login(self, username, password):
        user = self._users.get(username)
        if user is None or not user.check_password(password):
            raise ValueError("Неверный логин или пароль")
        return user

    def visible_tasks(self, user):
        return [task for task in self._tasks
                if user.can_manage_all() or task.get_owner() == user.get_username()]

    def add_task(self, user, title, urgent=False):
        task_id = max((task.get_id() for task in self._tasks), default=0) + 1
        task = (UrgentTask if urgent else Task)(task_id, user.get_username(), title)
        self._tasks.append(task)
        try:
            self.save()
        except OSError:
            self._tasks.pop()
            raise
        return task

    def complete_task(self, user, task_id):
        for task in self.visible_tasks(user):
            if task.get_id() == task_id:
                was_completed = task.is_completed()
                task.complete()
                try:
                    self.save()
                except OSError:
                    # Восстанавливаем объект через конструктор, не обходя приватное поле.
                    item = task.to_dict()
                    replacement = (UrgentTask if item["kind"] == "urgent" else Task)(
                        item["id"], item["owner"], item["title"], was_completed)
                    self._tasks[self._tasks.index(task)] = replacement
                    raise
                return
        raise ValueError("Нет такой задачи или недостаточно прав")


def account_menu(tracker, user):
    while True:
        print("\n1 — добавить задачу\n2 — история задач\n3 — профиль\n4 — выйти из аккаунта\n5 — завершить задачу")
        if user.can_manage_all():
            print("6 — задачи всех пользователей")
        choices = (1, 2, 3, 4, 5, 6) if user.can_manage_all() else (1, 2, 3, 4, 5)
        choice = read_choice("Ваш выбор: ", choices)
        try:
            if choice == 4:
                return
            if choice == 1:
                title = read_text("Текст задачи: ")
                kind = read_choice("1 — обычная, 2 — срочная: ", (1, 2))
                tracker.add_task(user, title, urgent=kind == 2)
                print("Задача сохранена")
            elif choice in (2, 6):
                tasks = tracker.visible_tasks(user)
                if choice == 2:
                    tasks = [task for task in tasks if task.get_owner() == user.get_username()]
                for task in tasks:
                    print(task.get_info())
                if not tasks:
                    print("Задач пока нет")
            elif choice == 3:
                print(user.get_info())
            elif choice == 5:
                for task in tracker.visible_tasks(user):
                    print(task.get_info())
                task_id = read_choice("Номер задачи (0 — отмена): ",
                                      [0] + [task.get_id() for task in tracker.visible_tasks(user)])
                if task_id:
                    tracker.complete_task(user, task_id)
                    print("Задача завершена")
        except (ValueError, OSError) as error:
            print("Ошибка:", error)


def main():
    tracker = TaskTracker()
    if not tracker._writable:
        return
    try:
        while True:
            print("\n1 — регистрация\n2 — вход\n3 — завершить программу")
            choice = read_choice("Ваш выбор: ", (1, 2, 3))
            try:
                if choice == 3:
                    tracker.save()
                    print("Данные сохранены. До встречи!")
                    break
                username = read_text("Логин: ")
                password = read_text("Пароль: ")
                if choice == 1:
                    role = read_choice("Роль: 1 — пользователь, 2 — менеджер: ", (1, 2))
                    tracker.register(username, password, role)
                    print("Регистрация завершена. Теперь войдите в аккаунт.")
                elif choice == 2:
                    account_menu(tracker, tracker.login(username, password))
            except (ValueError, OSError) as error:
                print("Ошибка:", error)
    except (EOFError, KeyboardInterrupt):
        print("\nВыход. Все изменения сохранялись после каждого действия.")


if __name__ == "__main__":
    main()
