import json
import boto3
import base64

client = boto3.client("sagemaker-runtime", region_name="eu-west-1")


def lambda_handler(event, context):

    payload = event["payload"]

    print(response)
    response = response["Body"].read().decode("utf-8")
    response = json.loads(response)
    return {"statusCode": 200, "body": response}
