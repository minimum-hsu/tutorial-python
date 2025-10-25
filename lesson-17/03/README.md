# Get Startted for ORM and MySQL

This lesson will guide you through setting up an Object-Relational Mapping (ORM) tool to interact with a MySQL database in Python. We will use SQLAlchemy as our ORM of choice.

```bash
# Install dependencies
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Run MySQL server with Docker Compose
docker-compose up -d

# Run the application
python main.py
```