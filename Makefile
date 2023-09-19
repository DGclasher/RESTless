setup:
	cd backend/restless
	python -m pip install -r requirements.txt && \
	python manage.py migrate --noinput && \

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
