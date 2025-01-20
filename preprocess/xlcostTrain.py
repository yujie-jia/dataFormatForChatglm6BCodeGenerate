import json
import os
import shutil

# 获取当前路径
BASE_DIR=os.getcwd()

# 创建 myTrain 文件夹（如果尚未存在）
myTrain_folder=os.path.join(BASE_DIR,'xlcostTrain')
if not os.path.exists(myTrain_folder):
    os.makedirs(myTrain_folder)

# 获取文件夹中所有文件的列表
trainData_path=os.path.join(BASE_DIR,'program_level')
files = os.listdir(trainData_path)

for file in files:
    file_path = os.path.join(trainData_path, file)
    # sub_files = os.listdir(file_path)
    print(file_path)

    # 创建 myTrain_num 文件夹（如果尚未存在）
    myTrain_folder_num=os.path.join(myTrain_folder,file)
    if not os.path.exists(myTrain_folder_num):
        os.makedirs(myTrain_folder_num)

    loadJsonl = os.path.join(file_path, 'train.jsonl')
    print(loadJsonl)

    with open(loadJsonl, "r",encoding='utf-8') as metaFile:
        lines = metaFile.readlines()

    # Extract the 'docstring' and 'code' fields from each line
    extracted_data = []

    for line in lines:
        data = json.loads(line)
        extracted_data.append({
            "instruction": data.get("docstring_tokens", ""),
            "input":"",
            "output": data.get("code_tokens", ""),
            "history": []
        })

    # Save the extracted data to a new file
    saveJsonl = os.path.join(myTrain_folder_num,'xlcostTrain.jsonl')
    with open(saveJsonl, "w") as metafile:
        for entry in extracted_data:
            metafile.write(json.dumps(entry) + "\n")

    # Read the content of the uploaded jsonl file
    with open(saveJsonl, "r", encoding="utf-8") as metafile:
        lines = metafile.readlines()

    # Convert each line to a JSON object and store in a list
    data_list = [json.loads(line) for line in lines]

    # Convert the JSON object to a JSON string
    data_json_str = json.dumps(data_list, ensure_ascii=False, indent=4)

    # Save the converted JSON object to a file
    obtainJson = saveJsonl.replace('.jsonl', '.json')
    with open(obtainJson, "w", encoding="utf-8") as metafile:
        metafile.write(data_json_str)

    # 将文件移动到 myTrain_num 文件夹
    new_file_path = os.path.join(myTrain_folder_num, os.path.basename(obtainJson))
    shutil.move(obtainJson, new_file_path)







