# Contribute to RESTless

## Steps to perform

+ Fork this repository

+ Clone the forked repository
  ```
  git clone git@github.com:[YOUR USERNAME]/RESTless.git
  ```

+ Create python virtual environment
  ```
  python3 -m venv venv && source venv/bin/activate
  ```
  ```
  source venv/bin/activate
  ```
+ Make the setup
  ```
  make setup
  ```

+ Create a super user using `python3 manage.py createsuper user`, then in an `.env` file in the root directory of project, refer `.env` file to [this](../.env.example)

+ Run server
  ```
  make serve
  ```

+ To run tests
  ```
  make test
  ```

#### API docs are available [here](./api.md)