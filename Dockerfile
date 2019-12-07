FROM  python:3.7-slim-buster
ENV LOG_LEVEL=WARN
COPY ./ ./
RUN pip install pipenv
RUN pipenv run python setup.py install
RUN pipenv install
ENTRYPOINT [ "pipenv", "run", "dragonfly", "-h"]