env:
	cd SimpleTapBot
	python3.10 -m venv .venv
	source .venv/bin/activate
	pip3 install --upgrade pip setuptools wheel
	pip3 install -r requirements.txt
	cp .env-example .env
	nano .env
session:
	python main.py --action 1
run:
	python main.py --action 2
