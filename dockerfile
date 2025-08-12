FROM python:3.11-alpine

ARG TARGETPLATFORM
ARG BUILDPLATFORM
RUN echo "Building on $BUILDPLATFORM, targeting $TARGETPLATFORM"

WORKDIR /app

RUN apk add --no-cache ffmpeg \
    rust \
    cargo \
    build-base \
    openssl-dev \
    clang-dev \
    llvm-dev

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN cargo install rustifydl --force && \
    cp ~/.cargo/bin/rustifydl /usr/local/bin/ && \
    apk del build-base openssl-dev cargo rust clang-dev llvm-dev 


COPY src/ src/

EXPOSE 8000

VOLUME /music
VOLUME /public_downloads

CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]