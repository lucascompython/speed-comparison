FROM archlinux

USER root

RUN pacman --noconfirm -Sy yay python3 python-pip nodejs deno gcc jdk-openjdk pypy3 dotnet-sdk lua php ruby go rust time
RUN yay -S --noconfirm swift-bin powershell-bin

COPY requirements.txt /tmp/requirements.txt 
RUN pip3 install -r /tmp/requirements.txt

ADD . /usr/src/app
WORKDIR /usr/src/app
ENV NO_COLOR=true
ENV DOCKER=true

CMD ["python3", "/usr/src/app/comparison.py", "-n"]

