FROM python:{{ cookiecutter.python_version }}-slim-bullseye
WORKDIR /usr/
COPY requirements.txt /usr/src/requirements.txt
COPY requirements-dev.txt /usr/src/requirements-dev.txt
RUN apt-get update
RUN apt-get install -y build-essential python-dev git
RUN pip install --upgrade pip setuptools wheel \
    && pip install --no-cache-dir --upgrade -r /usr/src/requirements.txt \
    && pip install --no-cache-dir --upgrade -r /usr/src/requirements-dev.txt \
    && rm -rf /root/.cache/pip
COPY {{ cookiecutter.project_slug }}/ /usr/{{ cookiecutter.project_slug }}/
COPY tests/ /usr/tests/
ENTRYPOINT ["/bin/bash"]
