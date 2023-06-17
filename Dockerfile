FROM python:3.10.9

WORKDIR /usr/local/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --upgrade pip ipython ipykernel
RUN ipython kernel install --name "python3" --user

EXPOSE 4567

CMD ["python", "GameBuddy-ModelApi/api/main.py"]