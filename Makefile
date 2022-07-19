#!make

runserver:
	uvicorn api.main:app --reload

dc-up:
	sudo docker-compose up -d

dc-down:
	sudo docker-compose down

dc-logs:
	sudo docker logs pneumonia_fastapi