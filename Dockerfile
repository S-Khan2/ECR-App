FROM public.ecr.aws/docker/library/python:3.10.8-alpine3.16

WORKDIR /usr/src/app

COPY website/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY website/ .
EXPOSE 8080

CMD [ "python", "main.py" ]