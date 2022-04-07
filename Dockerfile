FROM archlinux

USER root

RUN pacman --noconfirm -Sy python3 python-pip nodejs deno gcc jdk-openjdk
#RUN pacman --noconfirm -Sy python-pip
#RUN pacman --noconfirm -Sy nodejs
#RUN pacman --noconfirm -Sy deno
#RUN pacman --noconfirm -Sy gcc
#RUN pacman --noconfirm -Sy tk

#get GNU Time
RUN pacman --noconfirm -Sy time
#RUN pacman --noconfirm -S pypy
#RUN pacman --noconfirm -S pypy
#RUN pacman --noconfirm -S pypy

COPY requirements.txt /tmp/requirements.txt 
RUN pip3 install -r /tmp/requirements.txt

ADD . /usr/src/app
WORKDIR /usr/src/app
ENV NO_COLOR=true


CMD ["python3", "/usr/src/app/comparison.py"]

