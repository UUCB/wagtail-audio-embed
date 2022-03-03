# Dockerfile for testing CI locally
FROM python:3.9

WORKDIR /app
COPY tests/requirements.txt setup.cfg setup.py  ./
RUN pip install --no-cache-dir -r requirements.txt && rm -rf /root/.cache
COPY wagtailaudioembed wagtailaudioembed/
COPY tests tests/
COPY manage.py pytest.ini ./
RUN python -m pytest
