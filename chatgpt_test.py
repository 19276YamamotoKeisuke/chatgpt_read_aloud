import openai
import os
from gtts import gTTS
import sounddevice as sd
import soundfile as sf
from scipy.io.wavfile import write
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
    #if len(transcript) <= 2:
    #    return ""
    return transcript["text"]

# ユーザからの入力を録音
def record_mp3():
    fs = 48000
    duration = 30
    file = "input_data/user_input.wav"
    record = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    finish_token = input("You have 30s to speak(press enter to finish recording) :")
    if finish_token == "":
        sd.stop
        #record = record / record.max() * np.iinfo(np.int16).max
        #record = np.dtype(np.int16)
        write(file, fs, record)
        s_to_text = sound_to_text(file)
        return s_to_text
    elif finish_token == "exit":
        pygame.mixer.music.stop()
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
        inputText = record_mp3()
        # 音声がうまく取得できなかった時にトークンを節約する(うまく動作していないので現時点で意味なし？)
        if len(inputText) < 4:
            print("I can't hear your voice, run this program again.")
        res_file = chatgpt_com(inputText)
        play_mp3(res_file)
        #dummy()
    
def setup():
    openai.api_key = os.getenv("OPENAI_API_KEY")
    sd.default.device = [0,1]


if __name__ == "__main__":
    # apikeyを設定
    # translator設定 一時凍結
    #en_to_ja_translator = pipeline("translation", model="staka/fugumt-en-ja")
    #ja_to_en_translator = pipeline("translation", model="staka/fugumt-ja-en")
    setup()
    print("If you want to finish this program, entering exit")
    main()
    # 個人のgoogleアカウントならいけた