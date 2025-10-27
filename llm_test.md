curl -X POST "http://localhost:8000/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek-r1-0528-qwen3-8b",
    "messages": [
      {
        "role": "user",
        "content": "请写一首关于春天的诗"
      }
    ],
    "max_tokens": 500,
    "temperature": 0.9,
    "stream": false
  }'



curl -X POST "http://localhost:8000/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek-r1-0528-qwen3-8b",
    "messages": [
      {
        "role": "user",
        "content": "5*6=？"
      }
    ],
    "max_tokens": 500,
    "temperature": 0.9,
    "stream": false
  }'
