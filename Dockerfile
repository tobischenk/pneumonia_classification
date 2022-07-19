FROM python:3.9
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./api /app/api
COPY ./api/main.py /app/
COPY ./models /app/models

# Install dependecies for cv2, which might not be installed in Docker by default
RUN apt-get update && apt-get install libgl1 -y

# Start uvicorn on port 80
ENTRYPOINT ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "80"]

