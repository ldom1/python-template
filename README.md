# Python template

This is a b template for Python projects develop to facilitate the creation of new projects following the best practices in the Python community.

This template can be used as a starting point for new projects.

## Table of contents

- [I - Features](#i---features)
- [II - How to use](#ii---how-to-use)
- [III - References](#iii---references)

## I - Features

### FAST API

This template uses [FAST API](https://fastapi.tiangolo.com/) to create the API. It is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

### Docker

This template uses [Docker](https://www.docker.com/) to containerize the application. Docker is a set of platform as a service products that use OS-level virtualization to deliver software in packages called containers.

### Poetry

This template uses [Poetry](https://python-poetry.org/) to manage the dependencies. Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you.

### MongoDB

This template uses [MongoDB](https://www.mongodb.com/) as database. MongoDB is a general purpose, document-based, distributed database built for modern application developers and for the cloud era.

### Amazon S3

This template uses [Amazon S3](https://aws.amazon.com/s3/) to store the files. Amazon S3 or Amazon Simple Storage Service is a service offered by Amazon Web Services that provides object storage through a web service interface.

### Sphinx

This template uses [Sphinx](https://www.sphinx-doc.org/en/master/) to generate the documentation. Sphinx is a tool that makes it easy to create intelligent and beautiful documentation, written by Georg Brandl and licensed under the BSD license.

### Testing

#### Pytest

This template uses [Pytest](https://docs.pytest.org/en/stable/) to test the code. The pytest framework makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries.

We use also pytest-cov to generate the coverage report.

#### Docker in Docker for integration testing

This template uses [Docker in Docker](https://www.docker.com/blog/docker-can-now-run-within-docker/) to run the integration tests. Docker can now run within Docker. This is a feature that allows you to run Docker containers as part of your Docker build CI/CD pipeline. See section [Github Actions](#github-actions) for more details.

Indeed, if you run the tests/integration, we need to have the FastAPI server running. We can use Docker to run the FastAPI server in a container and then run the tests in another container, the github action runner.

You can see the configuration in the file `.github/workflows/git_ci.yml`.

### Pre-commit

This template uses [Pre-commit](https://pre-commit.com/) to run some checks before commiting the code. pre-commit is a framework for managing and maintaining multi-language pre-commit hooks. The pre-commit hooks are run in the order given, and if any of them fail, the commit is aborted.

### Github Actions

This template uses [Github Actions](https://docs.github.com/en/actions) to automate the workflow. GitHub Actions makes it easy to automate all your software workflows, now with world-class CI/CD. Build, test, and deploy your code right from GitHub. Make code reviews, branch management, and issue triaging work the way you want.

### Logging

This template uses [Loguru](https://loguru.readthedocs.io/en/stable/) to log the messages. Loguru is a library which aims to bring enjoyable logging in Python. By adding a simple and powerful configuration, it allows to have a more human-friendly logging.

### Linting & Formatting

#### Flake8

This template uses [Flake8](https://flake8.pycqa.org/en/latest/) to lint the code. Flake8 is a wrapper around these tools:

#### Black

This template uses [Black](https://black.readthedocs.io/en/stable/) to format the code. Black is the uncompromising Python code formatter. By using it, you agree to cede control over minutiae of hand-formatting. In return, Black gives you speed, determinism, and freedom from pycodestyle nagging about formatting. You will save time and mental energy for more important matters.

#### Isort

This template uses [Isort](https://pycqa.github.io/isort/) to sort the imports. isort is a Python utility / library to sort imports alphabetically, and automatically separated into sections and by type. It provides a command line utility, Python library and plugins for various editors to quickly sort all your imports.

#### Pylint

This template uses [Pylint](https://www.pylint.org/) to lint the code. Pylint is a tool that checks for errors in Python code, tries to enforce a coding standard and looks for code smells.


## II - How to use

### Requirements

- Python 3.9+
- Poetry 1.6.1+
- Pyenv 2.3.0+

### Installation

1. **Clone this repository**

```bash
git clone https://github.com/ldom1/python-template.git
```

2. **Create a new repository in github**

3. **Change the remote url to the new repository**

```bash
git remote set-url origin
```

4. **Change the name of the project in the following files:**

- README.md
- pyproject.toml
- Makefile
- python_template/config.py

5. **Install the dependencies and create the virtual environment**

NB: I prefer to create my virtual environment in the project folder. If you prefer to create it in another folder, you can ignore this step and let poetry create the virtual environment in the default folder.

```bash
poetry config virtualenvs.in-project true
```

Then run the following commands:

```bash
pyenv install 3.10.11
pyenv shell 3.10.11
poetry env use python
source .venv/bin/activate
poetry install
pre-commit install
```

6. **Start coding!**

## III - References

This template is partely based on the following articles:

- [Creating A Modern Python Development Environment](https://itnext.io/creating-a-modern-python-development-environment-3d383c944877)
- [Automated Project Documentation — Python](https://python.plainenglish.io/automated-project-documentation-python-f880f19ad13b)
- [Pytest In Practice: Fundamentals of Python Testing Techniques](https://python.plainenglish.io/pytest-in-practice-fundamentals-of-python-testing-techniques-69f299aef09e)
- [🐍 Python Backend Project Advanced Setup (FastAPI Example)](https://python.plainenglish.io/python-backend-project-advanced-setup-fastapi-example-7b7e73a52aec)
- [4 Tools to Add to Your Python Project Before Shipping to Production](https://levelup.gitconnected.com/4-tools-to-add-to-your-python-project-before-shipping-to-production-c324f2fb8444)
- [Blazing fast Python Docker builds with Poetry](https://medium.com/@albertazzir/blazing-fast-python-docker-builds-with-poetry-a78a66f5aed0)

NB: Congratulations to the authors of the articles above for the quality of their work.