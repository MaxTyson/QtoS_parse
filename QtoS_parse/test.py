# import json

# # with open('parsed_data/data.json', 'r', encoding='utf-8') as json_file:
#     # data = json_file.open()
# # print(data)


# iii = open('parsed_data/data.json', 'r', encoding='utf-8')
# f = iii.read()
# data = json.loads(f)


# print(data)



import json

with open("parsed_data/data.json") as json_file:
     json_data = json.load(json_file)
     print(json_data)