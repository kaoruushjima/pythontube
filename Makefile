migrate:
	python pythontube/manage.py makemigrations users posts
	python pythontube/manage.py migrate
