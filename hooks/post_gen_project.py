#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':

    if '{{ cookiecutter.create_dev_environment }}' == "n":
        remove_file('docker-compose-dev.yml')
        remove_file('.env-dev')

    if '{{ cookiecutter.celery }}' == 'n':
        remove_file('{{ cookiecutter.project_slug }}/{{ cookiecutter.project_slug }}/celery.py')

    if '{{ cookiecutter.grafana }}' == 'n':
        shutil.rmtree('grafana', ignore_errors=True)
        shutil.rmtree('prometheus', ignore_errors=True)

