setup:
	cd backend/restless
	python3 -m pip install -r requirements.txt && \
	python3 manage.py migrate --noinput && \
	python3 manage.py migrate --run-syncdb

serve:
	cd backend/restless && \
	python3 manage.py runserver

serve-bg:
	cd backend/restless && \
	python3 manage.py runserver &

test:
	python3 -m pytest -v

stop:
	kill $(lsof -t -i:8000)