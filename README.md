
![python-version](https://img.shields.io/badge/Python-3.10-green)
[![tests](https://github.com/ryankarlos/cookiecutter-mle-template/actions/workflows/tests.yml/badge.svg?branch=master)](https://github.com/ryankarlos/cookiecutter-mle-template/actions)


## Customised Cookiecutter Template

This repository builds a customised Machine Learning Engineering repository
template to include the following features:

* Testing setup with ``pytest``
* GitHubActions: Ready for Continuous Integration testing and other workflows
* Tox_ testing: Setup to easily test for multiple specified python versions (e.g. 3.8, 3.9, 3.10)
* Linting: Configured precommit hooks which can be setup locally to automatically lint codebase before pushing to repo.
* Sphinx_ docs: Documentation which will be published to ReadTheDocs
* Containers for dev: Using docker-compose, start container locally with all dependencies for development.
* Command line interface using Click or Argparse (optional)
* AWS setup (optional)

### Setup
------------

 Install the latest Cookiecutter if you haven't installed it yet:

    ```bash
    $ pip install cookiecutter
    ```

Then to initiate the run the following command, with the url of the repo

    ```bash
    $ cookiecutter -c  https://github.com/ryankarlos/cookiecutter-mle-template.git
    ```

### The resulting directory structure
------------
Lets assume you set the `project_name` as  `Data Science`, then the
directory structure of your new project looks like this:

```
data_science
    ├── Dockerfile
    ├── LICENSE
    ├── MANIFEST.in
    ├── Makefile
    ├── README.md
    ├── _config.yml
    ├── docker-compose.yml
    ├── docs
    │   ├── Makefile
    │   ├── authors.rst
    │   ├── conf.py
    │   ├── index.rst
    │   ├── installation.rst
    │   ├── make.bat
    │   └── readme.rst
    ├── pyproject.toml
    ├── pytest.ini
    ├── requirements.txt
    ├── requirements_dev.txt
    ├── setup.cfg
    ├── setup.py
    ├── tests
    │   ├── __init__.py
    │   ├── conftest.py
    │   └── test_data_science.py
    ├── tox.ini
    └── data_science
        ├── __init__.py
        ├── cli.py
        └── data_science.py
```


### Acknowledgements
---

This template is adapted from the ![Cookiecutter PyPackage](https://github.com/audreyfeldroy/cookiecutter-pypackage)
and  ![Cookiecutter Data Science](https://github.com/drivendata/cookiecutter-data-science.git) projects.
