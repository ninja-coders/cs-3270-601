FROM python:3.6

MAINTAINER "Michael Wright <mkwright@gmail.com>"

RUN pip install --upgrade pip && \
    pip install jupyter

WORKDIR "/notebook"

ENV TINI_VERSION v0.6.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini
ENTRYPOINT ["/usr/bin/tini", "--"]

RUN mkdir -p /.jupyter && chmod 777 /.jupyter && \
    mkdir -p /.local && chmod 777 /.local

EXPOSE 8888
CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0"]
