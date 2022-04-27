import json
import requests
import boto3
from datetime import datetime

s3_client = boto3.client("s3")


def lambda_handler(event, context):

    response = requests.get(
        "https://api.stackexchange.com/2.3/questions?pagesize=10&fromdate=1625961600&todate=1626048000&order=desc&sort=votes&site=stackoverflow"
    )
    response = response.json()
    print("response:", response)

    current_date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    s3_client.put_object(
        Body=json.dumps(response),
        Bucket="aicore-demo-bucket",
        Key=f"{current_date}.json",
    )

    return {"statusCode": 200, "body": json.dumps("Hello from Lambda!")}
