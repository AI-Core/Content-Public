import json
import boto3
import base64

client = boto3.client("sagemaker-runtime", region_name="eu-west-1")


def lambda_handler(event, context):

    payload = event["payload"]

    payload = payload.encode("utf-8")
    payload = base64.b64decode(payload)

    response = client.invoke_endpoint(
        EndpointName="demo-classifier-endpoint",
        Body=payload,
        ContentType="image/jpeg",
    )

    print(response)
    response = response["Body"].read().decode("utf-8")
    response = json.loads(response)
    return {"statusCode": 200, "body": response}
