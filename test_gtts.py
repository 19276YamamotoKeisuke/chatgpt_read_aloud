from gtts import gTTS

text = "こんにちは、何かお困りのことはありますか"
tts = gTTS(text, lang='ja')
tts.save("data/start.mp3")
