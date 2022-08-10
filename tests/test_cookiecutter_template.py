import pathlib
from cookiecutter.main import cookiecutter


DIR = str(pathlib.Path(__file__).parent.parent)


def test_custom_project(tmpdir):
    """Test for 'cookiecutter-template'."""
    cookiecutter(
        template=DIR,
        output_dir=str(tmpdir),
        no_input=True,
        extra_context={
            "python_version": "3.10",
        },
    )
    p = pathlib.Path(tmpdir)
    paths = [str(r.relative_to(p)) for r in p.glob("**/")]
    paths.remove(".")
    assert paths == [
        "cookiecutter_template",
        "cookiecutter_template\\.circleci",
        "cookiecutter_template\\.github",
        "cookiecutter_template\\.github\\workflows",
        "cookiecutter_template\\cookiecutter_template",
        "cookiecutter_template\\cookiecutter_template\\db",
        "cookiecutter_template\\cookiecutter_template\\modelling",
        "cookiecutter_template\\cookiecutter_template\\utils",
        "cookiecutter_template\\docs",
        "cookiecutter_template\\docs\\source",
        "cookiecutter_template\\tests",
        "cookiecutter_template\\tests\\__pycache__",
    ]
