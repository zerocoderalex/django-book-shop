# BookShop & Telegram Bot

## Описание проекта
Этот проект представляет собой интернет-магазин книг на Django с Telegram-ботом для проверки статуса заказов.

### Функционал магазина
- Главная страница с информацией о магазине.
- Страница ассортимента с товарами в виде карточек.
- Корзина, привязанная к сессии.
- Оформление заказа с сохранением данных в базе данных.
- Уникальный ключ для каждого заказа.

### Telegram-бот
- Бот создан с использованием `aiogram`.
- Проверяет статус заказа по ключу, выданному на сайте.
- Выводит статус и наполнение заказа, если ключ существует в базе данных.

---

## Установка и настройка
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/username/repo-name.git
   cd repo-name
   ```

2. Установите зависимости для Django:
   ```bash
   pip install django
   ```

3. Настройте базу данных:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Запустите сервер:
   ```bash
   python manage.py runserver
   ```

5. Настройте и запустите бота:
   - Установите зависимости для `aiogram`:
     ```bash
     pip install aiogram
     ```
   - Добавьте токен бота в переменные окружения:
     ```bash
     export BOT_TOKEN="your-bot-token"
     ```
   - Запустите бота:
     ```bash
     python bot.py
     ```

---

## Структура проекта
- **bookshop/** — папка с кодом Django-приложения.
  - `static/` — файлы стилей.
  - `templates/` — HTML-шаблоны.
  - `db.sqlite3` — база данных (SQLite).
- **bot/** — папка с кодом Telegram-бота.

---

## Требования
- Python 3.9+
- Django 5.1.4
- aiogram 3.0+

---

## Лицензия
Проект распространяется под лицензией MIT.
