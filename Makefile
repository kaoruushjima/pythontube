migrate:
	python pythontube/manage.py makemigrations users posts tags
	python pythontube/manage.py migrate

test:
	pycodestyle .
	python pythontube/manage.py test users posts tags -v2
