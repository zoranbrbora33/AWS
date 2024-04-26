from aws_cdk import Stack, aws_s3 as s3
from constructs import Construct


class ExampleS3StackStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        for num in range(1, 6):
            bucket = s3.Bucket(self, f"zbrbora-academy-cdk-{num}",
                               bucket_name=f"zbrbora-academy-cdk-{num}")
