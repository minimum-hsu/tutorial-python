# Flask API

In this lesson, we will create a simple RESTful API using the Flask web framework. The API will have a single endpoint that returns a greeting message.

## How to Run

To run the Flask application, follow these steps:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=api.py
flask run
```

Or, you can use the provided `run.sh` script:

```bash
bash run.sh
```

## Accessing the API

The application will be accessible at `http://localhost:5000`.
You can test the endpoints using a web browser or tools like `curl` or Postman.
