# Contribute to RESTless

## Steps to perform

+ Fork this repository
+ Clone the forked repository
  ```
  git clone git@github.com:[YOUR USERNAME]/RESTless.git
  ```
+ Create python virtual environment and activate
  ```
  python3 -m venv venv && source venv/bin/activate
  ```
+ Install dependencies
  ```
  pip install -r requirements.txt
  ```

+ Create a super user using `python3 manage.py createsuper user`, then in an `.env` file in the root directory of project, refer `.env` file to [this](../.env.example).
  
+ Migrate DB
  ```
  python manage.py migrate
  ```
+ Run server
  ```
  python manage.py runserver
  ```
+ To run tests
  ```
  cd tests; pytest -v
  ```

#### API docs are available [here](./api.md)