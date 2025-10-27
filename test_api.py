#!/usr/bin/env python3
"""
测试 DeepSeek R1 API 调用
包含系统消息来抑制推理输出
"""

import requests
import json
import re

def test_deepseek_api():
    """
    测试 DeepSeek API 调用
    """
    url = "http://localhost:8000/v1/chat/completions"
    
    # 方法1: 使用系统消息
    payload_with_system = {
        "model": "deepseek-r1-0528-qwen3-8b",
        "messages": [
            {
                "role": "system",
                "content": "你是一个有用的助手。请直接给出答案，不要显示思考过程。不要使用 <think> 标签或显示内部推理。"
            },
            {
                "role": "user",
                "content": "1+1=?"
            }
        ],
        "max_tokens": 100,
        "temperature": 0.1,
        "stream": False
    }
    
    # 方法2: 在用户消息中添加指令
    payload_with_instruction = {
        "model": "deepseek-r1-0528-qwen3-8b",
        "messages": [
            {
                "role": "user",
                "content": "1+1=? 请直接给出答案，不要显示思考过程。"
            }
        ],
        "max_tokens": 100,
        "temperature": 0.1,
        "stream": False
    }
    
    print("测试方法1: 使用系统消息")
    try:
        response = requests.post(url, json=payload_with_system, timeout=30)
        result = response.json()
        print("响应:", result['choices'][0]['message']['content'])
    except Exception as e:
        print(f"方法1失败: {e}")
    
    print("\n测试方法2: 在用户消息中添加指令")
    try:
        response = requests.post(url, json=payload_with_instruction, timeout=30)
        result = response.json()
        print("响应:", result['choices'][0]['message']['content'])
    except Exception as e:
        print(f"方法2失败: {e}")

if __name__ == "__main__":
    test_deepseek_api()
