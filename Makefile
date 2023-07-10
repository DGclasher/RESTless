setup:
	python3 -m pip install -r requirements.txt
	cd backend/restless && \
	python3 manage.py makemigrations && \
	python3 manage.py migrate && \
	python3 manage.py migrate --run-syncdb

serve:
	cd backend/restless && \
	python3 manage.py runserver

serve-bg:
	cd backend/restless && \
	python3 manage.py runserver &