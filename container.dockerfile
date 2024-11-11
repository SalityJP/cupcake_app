FROM python:3.13
WORKDIR /cupcake_app
COPY . /app.py
RUN pip install -r requirements.txt
CMD ["flask", "run", "--host=127.0.0.1:5000"]
