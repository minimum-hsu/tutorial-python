# Quart API with Uvicorn

In this lesson, we will create a simple RESTful API using the Quart web framework and deploy it using Uvicorn. The API will have a single endpoint that returns a greeting message.

## How to Run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn api:app --host 0.0.0.0 --port 8000
```

Or, you can use the provided `run.sh` script:

```bash
bash run.sh
```

## Accessing the API

The application will be accessible at `http://localhost:8000`.
You can test the endpoints using a web browser or tools like `curl` or Postman.
