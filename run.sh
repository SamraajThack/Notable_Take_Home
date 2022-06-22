#!/bin/sh
export APP_MODULE=${APP_MODULE-notable.main:app}
exec uvicorn "$APP_MODULE" --reload