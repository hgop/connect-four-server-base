FROM python:3.9.0-buster

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY connect4/*.py ./connect4/

CMD PYTHONPATH=. python ./connect4/app.py
