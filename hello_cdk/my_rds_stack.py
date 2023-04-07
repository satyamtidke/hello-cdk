import aws_cdk as cdk
from aws_cdk import  aws_rds as rds
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_secretsmanager as sm

class MyRdsStack(cdk.Stack):
    def __init__(self, scope: cdk.App, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        vpc = ec2.Vpc(self, "TheVPC",
            cidr="10.0.0.0/16"
        )
        # Create the RDS instance
        # my_secret = sm.Secret.
        # .from_secret_name(self, "DBSecret", "myDBLoginInfo")
        # my_secret = sm.Secret(self, "DBSecret")
        # Retrieve the secret value
        # my_secret_value = sm.SecretValue.from_secret_arn(self, "MySecretValue", my_secret.secret_arn)
        my_rds_instance = rds.DatabaseInstance(
            self, "MyRdsInstance",
            engine=rds.DatabaseInstanceEngine.mysql(version=rds.MysqlEngineVersion.VER_8_0_25),
            instance_type=ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE3, ec2.InstanceSize.SMALL),
            # credentials= rds.Credentials.from_secret(my_secret),
            credentials=rds.Credentials.from_generated_secret('SecretManger'),
            # credentials={
            #     "username": sm.secret_value_from_json("username").to_string(),
            #     "password": sm.secret_value_from_json("password")
            # },
            vpc=vpc,
            removal_policy=cdk.RemovalPolicy.DESTROY      
        )
        # Add tags to the RDS instance
        cdk.Tags.of(my_rds_instance).add("Name", "MyRdsInstance")
        #sm.

# # Create the RDS stack
# my_rds_stack = MyRdsStack(app, "MyRdsStack")

# # Synthesize the CloudFormation template
# app.synth()
