import re


def test_custom_project_tree(default_cookie_project):
    """Test for 'cookiecutter-template'."""
    rtx = [re.compile(word) for word in ["__pycache__", "."]]
    all_paths = (
        str(r.relative_to(default_cookie_project))
        for r in default_cookie_project.glob("**/*")
    )
    paths = []
    for p in all_paths:
        for word in rtx:
            if not re.search(word, p):
                paths.append(p)

    assert paths == [
        "making_cookies",
        "making_cookies\\.circleci",
        "making_cookies\\.codecov.yml",
        "making_cookies\\.editorconfig",
        "making_cookies\\.github",
        "making_cookies\\.gitignore",
        "making_cookies\\.pre-commit-config.yaml",
        "making_cookies\\docker-compose.yml",
        "making_cookies\\Dockerfile",
        "making_cookies\\docs",
        "making_cookies\\LICENSE",
        "making_cookies\\logging.conf",
        "making_cookies\\Makefile",
        "making_cookies\\making_cookies",
        "making_cookies\\MANIFEST.in",
        "making_cookies\\pyproject.toml",
        "making_cookies\\pytest.ini",
        "making_cookies\\README.md",
        "making_cookies\\requirements.txt",
        "making_cookies\\requirements_dev.txt",
        "making_cookies\\setup.cfg",
        "making_cookies\\setup.py",
        "making_cookies\\tests",
        "making_cookies\\tox.ini",
        "making_cookies\\_config.yml",
        "making_cookies\\__init__.py",
        "making_cookies\\.circleci\\config.yml",
        "making_cookies\\.github\\workflows",
        "making_cookies\\.github\\workflows\\tests.yml",
        "making_cookies\\docs\\make.bat",
        "making_cookies\\docs\\make.sh",
        "making_cookies\\docs\\Makefile",
        "making_cookies\\docs\\source",
        "making_cookies\\docs\\source\\conf.py",
        "making_cookies\\docs\\source\\index.rst",
        "making_cookies\\docs\\source\\readme.rst",
        "making_cookies\\making_cookies\\cli.py",
        "making_cookies\\making_cookies\\db",
        "making_cookies\\making_cookies\\modelling",
        "making_cookies\\making_cookies\\py.typed",
        "making_cookies\\making_cookies\\utils",
        "making_cookies\\making_cookies\\__init__.py",
        "making_cookies\\making_cookies\\db\\orm.py",
        "making_cookies\\making_cookies\\db\\update_db.py",
        "making_cookies\\making_cookies\\db\\__init__.py",
        "making_cookies\\making_cookies\\modelling\\features.py",
        "making_cookies\\making_cookies\\modelling\\load_data.py",
        "making_cookies\\making_cookies\\modelling\\predict.py",
        "making_cookies\\making_cookies\\modelling\\train.py",
        "making_cookies\\making_cookies\\modelling\\visualize.py",
        "making_cookies\\making_cookies\\modelling\\__init__.py",
        "making_cookies\\making_cookies\\utils\\config.py",
        "making_cookies\\making_cookies\\utils\\constants.py",
        "making_cookies\\making_cookies\\utils\\__init__.py",
        "making_cookies\\tests\\conftest.py",
        "making_cookies\\tests\\test_making_cookies.py",
        "making_cookies\\tests\\__init__.py",
    ]


def test_generated_readme(default_cookie_project):

    with open(  # noqa: W605
        f"{default_cookie_project.resolve()}\\making_cookies\\README.md", "r"
    ) as fs:
        readme_txt = [x.strip("\n") for x in fs.readlines()]
        expected = list(filter(str.strip, readme_txt))

    assert expected == [
        "![python-version](https://img.shields.io/badge/Python-3.10-green)",
        "[![tests](https://github.com/cookie/making_cookies/actions/workflows/tests.yml/badge.svg?branch=master)]"
        "(https://github.com/cookie/making_cookies/actions)",
        "Making Cookies",
        "==============================",
        "MLE implementations in the cloud",
    ]
