import pandas as pd

def get_auto_mpg_data():
    feature_names = [
        'mpg',
        'cylinders',
        'displacement',
        'horsepower',
        'weight',
        'acceleration',
        'model year',
        'origin',
        # 'car name'
    ]

    with open('auto-mpg.data') as f:
        lines = f.readlines()

    datapoints = []
    for line in lines:
        numerical_features, model = line.split('\t')
        features = [f for f in numerical_features.split(' ')]
        features = [f for f in features if f != '']
        features = [f for f in features if f != '?']
        features = [float(f) for f in features]
        if len(features) != len(feature_names):
            # print('missing features!')
            continue
        example = {}
        for feature_idx in range(len(feature_names)):
            example[feature_names[feature_idx]] = features[feature_idx]

        datapoints.append(example)
    df = pd.DataFrame(datapoints)
    return df