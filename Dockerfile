FROM        python:3.4-onbuild
MAINTAINER  Kotaimen <kotaimen.c@gmail.com>
ENV         DEBIAN_FRONTEND noninteractive


RUN         pip3 install .


EXPOSE      80
ENTRYPOINT  ["ironsmith"]
CMD         ["--debug", "runserver","--bind=0.0.0.0:80"]
