FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /anaconda_django
WORKDIR /anaconda_django
ADD requirements.txt /anaconda_django/
RUN cat requirements.txt
RUN pip install  certifi
RUN pip install  cycler
RUN pip install  asgiref
RUN pip install  Django
RUN pip install  kiwisolver
RUN pip install  matplotlib
RUN pip install  numpy
RUN pip install  pandas
RUN pip install  Pillow
RUN pip install  pyparsing
RUN pip install  python-dateutil
RUN pip install  pytz
RUN pip install  scipy
RUN pip install  seaborn
RUN pip install  six
RUN pip install  sqlparse
ADD . /anaconda_django/