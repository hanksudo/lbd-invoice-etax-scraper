FROM alpine

RUN apk add --update py2-pip

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

COPY app.py /usr/src/app/

CMD ["python", "/usr/src/app/app.py"]