from time import sleep

for index in range(100):
    sleep(1)
    with open(f'/my_directory/file_{index}', 'w') as f:
        f.write(str(index))
