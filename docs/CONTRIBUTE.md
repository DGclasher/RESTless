# Contribute to RESTless

## Steps to perform

+ Fork this repository

+ Clone the forked repository
  ```
  git clone git@github.com:[YOUR USERNAME]/RESTless.git
  ```

+ Create python virtual environment
  ```
  python3 -m venv venv
  ```
  ```
  source venv/bin/activate
  ```

+ Create `.env` file in the root directory of project with following items
  ```
  TEST_USER=<a test user>
  TEST_PASS=<password of test user>
  ```

+ Make the setup
  ```
  make setup
  ```

+ Run server
  ```
  make serve
  ```

+ To run tests
  ```
  make test
  ```

#### API docs are available [here](./api.md)