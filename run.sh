#!/bin/sh
export APP_MODULE=${APP_MODULE-notable.main:app}

python3 notable/prestart.py
python3 notable/insert_initial_data.py
exec uvicorn "$APP_MODULE" --reload
