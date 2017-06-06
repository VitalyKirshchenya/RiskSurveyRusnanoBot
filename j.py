import json
from pprint import pprint

with open('survey/mandatory_questions_en_test.json') as data_file:
    data = json.load(data_file)

# for i in range(0, len(data)):
#     block = len(data[i]["blocks"])
#     pprint(block)
#     for j in range(0, len(data[i]["blocks"])):
#         question = len(data[i]["blocks"][j]["questions"])
#         pprint(question)
pprint(data[0]["blocks"][1]["block_name"])
