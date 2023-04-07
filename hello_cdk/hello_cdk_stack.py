import this
import aws_cdk as cdk
import aws_cdk.aws_s3 as s3
            
class HelloCdkStack(cdk.Stack):

    def __init__(self, scope: cdk.App, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # bucket = s3.Bucket(self, "AWSSDKBUCKET_2023-04-03-6", versioned=True)
        bucket = s3.Bucket(
            self,
            "AWSSDKBUCKET_2023-04-03-6",
            versioned=True,
            removal_policy=cdk.RemovalPolicy.DESTROY,
            auto_delete_objects=True
        )
        #self.add_cdk_destroy_command(resources=["AWSSDKBUCKET_2023-04-03-6"])

        # bucket = s3.Bucket(this, 'MyTempFileBucket', {
        #                 removalPolicy: cdk.RemovalPolicy.DESTROY,
        #                 autoDeleteObjects: true,
        #                 });
        