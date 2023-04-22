import openai
import os
import sounddevice as sd
from scipy.io.wavfile import write

def record_mp3():
    fs = 48000
    duration = 10
    file = "input_data/user_input.wav"
    record = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    finish_token = input("Speak for the me(If you finish recording, press enter,) :")
    if finish_token == "":
        sd.stop
        #record = record / record.max() * np.iinfo(np.int16).max
        #record = np.dtype(np.int16)
        write(file, fs, record)
    elif finish_token == "exit":
        sd.stop
        exit()

def test():
    openai.api_key = os.getenv("OPENAI_API_KEY")
    sd.default.device = [0,1]
    #audio_file= open("gTTs_test.mp3", "rb")
    #transcript = openai.Audio.transcribe("whisper-1", audio_file)
    #print(transcript["text"])

test()
record_mp3()