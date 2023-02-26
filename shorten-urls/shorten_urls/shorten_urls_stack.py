import typing
from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda as _lambda
    # aws_sqs as sqs,
)
from constructs import Construct


class ShortenUrlsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        my_lambda = _lambda.Function(
            self, 'ShortenURLHandler',
            runtime=typing.cast(_lambda.Runtime, _lambda.Runtime.PYTHON_3_7),
            code=_lambda.Code.from_asset('lambda'),
            handler='shorten_url.handler',
        )
