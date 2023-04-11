# Project Description


## How to set up.
- Create a postgres database.
- Clone the repo.
- Ensure you are on the dev branch.
- Create a `.env` file from the `.env_example`.
- Run command `python create_tables.py`. This runs the code in the file `create_tables.py` which creates the necessary tables for the application to work.

## Run application
- Run the command `python manage.py runserver`.

#### Expected output
```
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:8000/articleshub/home.html/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 125-482-972
 ```

- Use postman to interact with application.

Project Overview
--------------------------------
|Endpoint |Functionality |Note |
|---------|:------------:|:---:|
|POST /auth/signup|Register a user| |
|POST /auth/login |Login a user | |

## Built With

* `Django` : [Django](https://www.djangoproject.com/) is  a high-level Python web framework that encourages rapid development and clean, pragmatic design.
* `html` : [html](https://html.com/) is the standard markup language for Web pages.
* `css` : [css](https://www.w3.org/) is the language we use to style an HTML document

## Authors

* **Alexey Chemlev** - [Github](https://github.com/CHEMLEV)
* **Rosalind Martina Cervante** - [Github](https://github.com/rozzlethegreat)
* **Thi Thuy Trinh Nguyen** - [Github](https://github.com/trinhnguyen212)
* **Keita Morioka** - [Email](20220601@mywhitecliffe.com)
* **Mei-Hsiu Chen** - [Github](https://github.com/MeiHsiu)
