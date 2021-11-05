# ecom-demo
-----------------------------------------
We are going to build an eCommerce Website using Django with production-level code.
Will try to add the documentation and testing part too. So, stay tuned!

## Setup

- The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/nitesh585/ecom-demo.git
$ cd ecom-demo
```

- Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv venv
$ . venv/bin/activate
```

- Then install the dependencies:

```sh
(venv)$ pip install -r requirements.txt
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

- Once `pip` has finished downloading the dependencies:
```sh
(venv)$ python manage.py runserver
```
- And navigate to `http://127.0.0.1:8000/`.

--------------
#### Any PR and issues are most welcome 😊
