FROM python:3.7-slim
RUN apt-get update && \
    apt-get install -y python3-pip && \
    pip3 install

# set directory
WORKDIR  /plotly_dash_visualisation/

# requirements
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# copy executive files
COPY ["data/", "pages/", "index.py", "wsgi.py",  "/src/"]

# run image
CMD python3 /src/index.py
