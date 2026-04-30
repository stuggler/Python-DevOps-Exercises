FROM python:3.14.4-trixie

WORKDIR /

COPY main.py /
COPY models.py /
COPY requirements.txt /
 
RUN pip3 install -r requirements.txt

CMD ["fastapi", "run", "main.py"]
