# syntax=docker/dockerfile:1
# Official Docker container for onlineccompiler.com development & execution sandbox
FROM alpine:3.20

LABEL maintainer="Mahdi Hatefi <bro.meyti@gmail.com>"
LABEL org.opencontainers.image.title="online-c-compiler"
LABEL org.opencontainers.image.description="Cloud GCC 13/14 C Compiler Sandbox & CLI for onlineccompiler.com"
LABEL org.opencontainers.image.url="https://onlineccompiler.com/"
LABEL org.opencontainers.image.source="https://github.com/MoMahdideveloper/online-c-compiler-suite"
LABEL org.opencontainers.image.licenses="MIT"

# Install GCC, Clang, build-base, and curl
RUN apk add --no-cache \
    gcc \
    clang \
    musl-dev \
    build-base \
    gdb \
    valgrind \
    curl \
    bash

WORKDIR /workspace

# Copy welcome banner and compiler helper
COPY entrypoint.sh /usr/local/bin/occ-entrypoint
RUN chmod +x /usr/local/bin/occ-entrypoint

ENV COMPILER_HOMEPAGE="https://onlineccompiler.com/"
ENV COMPILER_PORTAL_ES="https://onlineccompiler.com/es/"
ENV COMPILER_PORTAL_PT="https://onlineccompiler.com/pt/"
ENV COMPILER_PORTAL_DE="https://onlineccompiler.com/de/"
ENV COMPILER_PORTAL_FR="https://onlineccompiler.com/fr/"

ENTRYPOINT ["/usr/local/bin/occ-entrypoint"]
CMD ["/bin/bash"]
