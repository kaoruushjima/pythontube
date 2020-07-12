migrate:
	python pythontube/manage.py makemigrations posts users tags
	python pythontube/manage.py migrate

test:
	pycodestyle .
	python pythontube/manage.py test users posts tags -v2
