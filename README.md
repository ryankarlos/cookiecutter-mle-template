## Customised Cookiecutter Template

This repository builds a customised Machine Learning Engineering repository
template to include the following features:

* Testing setup with ``pytest``
* GitHubActions: Ready for Continuous Integration testing and other workflows
* Tox_ testing: Setup to easily test for Python 3.6, 3.7, 3.8
* Sphinx_ docs: Documentation ready for generation with, for example, `Read the Docs`_
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

The directory structure of your new project looks like this: 

```
├── README.md
├── cookiecutter.json
└── {{cookiecutter.project_slug}}
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
    │   └── test_{{cookiecutter.project_slug}}.py
    ├── tox.ini
    └── {{cookiecutter.project_slug}}
        ├── __init__.py
        ├── cli.py
        └── {{cookiecutter.project_slug}}.py
```


### Acknowledgements
---

This template is adapted from the following cookiecutter repos:

1. ![Cookiecutter PyPackage](https://github.com/audreyfeldroy/cookiecutter-pypackage)
2. ![Cookiecutter Data Science](https://github.com/drivendata/cookiecutter-data-science.git)