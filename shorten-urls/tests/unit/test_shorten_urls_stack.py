import aws_cdk as core
import aws_cdk.assertions as assertions

from shorten_urls.shorten_urls_stack import ShortenUrlsStack

# example tests. To run these tests, uncomment this file along with the example
# resource in shorten_urls/shorten_urls_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ShortenUrlsStack(app, "shorten-urls")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
