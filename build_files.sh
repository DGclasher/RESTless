#!/bin/bash

echo "STATIC BUILD START"
python3 -m pip install -r requirements.txt
python3 manage.py collectstatic --noinput
echo "STATIC BUILD DONE"
