# Use an official Python runtime as a parent image
FROM continuumio/miniconda3

RUN apt-get --allow-releaseinfo-change update
RUN apt-get install -y build-essential 

RUN mkdir /tmp/cellmaps_ppidownloader
COPY ./ /tmp/cellmaps_ppidownloader/
RUN pip install /tmp/cellmaps_ppidownloader

RUN rm -rf /tmp/cellmaps_ppidownloader

ENTRYPOINT ["/opt/conda/bin/cellmaps_ppidownloadercmd.py"]

CMD ["--help"]
