#!/usr/bin/env bash
docker build -t qups-store .
#source .flaskenv
#docker run -p 80:5000 -d --rm -e SECRET_KEY="$(pwgen 32 1)" -e ADMIN_PASSWORD="${ADMIN_PASSWORD}" -e MAIL_USERNAME="${MAIL_USERNAME}" -e MAIL_PASSWORD="${MAIL_PASSWORD}" -e MAIL_ADDRESS="${MAIL_ADDRESS}" -e MAIL_SERVER="${MAIL_SERVER}" -e MAIL_PORT="${MAIL_PORT}" -e MAIL_USE_TLS="${MAIL_USE_TLS}" qups-store
docker run -p 80:5000 -d --restart=always  qups-store
