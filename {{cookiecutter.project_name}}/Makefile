.DEFAULT_GOAL := build
.PHONY: build freeze publish package publish pubtest clean venv install
PROJ_NAME = {{cookiecutter.package_name}}
PY_VERSION = {{cookiecutter.python_ver}}
SHELL = bash


build: venv
	pip install --editable .

freeze:
	pip freeze > requirements.txt

package: clean
	python setup.py sdist

publish: package
	twine upload dist/*

pubtest: package
	twine upload --repository pypitest dist/*

clean :
	rm -rf dist \
	rm -rf *.egg-info

venv: .venv
	source .venv/bin/activate

.venv:
	python3 -m venv .venv
	source .venv/bin/activate && pip install pip --upgrade

install:
	pip install -r requirements.txt

