import json
import sys

# 从用户输入获取文件名
file_name = "leet10k.json"

# 尝试读取文件内容
try:
    with open(file_name, 'r', encoding='utf-8') as file:
        data = json.load(file)
except FileNotFoundError:
    print("文件未找到，请检查文件名是否正确。")
    sys.exit(1)
except json.JSONDecodeError:
    print("文件内容不是有效的JSON格式。")
    sys.exit(1)
except Exception as e:
    print(f"读取文件时发生错误：{e}")
    sys.exit(1)

for item in data:
    if "Instruction" in item:
        item["instruction"] = item.pop("Instruction")
    if "Input" in item:
        item["input"] = item.pop("Input")
    if "Output" in item:
        item["output"] = item.pop("Output")
    item["history"] = []

# 将修改后的内容写回文件
try:
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"文件 {file_name} 已成功更新。")
except Exception as e:
    print(f"写入文件时发生错误：{e}")











