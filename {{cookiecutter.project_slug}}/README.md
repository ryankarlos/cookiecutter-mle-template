
{% if cookiecutter.add_badges %}
![python-version](https://img.shields.io/badge/Python-{{cookiecutter.python_version}}-green)
[![tests](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/actions/workflows/tests.yml/badge.svg?branch=master)](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/actions)
{% endif %}


{{ cookiecutter.project_name }}
==============================

{{ cookiecutter.project_short_description }}
