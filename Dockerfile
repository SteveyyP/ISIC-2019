# Docker Image
FROM jjanzic/docker-python3-opencv

# Copy Data
COPY . /app

# Updates
RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

# Work Dir
WORKDIR /app

# ENV
ENV PATH=/root/.local/bin:${PATH}

# Requirements
RUN pip install --user -r requirements.txt

# SERVER
EXPOSE 5000
CMD ["python", "/app/app.py"]