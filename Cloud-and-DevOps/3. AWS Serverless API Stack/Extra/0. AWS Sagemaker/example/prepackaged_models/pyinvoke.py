import boto3

client = boto3.client("sagemaker-runtime")

with open("angry-dog.jpg", "rb") as f:
    payload = f.read()
    payload = bytearray(payload)

response = client.invoke_endpoint(
    EndpointName="demo-classifier-endpoint",
    Body=payload,
    ContentType="image/jpeg",
    # Accept="image/jpeg",
    # CustomAttributes='string',
    # TargetModel='string',
    # TargetVariant='string',
    # TargetContainerHostname='string',
    # InferenceId='string'
)
print(response)

print(response["Body"].read())
