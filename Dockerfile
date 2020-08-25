FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
WORKDIR /
# RUN mkdir card_game_backend
COPY ./app /app/app
WORKDIR /app/app
RUN pip install -r requirements.txt
