FROM python:3.8

LABEL maintainer="Yannic Nevado <nevado-git@magenta.de>"

WORKDIR /usr/src/api

RUN apt-get update \
	&& apt-get install python3-dev vim -y

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]