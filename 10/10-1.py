filename = "learning_python.txt"

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

list = []
with open(filename) as file_object:
    for line in file_object:
        list.append(line.rstrip())

for line in list:
    print(line)

with open(filename) as file_object:
    contents = file_object.read()
    print(contents)

