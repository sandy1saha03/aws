import boto3
import json

# Define common Variables

lambda_arn='arn:aws:lambda:us-west-2:699325298196:function:LogEC2InstanceStateChange'
role_arn='arn:aws:iam::699325298196:role/mycloudwatch'
rule_name='AwsConsoleSignIn'

# Create  Cloudwatch client
event = boto3.client('events')

# Create Cloudwatch Rule
event_rule = event.put_rule(
    Name=rule_name,
    EventPattern=json.dumps(
        {
            "detail-type": [
                "AWS Console Sign In via CloudTrail"
            ]
        }
    ),
    State='ENABLED',
    Description='This Rule will send information for every AWS console sign in ',
    RoleArn=role_arn
)

## Create event Target for the above rule

event_target = event.put_targets(
    Rule = rule_name,
    Targets=[
        {
            'Id': rule_name + 'sign-in',
            'Arn': lambda_arn,

       }
    ]
)