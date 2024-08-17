[<img src="https://img.shields.io/badge/python-3.10%20%7C%203.11-blue">](https://www.python.org/downloads/)

# SimpleTapBot

- Собирает монеты
- Кликает и выполняет задания
- Крутит колесо
- Собирает награды за рефералов
- Собирает карты в коллекциях

# 📕 Установка

`git clone <репа>`

`cd SimpleTapBot`

`make env`

`make session`

`make run`



_или так:_

`git clone <репа>`

`cd SimpleTapBot`

`python3.10 -m venv .venv`

`source .venv/bin/activate`

`pip3 install --upgrade pip setuptools wheel`

`pip3 install -r requirements.txt`

`cp .env-example .env`

`nano .env`

Отредактировать и сохранить .env файл

# ⚙ Настройки
_все настройки хранятся в файле .env_

| Настройка                   | Описание                                                                                 |
|-----------------------------|------------------------------------------------------------------------------------------|
| **API_ID / API_HASH**       | Данные платформы, с которой запускать сессию Telegram _брать на https://my.telegram.org_ |
| **TAPS_AMOUNT**             | количество тапов, _например [5,8]_                                                       |
| **SLEEP_AFTER_TAP**         | Задержка после серии тапов в секундах _например 2_                                       |
| **SLEEP_NOT_ENOUGH_TAPS**   | Задержка после расхода тапов в секундах, _например [2000, 3600]_                         |
| **SPIN_THE_WHEEL**          | Крутить колесо (True / False), по умолчанию _True_                                       |
| **CLAIM_REFERRALS_REWARD**  | Собирать награды за рефералов (True / False), по умолчанию _True_                        |
| **CLAIM_COLLECTIONS_CARDS** | Собирать карты из коллекций (True / False), по умолчанию _True_                          |
| **UPGRADE_CARDS**           | Улучшать карты (True / False), _пока не работает)_                                       |



# ⚡ Запуск 
`python main.py`

_или_

добавление сессии:

`python main.py --action 1`

запуск бота:

`python main.py --action 2`
