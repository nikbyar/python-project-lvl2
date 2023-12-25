rave: build publish package-install
raveli: build publish package-install lint gendiff

install:
	poetry install


gendiff:
	poetry run gendiff file1.json file2.json


build:
	poetry build


lint:
	poetry run flake8 gendiff


package-install:
	python3 -m pip install --force-reinstall dist/*.whl

publish:
	poetry publish --dry-run
	

test:
	poetry run pytest --cov=gendiff tests/ --cov-report xml
	
	
test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
	
	
selfcheck:
	poetry check

check: selfcheck test lint


.PHONY: gendiff




