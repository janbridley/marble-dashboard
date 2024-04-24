FROM mambaorg/micromamba:1.5.8
COPY --chown=$MAMBA_USER:$MAMBA_USER env.yaml /tmp/env.yaml
RUN micromamba install -y -n base -f /tmp/env.yaml
RUN micromamba clean --all --yes

ARG MAMBA_DOCKERFILE_ACTIVATE=1

RUN micromamba install -c conda-forge signac-dashboard -y

RUN which python
RUN pwd
RUN ls /opt/conda
RUN ls /opt/conda/bin

COPY dashboard.py /
ENTRYPOINT /opt/conda/bin/python dashboard.py run --port=8080