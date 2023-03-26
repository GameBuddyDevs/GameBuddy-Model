FROM python:3.10.9

WORKDIR /usr/local/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 4567

CMD [ "python", "GameBuddy-ModelApi/api/main.py" ]