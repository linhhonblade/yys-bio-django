#!/usr/bin/env sh
set -e

# wait for db? (optional) you can add wait-for-it logic if desired

# Apply migrations only if environment asks for it (so CI/CD can control)
if [ "${DJANGO_MIGRATE:-1}" = "1" ] ; then
  echo "Running migrations..."
  python manage.py migrate --noinput
fi

# Collect static files in production mode
# Use DJANGO_COLLECTSTATIC=1 to explicitly run collection
if [ "${DJANGO_COLLECTSTATIC:-1}" = "1" ] ; then
  echo "Collecting static files..."
  python manage.py collectstatic --noinput
fi

exec "$@"
