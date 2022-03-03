FROM archlinux

USER root

RUN pacman --noconfirm -Sy python3
RUN pacman --noconfirm -Sy python-pip
#RUN pacman --noconfirm -S pypy
#RUN pacman --noconfirm -S pypy
#RUN pacman --noconfirm -S pypy

COPY requirements.txt /tmp/requirements.txt 
RUN pip3 install -r /tmp/requirements.txt

ADD . /usr/src/app
WORKDIR /urs/src/app


CMD ["/usr/src/app/run.py"]

