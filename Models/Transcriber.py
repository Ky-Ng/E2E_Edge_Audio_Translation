from transformers import pipeline

transcriber = pipeline(model="openai/whisper-base")
# file = "https://huggingface.co/datasets/Narsil/asr_dummy/resolve/main/1.flac"
file = "./Data/wavs/recording0.wav"
x = transcriber(file)
print(x)