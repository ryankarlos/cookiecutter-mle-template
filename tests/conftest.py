from pathlib import Path
import shutil

from cookiecutter.main import cookiecutter
import pytest

DIR = str(Path(__file__).parent.parent)


params = {
    "full_name": "Cookie Monster",
    "email": "cookie@gmail.com",
    "github_username": "cookie",
    "project_name": "Making Cookies",
    "author_name": "cookie monster",
    "python_version": "3.10",
}


@pytest.fixture(scope="session", params=[params])
def default_cookie_project(tmp_path_factory, request):
    fn = tmp_path_factory.mktemp("project")
    out_dir = fn.resolve()
    cookiecutter(
        template=DIR,
        output_dir=out_dir,
        no_input=True,
        extra_context=request.param,
    )
    yield fn

    shutil.rmtree(out_dir)
