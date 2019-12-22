FROM python:3.7-slim

WORKDIR /chip-multi

COPY . /chip-multi

RUN apt-get update && apt-get install -y \
    tree \
    vim
RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.python.org -r requirements.txt

RUN chmod a+x /chip-multi/api/entrypoint-api.sh \
    && chmod a+x /chip-multi/src/entrypoint-job.sh