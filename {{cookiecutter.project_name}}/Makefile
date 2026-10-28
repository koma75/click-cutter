.DEFAULT_GOAL := build
.PHONY: build freeze publish package pubtest clean venv install
PROJ_NAME = {{cookiecutter.package_name}}
PY_VERSION = {{cookiecutter.python_ver}}
SHELL = bash


build: venv
	uv pip install --editable .

freeze:
	@uv pip freeze > requirements.txt

package: clean
	@uv build

publish: package
	@uv run twine upload dist/*

pubtest: package
	@uv run twine upload --repository pypitest dist/*

clean :
	rm -rf dist *.egg-info

venv:
	@uv venv --python $(PY_VERSION) .venv

install:
	@uv pip install -r requirements.txt
