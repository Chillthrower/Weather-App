FROM python:3

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install default-libmysqlclient-dev
RUN apt-get update \
    && apt-get install -y default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/* \
    && pip install mysqlclient

COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

# Expose port 8000
EXPOSE 8000

# Run the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
