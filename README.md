# Notable Appointment Scheduler

Making doctors' and patients' lives easier

Please use notable_take_home_final.zip, previous file had 'import uvicorngit' instead of 'import uvicorn' please excuse that, nothing else has changed

## Summary
I used the modern python API solution FastAPI as my framework of choice and a SQLite Database with the SQLAlchemy ORM. I tried to implement a proper folder structure (db, schema, models, crud_middleware)  and data validation techniques with basic error handling

## Installation and Running the application
The application runs on a package management tool called poetry. SQLite also will need to be downloaded, all modern Mac OS have SQLite pre-installed.

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install poetry.

```bash
pip install poetry
```

In the notable_take_home directory, you will see a notable folder that contains the source code and the pyproject.toml file which has all the dependencies

In the notable_take_home directory, install the dependencies with 
```bash
poetry install
```
Run the command 

```bash
poetry run ./run.sh
```
which initializes the SQLite database, adds some initial data, and starts the server
(usually at default: http://127.0.0.1:8000)

## Usage

FastAPI provides an interactive interface to test out API. Visit /docs from the local server (ex. http://127.0.0.1:8000/docs). This is what I used during development but you can use Postman or any other RestAPI client. 

The usage of data and time is very primitive and basic given time constraints. It gets added as a string and the format has to be - date: 'YYYY-MM-DD', time : HH: MM with a 24hr format


## Notes and Basic Further Implementation

- FastAPI is very good at high-performance async processing, I tried to implement it but couldn't in time with the DB
- Using proper date and time objects. SQLite does not have support have built-in support for date and time which is where I had some obstacles
- Improve the folder structure better, add API versioning
- Better documentation, I have barely used any comments under the time constraint
- Sophisticated error handling and considering more edge cases
- Containerization using Docker or other tools

