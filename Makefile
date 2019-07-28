runserver:
	./source/manage.py runserver

migrate:
	./source/manage.py migrate

test:
	cd ./source && pytest --cov

rodar_verificacoes:
	./source/manage.py rodar_verificacoes

