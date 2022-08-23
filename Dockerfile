FROM python:3.10
COPY requirements.txt /requirements.txt
COPY endpoint.py /app.py
COPY scripts /scripts
COPY models /models 
RUN pip install -r requirements.txt
EXPOSE 5001
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5001"]
