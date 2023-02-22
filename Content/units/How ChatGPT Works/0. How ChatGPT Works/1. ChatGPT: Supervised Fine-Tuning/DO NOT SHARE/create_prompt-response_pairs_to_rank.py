# %%
import json
import pandas as pd

file = "raw_data.json"

input_data = pd.read_json(file, orient="records")
# print(input_data.columns)
# # print(input_data.head())
# print(input_data[0])

# create a dictionary mapping each prompt, which may be repeated, to a list of the given responses

data = {}

for idx, item in input_data.iterrows():
    pass
    # print(row)
    # print(row[0])
    prompt = item["prompt"]
    response = item["response"]
    if prompt not in data:
        data[prompt] = [response]
    else:
        data[prompt].append(response)

data = [
    {
        "text": prompt,
        "attachment_url": ""
        # **{f"response_{idx}": response for idx, response in enumerate(responses)}
    }
    for prompt, responses in data.items()
]

attachments = [
    [
        {
            "type": "text",
            "content": response
        }
        for response in responses
    ]
    for prompt, responses in data.items()
]

output_file = "prompt-response_pairs_to_rank.csv"

# save as csv
data = pd.DataFrame(data)
data.to_csv(output_file, index=False)


# %%
