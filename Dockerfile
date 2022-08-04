FROM glotzerlab/software
USER root
RUN python3 -m pip install -U git+https://github.com/glotzerlab/signac-dashboard.git@b9c5a2fac0ffd5567eed1345481581b2c6d73d42
COPY dashboard.py /
ENTRYPOINT python3 dashboard.py run --port=8080
