FROM praqma/helmsman:v3.4.4-helm-v3.2.4

RUN helm version

# Install git secret
RUN apk add --update --no-cache gawk
RUN git --version

# Install Java
RUN apk add openjdk11
RUN java --version
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk
ENV PATH="$JAVA_HOME/bin:${PATH}"

# Install python and python related dependencies
RUN apk add --update --no-cache python3 py3-pip
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade toml
RUN pip3 install --upgrade pyyaml
RUN pip3 install --upgrade awscli
RUN aws --version

# Add the toml-parser for Helmsman
WORKDIR /tmp
ADD dsf-updater.py /tmp

# Test that the toml-parser works
ADD test-env /tmp/test-env
RUN python3 dsf-updater.py test-app 0.1 test-env dsf-test.toml
RUN rm -rf /tmp/test-env
# End testing
