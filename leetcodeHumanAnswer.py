import os
import json
import re


# Define the directory containing the problems
problems_dir = "problems_原始数据"

# Define the pattern to match the content
description_pattern = r"## 题目描述(.+?)(?=\n##|$)"
code_to_complexity_pattern = r"## 代码(.+?)(?=\n##|\n\*\*)"

# Initialize a dictionary to hold the results
problems_json = {}

# Iterate over all .md files in the directory
for filename in os.listdir(problems_dir):
    if filename.endswith(".md") and not filename.endswith("en.md"):
        # Read the content of the file
        with open(os.path.join(problems_dir, filename), "r", encoding="utf-8") as file:
            content = file.read()

        # Extract the content under "## 题目描述" and from "## 代码" to "**复杂度分析**"
        description_match = re.search(description_pattern, content, re.DOTALL)
        description_content = description_match.group(1).strip() if description_match else ""

        code_to_complexity_match = re.search(code_to_complexity_pattern, content, re.DOTALL)
        code_to_complexity_content = code_to_complexity_match.group(1).strip() if code_to_complexity_match else ""

        # Add the content to the dictionary
        problems_json[filename] = {
            "instruction": description_content,
            "input":"",
            "output": code_to_complexity_content,
            "history": []
        }    

# Save the combined JSON content to a file
json_file_path = "leetcodeHumanAnswer.json"
with open(json_file_path, "w", encoding="utf-8") as json_file:
    json_file.write(json.dumps(list(problems_json.values()), ensure_ascii=False, indent=4))      

