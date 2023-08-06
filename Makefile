setup:
	python3 -m pip install -r requirements.txt
	cd backend/restless && \
	python3 manage.py makemigrations && \
	python3 manage.py makemigrations quotes && \
	python3 manage.py makemigrations users && \
	python3 manage.py migrate --database=users && \
	python3 manage.py migrate --database=quotes && \
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