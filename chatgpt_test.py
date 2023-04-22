import openai
import os
import time
from datetime import datetime as dt
from gtts import gTTS
import pygame


def play_mp3(mpfile):
    pygame.mixer.init(frequency = 44100)
    pygame.mixer.music.set_volume(1.0)
    print("data/" + mpfile)
    # pygame.mixer.music.load("data/" + mpfile)
    pygame.mixer.music.load("test.mp3")
    pygame.mixer.music.play(1)
    time.sleep(20)

def chatgpt_com(input_t):
    # chatgptと通信して返答を取得&mp3に加工
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "あなたは賢いAIです。"},
            {"role": "user", "content": input_t},
        ],
        temperature=1,
    )
    text = res["choices"][0]["message"]["content"]
    tts = gTTS(text, lang='ja')
    # ファイルネームが重複しないように時間.mp3で保存
    tdatetime = dt.now()
    filename = tdatetime.strftime('%d%h%m%s')
    # filename += ".mp3"
    filename = filename + ".mp3"
    filearray.append(filename)
    tts.save("data/" + filename)
    #配列に追加(変数でも可？)　再生する時に参照
    print(filearray)

def dummy():
    text = "これはpygame音声再生のテストです。"
    tts = gTTS(text, lang='ja')
    tts.save("for_test_pygame.mp3")
    pygame.mixer.init(frequency = 44100)
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.load("for_test_pygame.mp3")
    pygame.mixer.music.play(1)
    time.sleep(20)
    # pygame.mixer.music.stop()

def main():
    global filearray
    filearray = []
    while(True):
        # inputText = input("Enter your text:")
        #chatgpt_com(inputText)
        dummy()
        break
        # filearray.append(inputText)
        # play_mp3(filearray[0])

if __name__ == "__main__":
    openai.api_key = os.getenv("OPENAI_API_KEY")
    main()
    # 個人のgoogleアカウントならいけた