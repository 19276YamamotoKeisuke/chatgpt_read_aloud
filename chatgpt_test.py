import openai
import os
from datetime import datetime as dt
from gtts import gTTS
import sounddevice as sd
import soundfile as sf
import numpy as np
import pygame
#from transformers import pipeline

# mp3を再生
def play_mp3(output_mpfile):
    pygame.mixer.init(frequency = 44100)
    pygame.mixer.music.set_volume(1.0)
    print(output_mpfile)
    pygame.mixer.music.load(output_mpfile)
    pygame.mixer.music.play(1)
    # time.sleep(15)

# 入力した音源を文字起こし　whisperAPI
def sound_to_text(input_mpfile):
    audio_file= open(input_mpfile, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    # print(transcript["text"])
    return transcript["text"]

def record_mp3():
    fs = 48000
    duration = 30
    file = "input_data/user_input.wav"
    record = sd.rec(duration * fs, samplerate=fs, channels=1)
    finish_token = input("Speak for the me(If you finish recording, press enter,) :")
    if finish_token == "":
        sd.stop
        sf.write(file, fs, record)
    elif finish_token == "exit":
        sd.stop
        exit()
    

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
    filename = "data/" + "chatgpt_res.mp3"
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
    # 会話内容を記憶するための配列　未実装
    history = []
    while True:
        inputText = input("Enter your text(If you exit this program, please write exit.):")
        if inputText == "exit":
            pygame.mixer.music.stop()
            break
        res_file = chatgpt_com(inputText)
        play_mp3(res_file)
        #dummy()
    
def setup():
    openai.api_key = os.getenv("OPENAI_API_KEY")
    sd.default.device = 2


if __name__ == "__main__":
    # apikeyを設定
    # translator設定 一時凍結
    #en_to_ja_translator = pipeline("translation", model="staka/fugumt-en-ja")
    #ja_to_en_translator = pipeline("translation", model="staka/fugumt-ja-en")
    setup()
    main()
    # 個人のgoogleアカウントならいけた