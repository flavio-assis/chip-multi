FROM python:3.7-slim

WORKDIR /chip-multi

COPY . /chip-multi

RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN apt-get update && apt-get install -y \
    tree \
    vim

CMD ["python3", "__main__.py"]