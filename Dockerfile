FROM glotzerlab/software
USER root
RUN python3 -m pip install git+https://github.com/glotzerlab/signac-dashboard.git@93625886ef12edc223c2d8b8dd289947e8f80a5c
COPY dashboard.py /
ENTRYPOINT python3 dashboard.py run --port=8080
