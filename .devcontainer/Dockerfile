FROM debian:bullseye

RUN apt-get update && \
    apt-get install git -y && \
    apt update && \
    apt install wget build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev libbz2-dev liblzma-dev -y

RUN cd && \
    wget https://www.python.org/ftp/python/3.10.0/Python-3.10.0.tar.xz && \
    tar -xf Python-3.10.0.tar.xz && \
    cd Python-3.10.0 && \
    ./configure --enable-optimizations && \
    make -j$(nproc) && \
    make install

# Add pip path to .bashrc
RUN export PATH="$PATH:/root/.local"

# RUN pip install flake8 

RUN git clone https://github.com/FelixBrgm/.unix.git ~/.unix

RUN cd ~/.unix && \
    chmod 777 ./setup.sh && \
    ./setup.sh

CMD ["tail", "-f", "/dev/null"]