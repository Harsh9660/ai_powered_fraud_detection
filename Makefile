Docker:

	docker-compose up --build 
	docker-compose down
	docker-compose logs
	docker-compose ps
	docker-compose exec web python manage.py makemigrations
	docker-compose exec web python manage.py migrate
	docker-compose exec web python manage.py createsuperuser
	docker-compose exec web python manage.py runserver
	docker system prune -a

python:

	python3 manange.py makemigrations
	python3 manange.py migrate
	python3 manange.py createsuperuser
	python3 manange.py runserver

Streamlit:

	streamlit run app.py