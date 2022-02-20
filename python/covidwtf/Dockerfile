FROM ubuntu:18.04
ARG CHROME_VERSION=97.0.4692.36

RUN apt update && apt install -y \
        curl \
        python3.6 \
        python3-pip \
        python3-setuptools

RUN curl -k --silent --location --show-error https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
        --output /tmp/google-chrome-stable_current_amd64.deb \
        && apt install -y /tmp/google-chrome-stable_current_amd64.deb
RUN curl -k --silent --location --show-error https://chromedriver.storage.googleapis.com/${CHROME_VERSION}/chromedriver_linux64.zip \
        --output /tmp/chromedriver_linux64.zip \
        && unzip /tmp/chromedriver_linux64.zip -d /usr/local/bin/ \
        && chmod 755 /usr/local/bin/chromedriver

COPY . /opt/covidwtf/
RUN pip3 install -r /opt/covidwtf/requirements.txt

CMD ["python3", "/opt/covidwtf/covidwtf.py"]
