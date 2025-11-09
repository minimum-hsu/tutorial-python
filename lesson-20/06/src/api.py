"""
This module contains the API Gateway Lambda handler and the routes for the APIs.
"""


from functools import lru_cache
from http import HTTPStatus
from pydantic import ValidationError
from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from aws_lambda_powertools.event_handler import content_types
from aws_lambda_powertools.event_handler import Response
from aws_lambda_powertools.event_handler.openapi.exceptions import SchemaValidationError
from aws_lambda_powertools.event_handler.openapi.exceptions import SerializationError
from aws_lambda_powertools.event_handler.openapi.exceptions import RequestValidationError
from aws_lambda_powertools.event_handler.openapi.exceptions import ValidationException
from aws_lambda_powertools.event_handler.openapi.models import APIKey
from aws_lambda_powertools.event_handler.openapi.models import APIKeyIn
from aws_lambda_powertools.event_handler.openapi.params import Body
from aws_lambda_powertools.event_handler.openapi.params import Path
from aws_lambda_powertools.event_handler.openapi.params import Query
from aws_lambda_powertools.event_handler.openapi.types import OpenAPIResponse
from aws_lambda_powertools.event_handler.openapi.types import OpenAPIResponseContentModel
from model import User
from model import Users
from utils import is_feature_enabled


#############################
# Typing
#############################
from typing import Annotated
from aws_lambda_powertools.utilities.typing import LambdaContext


#############################
# Logging
#############################
from aws_lambda_powertools import Logger
from aws_lambda_powertools.logging import correlation_paths
logger = Logger()


#############################
# Tracer
#############################
from aws_lambda_powertools import Tracer
tracer = Tracer()


#############################
# Main
#############################
app = APIGatewayRestResolver(enable_validation=True, debug=is_feature_enabled("FEATURE_API_DEBUG"))
if is_feature_enabled("FEATURE_SWAGGER"):
    app.enable_swagger(
        path="/swagger",
        title="Tutorial Python",
        description="Introduce AWS API Gateway",
        security_schemes={
            "apikey": APIKey(
                name="X-API-KEY",
                description="AWS API Gateway API Key",
                in_=APIKeyIn.header, # type: ignore
            ),
        },
        security=[{"apikey": []}],
    )


@logger.inject_lambda_context(clear_state=True, correlation_id_path=correlation_paths.API_GATEWAY_REST)
@tracer.capture_lambda_handler
def lambda_handler(event: dict, context: LambdaContext) -> dict:
    """
    API Gateway Lambda handler.

    Args:
        event (dict): API Gateway Lambda Proxy Input Format.
        context (LambdaContext): Lambda Context runtime methods and attributes.
    """

    return app.resolve(event, context)


#############################
# Routes
#############################
@app.get("/api/users",
         summary="List all users",
         description="Get user IDs and names.",
         response_description="List of users",
         responses={
             HTTPStatus.OK: OpenAPIResponse(description="Accounts found"),
             HTTPStatus.BAD_REQUEST: OpenAPIResponse(description="Invalid request parameters", content={content_types.APPLICATION_JSON: OpenAPIResponseContentModel(model=Response)}),
             HTTPStatus.NOT_FOUND: OpenAPIResponse(description="Resource not found", content={content_types.APPLICATION_JSON: OpenAPIResponseContentModel(model=Response)}),
             HTTPStatus.INTERNAL_SERVER_ERROR: OpenAPIResponse(description="Unknown error", content={content_types.APPLICATION_JSON: OpenAPIResponseContentModel(model=Response)}),
         },
         security=[{"apikey": []}])
@tracer.capture_method
def list_users(
    offset: Annotated[int, Query(
        description="The offset parameter defines how many records to skip before starting to return results. It is typically used in conjunction with limit to paginate through a dataset.",
        ge=0,
    )] = 0,
    limit: Annotated[int, Query(
        description="The limit parameter defines the maximum number of records or results that the API should return in a single response. It is used to control the size of the dataset in the API response.",
        ge=1,
        le=1000,
    )] = 100,
) -> Response[Users]:
    # Simulate pagination
    users = _list_users()
    sub_users = Users(users[offset:offset + limit])
    return Response(
        status_code=HTTPStatus.OK,
        content_type=content_types.APPLICATION_JSON,
        body=sub_users,
    )

@app.get("/api/users/<user_id>",
         summary="Get user details",
         description="Get details of a specific user.",
         response_description="User details",
         responses={
             HTTPStatus.OK: OpenAPIResponse(description="User found"),
             HTTPStatus.BAD_REQUEST: OpenAPIResponse(description="Invalid request parameters", content={content_types.APPLICATION_JSON: OpenAPIResponseContentModel(model=Response)}),
             HTTPStatus.NOT_FOUND: OpenAPIResponse(description="Resource not found", content={content_types.APPLICATION_JSON: OpenAPIResponseContentModel(model=Response)}),
             HTTPStatus.INTERNAL_SERVER_ERROR: OpenAPIResponse(description="Unknown error", content={content_types.APPLICATION_JSON: OpenAPIResponseContentModel(model=Response)}),
         },
         security=[{"apikey": []}])
