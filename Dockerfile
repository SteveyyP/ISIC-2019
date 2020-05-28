FROM jjanzic/docker-python3-opencv
COPY . /app
RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean
WORKDIR /app
ENV PATH=/root/.local/bin:${PATH}
RUN pip install --user -r requirements.txt
CMD ["python", "/app/app.py"]