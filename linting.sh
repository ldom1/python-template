poetry run isort python_template
poetry run black python_template
poetry run pylint python_template --rcfile=pylintrc -j=0 --fail-under=9.5 --output=pylint-report.txt --output-format=text
poetry run flake8 python_template