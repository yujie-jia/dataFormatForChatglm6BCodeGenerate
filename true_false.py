import json
import black

# 原始jsonl文件路径
input_file_path = 'samples.jsonl_results.jsonl'
# 新的python文件路径
output_file_path = 'formatted_chatgpt3.5_snippets.py'

# 打开原始文件进行读取
with open(input_file_path, 'r', encoding='utf-8') as input_file:
    # 读取所有行并将它们转换为包含task_id, completion, result, 和 passed的字典的列表
    task_data = [
        {
            'task_id': json.loads(line).get('task_id', ''),
            'completion': json.loads(line).get('completion', ''),
            'result': json.loads(line).get('result', ''),
            'passed': json.loads(line).get('passed', '')
        }
        for line in input_file
    ]

# 创建一个包含所有字段和值的字符串列表
formatted_data = [
    f"# Task ID: {data['task_id']}\n"
    f"# Completion:\n{data['completion']}\n"
    f"# Result: {data['result']}\n"
    f"# Passed: {data['passed']}\n\n"
    for data in task_data
]

# 将所有代码片段连接起来，以便进行格式化
combined_code = ''.join(formatted_data)

# 使用black格式化代码
try:
    formatted_code = black.format_str(combined_code, mode=black.Mode())
except Exception as e:
    # 如果格式化失败，原样输出或记录错误
    formatted_code = combined_code  # 或者可以记录错误信息到日志

# 将格式化后的代码写入新的python文件
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(formatted_code)

print('格式化完成，新的文件已保存为:', output_file_path)
