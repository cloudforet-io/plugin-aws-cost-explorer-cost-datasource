FROM cloudforet/python-core:2

ENV PYTHONUNBUFFERED=1
ENV CLOUDONE_PORT=50051
ENV SERVER_TYPE=grpc
ENV PKG_DIR=/tmp/pkg
ENV SRC_DIR=/tmp/src

RUN apt update && apt upgrade -y

COPY pkg/*.txt ${PKG_DIR}/
RUN pip install --upgrade pip && \
    pip install --upgrade -r ${PKG_DIR}/pip_requirements.txt

COPY src ${SRC_DIR}

WORKDIR ${SRC_DIR}
RUN python3 setup.py install && \
    rm -rf /tmp/*

EXPOSE ${CLOUDONE_PORT}

ENTRYPOINT ["spaceone"]
CMD ["run", "grpc-server", "cloudforet.cost_analysis"]
