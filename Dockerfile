FROM gcr.io/google-appengine/python
LABEL python_version=python3.6
RUN virtualenv --no-download /env -p python3.6

# Set virtualenv environment variables. This is equivalent to running
# source /env/bin/activate
ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH
ADD requirements.txt /app/
RUN apt-get update
RUN apt-get install -y software-properties-common
RUN apt-add-repository ppa:ricotz/testing
RUN apt-get update
RUN apt-get install -y libcairo2-dev
RUN apt-get install -y build-essential python3-dev python3-pip python3-setuptools python3-wheel python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info
RUN apt install -y pkg-config
RUN pip install -r requirements.txt
ADD . /app/

CMD gunicorn -b :$PORT pressureVessel.wsgi
