#! /usr/bin/env bash

while ! nc -z postgres 5432; do
  sleep 0.1
done

aerich upgrade

exec "$@"