import json
import os
import shutil

# 获取当前路径
BASE_DIR=os.getcwd()


# Read the uploaded file
loadJson = os.path.join(BASE_DIR,'CodeExercise-Python-27k.json')
print(loadJson)
with open(loadJson, "r") as metaFile:
    lines = metaFile.readlines()

# Extract the 'docstring' and 'code' fields from each line
extracted_data = []

# 这样写是读全部   for line in lines:
for line in lines:
    data = json.loads(line)
    # 初始化instruction和output字段
    instruction = None
    output = None

    # 遍历chat_rounds，根据role提取content
    for round in data['chat_rounds']:
        if round['role'] == 'human':
            instruction = round['content']
        elif round['role'] == 'bot':
            output = round['content']

    extracted_data.append({
        "instruction": instruction,#根据json文件调整
        "input":"",
        "output": output,#根据json文件调整
        "history": []
    })

# Save the extracted data to a new file
saveJson = os.path.join(BASE_DIR,'revise_CodeExercise-Python-27k.json')
with open(saveJson, "w") as metafile:
    for entry in extracted_data:
        metafile.write(json.dumps(entry) + "\n")