@tracer.capture_method
def get_user(
    user_id: Annotated[int, Path(
        description="User ID",
        strict=True,
    )],
) -> Response[User]:
    user = _get_user(user_id)
    return Response(
        status_code=HTTPStatus.OK,
        content_type=content_types.APPLICATION_JSON,
        body=user,
    )


@app.route("/api/users",
            method=["POST"],
            summary="Add a new user",
            description="Create a new user.",
            responses={
                HTTPStatus.OK: OpenAPIResponse(description="User created"),
                HTTPStatus.BAD_REQUEST: OpenAPIResponse(description="Invalid request parameters", content={content_types.APPLICATION_JSON: OpenAPIResponseContentModel(model=Response)}),
                HTTPStatus.NOT_FOUND: OpenAPIResponse(description="Resource not found", content={content_types.APPLICATION_JSON: OpenAPIResponseContentModel(model=Response)}),
                HTTPStatus.INTERNAL_SERVER_ERROR: OpenAPIResponse(description="Unknown error", content={content_types.APPLICATION_JSON: OpenAPIResponseContentModel(model=Response)}),
            },
            security=[{"apikey": []}])
@tracer.capture_method
def add_user(
    user_id: Annotated[int, Path(
        description="User ID",
        strict=True,
    )],
    name: Annotated[str, Body(
        description="User name",
        max_length=100,
        examples=["John Doe"],
    )],
    email: Annotated[str, Body(
        description="User email",
        max_length=320,
        examples=["alice@example.com"],
    )],
) -> Response[User]:
    # Simulate adding a new user
    user = User.model_validate({"id": user_id, "name": name, "email": email})

    return Response(
        status_code=HTTPStatus.OK,
        content_type=content_types.APPLICATION_JSON,
        body=user
    )


#############################
# Error Handling
#############################
@app.exception_handler([IndexError])
def handle_not_found_account(e) -> Response:
    """
    The data record or route/resource/page/endpoint was not found.
    Developer should check the log for more details.
    """

    metadata = {
        "path": app.current_event.path,
        "query_strings": app.current_event.query_string_parameters,
        "body": app.current_event.body,
    }
    logger.error(f"Malformed request: {e} ({type(e)})", extra=metadata)

    return Response(
        status_code=HTTPStatus.NOT_FOUND,
        content_type=content_types.APPLICATION_JSON,
        body={
            "status_code": HTTPStatus.NOT_FOUND,
            "message": "Account not found."
        }
    )

@app.exception_handler(ValidationError)
def handle_validation_error(e) -> Response:
    """
    Data model validation failed.
    Developer should check the log for more details.
    """

    metadata = {
        "path": app.current_event.path,
        "query_strings": app.current_event.query_string_parameters,
        "body": app.current_event.body,
    }
    logger.error(f"Validation error: {e} ({type(e)})", extra=metadata)

    return Response(
        status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
        content_type=content_types.APPLICATION_JSON,
        body={
            "status_code": HTTPStatus.INTERNAL_SERVER_ERROR,
            "message": "Validation error."
        }
    )


@app.exception_handler([RequestValidationError])
def handle_request_validation_error(e) -> Response:
    """
    Request validation failed.
    Client should check the request parameters.
    """

    metadata = {
        "path": app.current_event.path,
        "query_strings": app.current_event.query_string_parameters,
        "body": app.current_event.body,
    }
    logger.error(f"Validation error: {e} ({type(e)})", extra=metadata)

    return Response(
        status_code=HTTPStatus.BAD_REQUEST,
        content_type=content_types.APPLICATION_JSON,
        body={
            "status_code": HTTPStatus.BAD_REQUEST,
            "message": "Invalid request parameters.",
        }
    )


@app.exception_handler([SchemaValidationError,
                        SerializationError,
                        ValidationException])
def handle_openapi_error(e) -> Response:
    metadata = {
        "path": app.current_event.path,
        "query_strings": app.current_event.query_string_parameters,
        "body": app.current_event.body,
    }
    logger.error(f"OpenAPI error: {e} ({type(e)})", extra=metadata)

    return Response(
        status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
        content_type=content_types.APPLICATION_JSON,
        body={
            "status_code": HTTPStatus.INTERNAL_SERVER_ERROR,
            "message": "OpenAPI error.",
        },
    )


@app.exception_handler(Exception)
def handle_unexpected_error(e) -> Response:
    metadata = {
        "path": app.current_event.path,
        "query_strings": app.current_event.query_string_parameters,
        "body": app.current_event.body,
    }
    logger.error(f"Unexpected error: {e} ({type(e)})", extra=metadata)

    return Response(
        status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
        content_type=content_types.APPLICATION_JSON,
        body={
            "status_code": HTTPStatus.INTERNAL_SERVER_ERROR,
            "message": "Unknown error."
        }
    )


#############################
# Functions
#############################
@lru_cache
def _list_users() -> list[User]:
    """List all users."""
    # Simulate fetching users from a data source
    users = [
        User(id_=1, name="Alice", email="alice@example.com"),
        User(id_=2, name="Bob", email="bob@example.com"),
    ]
    return sorted(users, key=lambda u: u.name)

@lru_cache
def _get_user(user_id: int) -> User:
    """Get a user by ID."""
    # Simulate fetching a user from a data source
    users = _list_users()
    for user in users:
        if user.id_ == user_id:
            return user
    raise IndexError("User not found")
