import requests
import json
from PIL import Image
import pickle

r = requests.get('http://127.0.0.1:5000') # make a get request to the local host (look in your hosts file)

print(r.__dir__()) # 
print(r.json()) # get the bytes back

r = requests.post('http://127.0.0.1:5000/predict', data=json.dumps({'input': 3}), headers={'content-type': 'application/json'})
print(r.content)


# import base64
# from io import BytesIO

# buffered = BytesIO()
# img = Image.open('../images/beijing.jpeg')
# img.save(buffered, format="JPEG")
# img_bytes = base64.b64encode(buffered.getvalue())
# img_str = img_bytes.decode('utf-8')
# r = requests.post('http://127.0.0.1:5000/detect', data=json.dumps({'input': img_str}), headers={'content-type': 'application/json'})
# print(r.content)