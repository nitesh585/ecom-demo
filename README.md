<p align="center" style="font-size:48px; font-weight:550" > ecom-demo</p>

[Ecom-Demo-Preview](https://drive.google.com/file/d/12eHbRAD4pYCgHngu_gJ678hgK7oYwgxk/view?usp=sharing)

-----------------------------------------
This is a baseline eCommerce application that you can use to build your own online store.
Used frameworks/languages and tools are:
|                                                                                                                                                               |                                                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                                                               |
| <img style="width:15px" src="https://img.stackshare.io/service/994/4aGjtNQv.png"> Django                                                                      | <img style="width:15px" src="https://www.drupal.org/files/project-images/screenshot_361.png"> Tailwind CSS                                                            |
| <img style="width:15px" src="https://avatars.githubusercontent.com/u/2918581?s=200&v=4"> Bootstrap                                                            | <img style="width:15px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1024px-Python-logo-notext.svg.png"> Python              |
| <img style="width:15px" src="https://docs.pytest.org/en/stable/_static/pytest1.png"> Pytest                                                                   | <img style="width:15px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/javascript/javascript.png"> Javascript  |
| <img style="width:15px" src="https://avatars.githubusercontent.com/u/70142?s=200&v=4"> Jquery                                                                 | <img style="height:15px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/HTML5_logo_and_wordmark.svg/1200px-HTML5_logo_and_wordmark.svg.png"> HTML     |
| <img style="width:15px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/CSS3_logo_and_wordmark.svg/1200px-CSS3_logo_and_wordmark.svg.png"> CSS | <img style="width:15px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/Sqlite-square-icon.svg/2048px-Sqlite-square-icon.svg.png"> SQLite              |
| <img style="width:15px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Git_icon.svg/2048px-Git_icon.svg.png"> Git                             | <img style="width:15px" src="https://upload.wikimedia.org/wikipedia/en/thumb/e/eb/Stripe_logo%2C_revised_2016.png/1024px-Stripe_logo%2C_revised_2016.png"> Stripe API |

--------------------------------------------------
Table of Content:
- [Guide to run the project](#guide-to-run-the-project)
  - [Virtual environment setup](#virtual-environment-setup)
  - [Database setup](#database-setup)
  - [Create admin user](#create-admin-user)
  - [Tailwind CSS setup](#tailwind-css-setup)
  - [Final step](#final-step)

--------------------------------------------------
## Guide to run the project

- The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/nitesh585/ecom-demo.git
$ cd ecom-demo
```
----------------------------------------------------
### Virtual environment setup

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

Once `pip` has finished downloading the dependencies:

----------------------------------------------------------
### Database setup
- Create the migrations (generate the SQL commands) according to defined models in each and every apps.
```sh
> python manage.py makemigrations
```

- Run the migrations (execute the SQL commands).
```sh
> python manage.py migrate
```
So, we done with databases. All the tables are created according to the schemas defined in model files

---------------------------------------------
### Create admin user
You can create a "superuser" account that has full access to the site and all needed permissions using manage.py.

Call the following command, in the same directory as manage.py, to create the superuser. You will be prompted to enter a username, email address, and strong password.

```sh
> python manage.py createsuperuser
```
---------------------------------------------
### Tailwind CSS setup
Create a new directory within your Django project, in which you'll install tailwindCSS like in any vanilla JS project setup:
```
> mkdir jstool && cd jstool
> npm init -y && npm install tailwindcss autoprefixer clean-css-cli && npx tailwindcss init -p
```

open the package.json and add build script to it.
```
...
"scripts": {
  "build": "tailwind build ../static/css/tailwind.css -o ../static/css/style.css && cleancss -o ../static/css/style.min.css ../static/css/style.css"
},
...
```

tailwind.config.js should be something like this:
```
module.exports = {
    future: {
        removeDeprecatedGapUtilities: true,
        purgeLayersByDefault: true,
    },
    purge: {
        enabled: false, //true for production build
        content: [
            '../**/templates/*.html',
            '../**/templates/**/*.html'
        ]
    },
    theme: {
        extend: {},
    },
    variants: {},
    plugins: [],
}
```
now make a Tailwind entry point in static/css/tailwind.css
```
@tailwind base;
@tailwind components;
@tailwind utilities;
```

We are ready to build.
```
> npm run build
```
This command will generate two files: styles.css and styles.min.css

Link styles.min.css to your templates and enjoy.

---------------------------------------------
### Final step
- Run the application server (only for developement)
```sh
> python manage.py runserver
```
- And navigate to `http://127.0.0.1:8000/`.

Yupeee! it's up and running 😃🤩 

----------------------------------------------
Any PR and issues are most welcome 😊
