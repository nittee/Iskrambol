# Dockerfile with:
#   - Android build environment
#   - Iskrambol dependencies    
# 
# Build with:
#     docker build --tag=app --file Dockerfile .
# 
# Run with interactive shell:
#     docker run -it --rm app
# 
# Note:
#     Use 'docker run' without '--rm' flag for keeping the container and use
#     'docker commit <container hash> <new image>' to extend the original image

FROM --platform=linux/amd64 ubuntu:22.04

LABEL maintainer="jiroblea"
LABEL version="0.0.1"

# RUN echo Dockerfile is running...

# configure locale
RUN apt -y update -qq > /dev/null \
    && DEBIAN_FRONTEND=noninteractive apt install -qq --yes --no-install-recommends \
    locales && \
    locale-gen en_US.UTF-8
ENV LANG="en_US.UTF-8" \
    LANGUAGE="en_US.UTF-8" \
    LC_ALL="en_US.UTF-8"

ENV USER="user"
ENV HOME_DIR="/home/${USER}"
ENV WORK_DIR="${HOME_DIR}/app" \
    PATH="${HOME_DIR}/.local/bin:${PATH}" \
    ANDROID_HOME="${HOME_DIR}/.android"

# install system dependencies
RUN apt -y update -qq > /dev/null \
    && DEBIAN_FRONTEND=noninteractive apt install --yes \
        python3 \
        python3-dev \
        python3-pip \
        git \
        openjdk-17-jdk \
    && apt -y autoremove \
    && apt -y clean \
    && rm -rf /var/lib/apt/lists/*

# prepare non root env
RUN useradd --create-home --shell /bin/bash ${USER}

# with sudo access and no password
RUN usermod -append --groups sudo ${USER}
RUN echo "%sudo ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

WORKDIR ${WORK_DIR}
RUN mkdir ${ANDROID_HOME} && chown --recursive ${USER} ${HOME_DIR} ${ANDROID_HOME}
USER ${USER}

# install iskrambol from current branch
COPY --chown=user:user . ${WORK_DIR}

# install dependencies from requirements.txt
RUN pip install -r requirements.txt
