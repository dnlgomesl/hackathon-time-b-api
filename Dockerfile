FROM python:3.8-slim-buster

ARG OPENAI_KEY
ARG ASSISTANT_ID

ENV OPENAI_KEY=$OPENAI_KEY
ENV ASSISTANT_ID=$ASSISTANT_ID

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD ["src/__main__.py"]