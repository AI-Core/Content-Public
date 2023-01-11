aws sagemaker-runtime invoke-endpoint \
    --endpoint-name classifier-endpoint \
    --body fileb://img.jpg \
    --content-type image/jpeg \
    --accept application/json \
    --custom-attributes '{"feature": "flat"}' \
    feat.out