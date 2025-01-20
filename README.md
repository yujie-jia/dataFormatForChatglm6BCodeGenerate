# ChatGLM代码生成数据格式化工具

这是一个用于处理和格式化代码生成任务数据的工具集，主要用于ChatGLM代码生成任务的数据预处理和后处理。

## 项目结构

```
dataFormatForChatglm6BCodeGenerate/
├── preprocess/                   # 预处理脚本
│   ├── CodeExercise-Python-27k.py    # 处理Python练习数据集
│   ├── codellama-2-20k-zhTrain.py    # 处理CodeLlama中文数据集
│   ├── leet10k.py                    # 处理LeetCode 10k数据集
│   ├── leetcodeHumanAnswer.py        # 处理LeetCode人工答案
│   └── xlcostTrain.py                # 处理XLCOST训练数据
└── postprocess/                  # 后处理脚本
    ├── format.py                     # ChatGLM测试结果格式化
    ├── true_false.py                 # 结果验证格式化
    └── json显示转化为易于人类阅读的python显示.py  # JSON转Python格式显示
```

## 功能特点

### 预处理功能
1. **数据格式统一化**
   - 将不同来源的数据统一转换为标准格式：
   ```json
   {
     "instruction": "问题描述",
     "input": "",
     "output": "代码答案",
     "history": []
   }
   ```

2. **支持多种数据源**
   - Python练习题(27k)数据集处理
   - CodeLlama中文数据集处理
   - LeetCode相关数据集处理
   - XLCOST训练数据处理

### 后处理功能
1. **代码格式化**
   - 使用black进行Python代码格式化
   - 保持代码风格一致性

2. **结果展示优化**
   - 将JSONL格式转换为易读的Python文件格式
   - 保留任务ID、完成情况、结果等元数据
   - 支持结果验证和展示

