# SimpleTapBot

Собирает монеты, кликает и выполняет задания, крутит колесо, собирает награды за друзей.

# Установить

git clone <репа>

cd SimpleTapBot

make env

make session

make run



или так:

git clone <репа>

cd SimpleTapBot

python3.10 -m venv .venv

source .venv/bin/activate

pip3 install --upgrade pip setuptools wheel

pip3 install -r requirements.txt

cp .env-example .env


# Настройка
все настройки - в файле .env

API_ID, API_HASH - брать на https://my.telegram.org

TAPS_AMOUNT - количество тапов, например [5, 8]

SLEEP_AFTER_TAP - заддержка после тапов в секундах

SLEEP_NOT_ENOUGH_TAPS - заддержка после расхода тапов в секундах, например [2000, 3600]


# Запуск 
`python main.py`

или

добавление сессии `python main.py --action 1`

запуск бота `python main.py --action 2`
