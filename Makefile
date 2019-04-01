.PHONY: clean clean-test clean-pyc clean-build docs help output
.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

lint: ## check style with flake8
	flake8 yield_curve_dynamics tests

test: ## run tests quickly with the default Python
	python setup.py test

test-all: ## run tests on every Python version with tox
	tox

download: ## Download raw yield curve data parameters from ECB
	yield_curve_dynamics download -s 2009-01-01 -e 2018-12-31 -f data/ecb_data.zip

data/ecb_data.zip: download

transform: data/ecb_data.zip ## Load data as provided by ECB and transform to parameters CSV
	yield_curve_dynamics transform -i data/ecb_data.zip -o data/euryieldcurve.csv

video: data/euryieldcurve.csv ## Load CSV file and create a yield curve video
	yield_curve_dynamics video -f data/euryieldcurve.csv -o output/euryieldcurve.mp4 -n 250 -m 40

presentation: ## create a HTML presentation from notebook
	jupyter nbconvert notebooks/Yield\ Curve\ Dynamics.ipynb --to slides --output-dir output

output: presentation video ## generate all output files

coverage: ## check code coverage quickly with the default Python
	coverage run --source yield_curve_dynamics setup.py test
	coverage report -m
	coverage html
	$(BROWSER) htmlcov/index.html

docs: ## generate Sphinx HTML documentation, including API docs
	rm -f docs/yield_curve_dynamics.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ yield_curve_dynamics
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html

servedocs: docs ## compile the docs watching for changes
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

release: dist ## package and upload a release
	twine upload dist/*

dist: clean ## builds source and wheel package
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

install: clean ## install the package to the active Python's site-packages
	python setup.py install
