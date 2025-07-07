FROM python:3.9-alpine
WORKDIR /flask_app
COPY requirement.txt .
RUN pip install --no-cache-dir -r requirement.txt
RUN pip install pytest
COPY /app .
COPY  /tests /app/tests/
CMD ["python", "app.py"]


