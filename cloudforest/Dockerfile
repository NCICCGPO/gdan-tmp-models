# build stage
FROM golang:1.17.2-alpine AS build-env
RUN apk add git bash build-base
ENV GOPATH=/go
ENV PATH="/go/bin:${PATH}"
RUN cd /go/bin && go install github.com/ryanbressler/CloudForest/applyforest@latest

# final stage
FROM alpine
ENV PATH="/app:${PATH}"
COPY --from=build-env /go/bin/applyforest /app/
