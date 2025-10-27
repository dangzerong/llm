#!/usr/bin/env python3
"""
DeepSeek R1 客户端脚本
自动过滤 <think> 标签，只返回最终答案
"""

import requests
import json
import re
import sys

def remove_reasoning_tags(text):
    """
    移除 <think> 标签及其内容
    """
    # 移除 <think> 和 </think> 标签及其内容
    pattern = r'<think>.*?</think>'
    cleaned_text = re.sub(pattern, '', text, flags=re.DOTALL)
    
    # 清理多余的空白字符
    cleaned_text = re.sub(r'\n\s*\n', '\n', cleaned_text)
    cleaned_text = cleaned_text.strip()
    
    return cleaned_text

def call_deepseek_api(messages, api_url="http://localhost:8000/v1/chat/completions"):
    """
    调用 DeepSeek API 并自动过滤推理标签
    """
    payload = {
        "model": "deepseek-r1-0528-qwen3-8b",
        "messages": messages,
        "max_tokens": 1000,
        "temperature": 0.7,
        "stream": False
    }
    
    try:
        response = requests.post(api_url, json=payload, timeout=60)
        response.raise_for_status()
        
        result = response.json()
        
        if 'choices' in result and len(result['choices']) > 0:
            content = result['choices'][0]['message']['content']
            # 过滤推理标签
            cleaned_content = remove_reasoning_tags(content)
            result['choices'][0]['message']['content'] = cleaned_content
            
        return result
        
    except requests.exceptions.RequestException as e:
        print(f"API 调用失败: {e}")
        return None

def main():
    """
    主函数 - 交互式聊天
    """
    print("DeepSeek R1 客户端 (自动过滤推理标签)")
    print("输入 'quit' 或 'exit' 退出")
    print("-" * 50)
    
    while True:
        try:
            user_input = input("\n用户: ").strip()
            
            if user_input.lower() in ['quit', 'exit', '退出']:
                print("再见!")
                break
                
            if not user_input:
                continue
                
            messages = [
                {
                    "role": "user",
                    "content": user_input
                }
            ]
            
            print("正在思考...")
            result = call_deepseek_api(messages)
            
            if result and 'choices' in result:
                response = result['choices'][0]['message']['content']
                print(f"\n助手: {response}")
            else:
                print("抱歉，无法获取响应。")
                
        except KeyboardInterrupt:
            print("\n\n再见!")
            break
        except Exception as e:
            print(f"错误: {e}")

if __name__ == "__main__":
    main()
