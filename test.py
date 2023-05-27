import json

def read_file(filename: str):
    with open(filename, mode='r', encoding='UTF-8') as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n','')
    return lines

def write_file(filename: str, data):
    with open(filename, mode='a', encoding='UTF-8') as file:
        file.write(data + "\n")

string = '{"message_id": 768, "user_id": 948908952}'
json_obj = json.loads(string)


