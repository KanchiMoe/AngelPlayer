FROM python:3
WORKDIR /script
COPY Requirements.txt *.py ./
RUN pip install --no-cache-dir -r Requirements.txt
