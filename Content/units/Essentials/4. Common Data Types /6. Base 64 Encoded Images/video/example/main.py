import base64

with open("base64encoding.png", "rb") as f:
    data = f.read()

print(data)
print(type(data))

data = base64.b64encode(data).decode('utf-8')

print(data)
print(type(data))

data = base64.b64decode(data.encode('utf-8'))
print(data)
print(type(data))

with open("new_img.png", 'wb') as f:
    f.write(data)
