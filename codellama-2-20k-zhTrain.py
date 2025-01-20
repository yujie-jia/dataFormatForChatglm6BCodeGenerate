import json
import os
import shutil

# 读取原始JSON文件
with open('codellama-2-20k-zh.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 修改数据中的格式
for item in data:
    item["history"] = []

# 将修改后的数据写回到新的JSON文件
with open('codellama-2-20k-zh.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("JSON格式已经成功修改并保存到新文件中。")










