env:
	python3.10 -m venv .venv
	source .venv/bin/activate
	pip3 install --upgrade pip setuptools wheel
	pip3 install -r requirements.txt
	cp .env-example .env
	nano .env
session:
	source .venv/bin/activate
	python main.py --action 1
run:
	source .venv/bin/activate
	python main.py --action 2
