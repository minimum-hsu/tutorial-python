from http import HTTPStatus
import json
import jmespath
from api import lambda_handler
from api import _list_users
from model import User
from model import Users


#############################
# Testcases
#############################
def test_list_users(lambda_context):
    """
    The testcase is to test the API /api/users.
    """

    users = _list_users()
    assert jmespath.search(
        "users[].id | contains(@, '000000000000')",
        json.loads(Users(users).model_dump_json())
    )

    event = {
        "path": "/api/users",
        "httpMethod": "GET",
        "requestContext": {
            "requestId": "227b78aa-779d-47d4-a48e-ce62120393b8",
            "path": "/api/users",
        },  # correlation ID
        "queryStringParameters": {"limit": "100", "offset": "0"},
    }

    response = lambda_handler(event, lambda_context)
    assert response["statusCode"] == HTTPStatus.OK, response
    assert jmespath.search(
        "users[].id | contains(@, '000000000000')",
        json.loads(Users.model_validate_json(response["body"]).model_dump_json())
    )
