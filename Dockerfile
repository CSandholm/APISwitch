# Version of Python
FROM python:3.10

# Working directory
WORKDIR /code

# Copy requirements into the working directory so it gets cached by itself
COPY ./requirements.txt /code/requirements.txt

# Install the dependencies from the reuirements file
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the code into the working directory
COPY ./app /code/app

# Set environment variable for Python path
ENV PYTHONPATH="/code/app"

# Tell uvicorn to start which will be running inside the container
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]