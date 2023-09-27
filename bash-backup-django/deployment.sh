#!/bin/bash

# Deployment script for a Django project

# Define your project variables
PROJECT_DIR="/Users/Macbook/desktop/work/PontosTuristicos"  # Replace with your project's directory
VENV_DIR="/Users/Macbook/desktop/work/PontosTuristicos/venv"         # Replace with your virtual environment directory
DJANGO_SETTINGS_MODULE="/Users/Macbook/desktop/work/PontosTuristicos/init/settings.py"  # Replace with your project's settings module

function error_exit {
  echo "Error: $1" >&2
  exit 1
}

function activate_venv {
  source "$VENV_DIR/bin/activate" || error_exit "Failed to activate virtual environment."
}

function update_code {
  cd "$PROJECT_DIR" || error_exit "Project directory not found."
  git pull origin master  # Replace 'master' with your branch name if needed
}

function install_dependencies {
  pip install -r requirements.txt
}

function apply_migrations {
  python manage.py migrate
}

function collect_static {
  python manage.py collectstatic --noinput
}

function restart_server {
  python manage.py runserver  # pode usar gunicorn
}

# Main deployment process
echo "Starting deployment..."

update_code

activate_venv

install_dependencies

apply_migrations

collect_static

restart_server

echo "Deployment completed successfully."

