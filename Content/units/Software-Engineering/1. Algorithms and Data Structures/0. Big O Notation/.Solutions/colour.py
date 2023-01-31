from sys import getsizeof

with open("./colour.txt", 'r') as p:
    colour_dict = {}
    for line in p:
        line_list = line.split()
        if line_list[1] in colour_dict:
            colour_dict[line_list[1]] += 1
        else: 
            colour_dict[line_list[1]] = 1

print(colour_dict)
getsizeof(colour_dict)