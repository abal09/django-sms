install:
	python setup.py develop --upgrade
	pip install -r example/requirements.txt

test:
	cd example && python manage.py test sms
