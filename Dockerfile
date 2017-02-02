FROM python:3.4

# This Dockerfile manually installs cg-django-uaa from a built
# distribution and sets up the example app to run. It can be used
# to verify that everything about the packaging of cg-django-uaa is
# working properly (e.g., that important data files aren't being left
# out of the built distribution).

ARG version

ARG django_version

RUN pip install django==${django_version}

COPY dist/cg_django_uaa-${version}-py3-none-any.whl /

WORKDIR /

RUN pip install cg_django_uaa-${version}-py3-none-any.whl

COPY example /example

WORKDIR /example

RUN python manage.py migrate && \
  python manage.py createsuperuser --noinput \
    --username foo --email foo@example.org

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000