import openai
import os

# プログラムは「```」で始まる

# path = "/Users/slabo_mac/Desktop/github/data/api.txt"
# path = "../../data/api.txt"

# with open(path) as f:
#     s = f.read()

openai.api_key = os.getenv("OPENAI_API_KEY")
print(openai.api_key)
# 個人のgoogleアカウントならいけた

res = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "あなたは賢いAIです。"},
        {"role": "user", "content": "こんにちは"},
    ],
    temperature=1,
)

print(res["choices"][0]["message"]["content"])