migrate:
	python pythontube/manage.py makemigrations users posts
	python pythontube/manage.py migrate

test:
	pycodestyle .
	python pythontube/manage.py test users posts -v2
