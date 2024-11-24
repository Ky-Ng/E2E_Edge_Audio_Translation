# Based off of documentation: https://github.com/2noise/ChatTTS/tree/main?tab=readme-ov-file#basic-usage
import ChatTTS
import wavio as wv

chat = ChatTTS.Chat()

chat.load(compile=True) # Set to True for better performance

texts = ["我和jonathan终于成功，最佳拍档[laugh][lbreak]"]

wavs = chat.infer(texts)

wavs = wavs.reshape(-1, 1)

freq = 24000
wv.write("recording1.wav", wavs, freq, sampwidth=2)