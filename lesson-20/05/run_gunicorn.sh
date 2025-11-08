# Navigate to the script's directory
workdir=$(dirname "$0")
cd "$workdir" || exit 1

# Set up a virtual environment and install dependencies
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Run database migrations
python manage.py migrate

# Run the Django application using Gunicorn
gunicorn myproject.wsgi:application --bind 127.0.0.1:8000 --workers 4
