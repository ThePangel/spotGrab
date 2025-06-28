FROM python:3.11-alpine

ARG TARGETPLATFORM
ARG BUILDPLATFORM
RUN echo "Building on $BUILDPLATFORM, targeting $TARGETPLATFORM"

WORKDIR /app

RUN apk add --no-cache ffmpeg

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir --upgrade spotdl


COPY src/ src/

EXPOSE 8000

VOLUME /music
VOLUME /public_downloads

CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]