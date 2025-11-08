from dataclasses import dataclass
import pytest
from main import lambda_handler


#############################
# Fixtures
#############################
@pytest.fixture(scope="function")
def lambda_context():
    """
    Dummy Lambda Context object.
    """

    @dataclass
    class LambdaContext:
        function_name: str = "test"
        memory_limit_in_mb: int = 128
        invoked_function_arn: str = "arn:aws:lambda:ap-northeast-1:000000000000:function:test"
        aws_request_id: str = "00000000-0000-0000-0000-000000000000"

    return LambdaContext()


#############################
# Testcases
#############################
def test_lambda_handler(lambda_context):
    lambda_handler({}, lambda_context)
