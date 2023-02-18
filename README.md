# GetPicLink Telegram Bot

Це Telegram-бот, який генерує посилання на фото, завантажене в чаті. Бот створено за допомогою мови програмування Python та бібліотеки python-telegram-bot.

## Налаштування

Щоб налаштувати бота, необхідно виконати наступні кроки:

1. Клонуйте цей репозиторій на свій локальний комп'ютер.
2. Створіть нового бота в Telegram за допомогою BotFather та отримайте API-токен.
3. Встановіть API-токен як змінну середовища з назвою `TELEGRAM_BOT_TOKEN` на своєму локальному комп'ютері.
4. Встановіть необхідні залежності, виконавши команду `pip install -r requirements.txt`.
5. Запустіть бота, виконавши команду `python bot.py`.

## Розгортання на Heroku

Щоб розгорнути бота на Heroku, слід виконати наступні кроки:

1. Зареєструйтеся на безкоштовному обліковому записі Heroku за посиланням https://signup.heroku.com/.
2. Встановіть Heroku CLI, дотримуючись інструкцій за посиланням https://devcenter.heroku.com/articles/heroku-cli.
3. Клонуйте цей репозиторій на свій локальний комп'ютер.
4. Створіть нового бота в Telegram за допомогою BotFather та отримайте API-токен.
5. Встановіть API-токен як змінну середовища з назвою `TELEGRAM_BOT_TOKEN` на Heroku.
6. Запустіть розгортування бота на Heroku, виконавши команду `git push heroku master`.
7. Запустіть бота на Heroku, виконавши команду `heroku ps:scale worker=1`.
8. Налаштуйте веб-хук для бота, виконавши команду `heroku ps:scale worker=0` і встановивши змінну середовища з назвою `WEBHOOK_URL` з URL-адресою веб-хуку на Heroku.
