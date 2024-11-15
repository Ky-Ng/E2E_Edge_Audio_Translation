from transformers import pipeline

transcriber = pipeline(model="openai/whisper-base")
# file = "https://huggingface.co/datasets/Narsil/asr_dummy/resolve/main/1.flac"
file = "./Data/wavs/recording1.wav"
transcription = transcriber(file)
print(transcription)

# Use a pipeline as a high-level helper
# from transformers import pipeline

pipe = pipeline("translation", model="alirezamsh/small100")
translation = pipe(transcription)
print(translation)