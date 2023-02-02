# Contribute to RESTless

## Steps to perform

+ Fork this repository

+ Clone the forked repository
  ```
  git clone git@github.com:[YOUR USERNAME]/RESTless.git
  ```

+ Change your directory to backend/restless

+ Install the requirements
  ```
  pip install -r requirements.txt
  ```

+ Make the required migrations
  ```
  python manage.py makemigrations
  ```
  ```
  python manage.py migrate
  ```
  ```
  python manage.py migrate --run-syncdb
  ```

+ To run the server
  ```
  python manage.py runserver
  ```

## API docs are available [here](api.md)