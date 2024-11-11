FROM python:3.13
WORKDIR /cupcake_app
COPY . /app.py
RUN pip install -r requirements.txt
CMD ["flask", "run", "--host=0.0.0.0"]
