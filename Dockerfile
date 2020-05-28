FROM python:3.7-slim
COPY static/ /app
COPY templates/ /app
COPY ISIC_preprocessing.py /app
COPY app.py /app
COPY predict_api.py /app
COPY lesion_dict.py /app
COPY requirements.txt /app
RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean
WORKDIR /app
ENV PATH=/root/.local/bin:$PATH
RUN pip install --user -r requirements.txt
CMD ["python", "/app/app.py"]