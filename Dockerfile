FROM mambaorg/micromamba:1.5.8
COPY --chown=$MAMBA_USER:$MAMBA_USER env.yaml /tmp/env.yaml
RUN micromamba install -y -n base -f /tmp/env.yaml
RUN micromamba clean --all --yes

COPY dashboard.py /
ENTRYPOINT python3 dashboard.py run --port=8080