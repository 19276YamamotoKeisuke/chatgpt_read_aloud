import openai
import os
import time
from datetime import datetime as dt
from gtts import gTTS
#from transformers import pipeline
import pygame

# mp3を再生
def play_mp3(mpfile):
    pygame.mixer.init(frequency = 44100)
    pygame.mixer.music.set_volume(1.0)
    print(mpfile)
    # pygame.mixer.music.load("data/" + mpfile)
    pygame.mixer.music.load(mpfile)
    pygame.mixer.music.play(1)
    # time.sleep(15)

# token数を減らすためにユーザ入力を英語に、gpt出力を日本語に
# def translate(text, lang):
#     if lang == "ja":
#         translated = ja_to_en_translator(text)
#     elif lang == "en":
#         translated = en_to_ja_translator(text)
#     return translated

# chatgptと通信して返答を取得&mp3に加工
def chatgpt_com(input_t):
    #input_t = translate(input_t, "ja")
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "あなたは賢いAIです。"},
            {"role": "user", "content": input_t},
        ],
        temperature=1,
    )
    text = res["choices"][0]["message"]["content"]
    #text = translate(text, "en")
    tts = gTTS(text, lang='ja')
    # ファイルネームが重複しないように時間.mp3で保存
    #tdatetime = dt.now()
    #filename = tdatetime.strftime('%d%h%m%s')
    # filename += ".mp3"
    filename = "data/" + "chatgpt_res.mp3"
    #filearray.append(filename)
    tts.save(filename)
    return filename

def dummy():
    text = "これはpygame音声再生のテストです。"
    tts = gTTS(text, lang='ja')
    tts.save("for_test_pygame.mp3")
    pygame.mixer.init(frequency = 44100)
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.load("for_test_pygame.mp3")
    pygame.mixer.music.play(1)
    # pygame.mixer.music.stop()

def main():
    #global filearray
    # 会話内容を記憶するための配列　未実装
    history = []
    #filearray = []
    while True:
        inputText = input("Enter your text(If you exit this program, please write exit.):")
        if inputText == "exit":
            pygame.mixer.music.stop()
            break
        # pygame.mixer.music.stop()
        res_file = chatgpt_com(inputText)
        play_mp3(res_file)
        #dummy()
        # filearray.append(inputText)

if __name__ == "__main__":
    # apikeyを設定
    openai.api_key = os.getenv("OPENAI_API_KEY")
    # translator設定 一時凍結
    #en_to_ja_translator = pipeline("translation", model="staka/fugumt-en-ja")
    #ja_to_en_translator = pipeline("translation", model="staka/fugumt-ja-en")
    main()
    # 個人のgoogleアカウントならいけた