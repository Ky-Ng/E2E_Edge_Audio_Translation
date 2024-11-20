from transformers import pipeline

class Transcriber:
    def __init__(self) -> None:
        self.transcriber = pipeline(model="openai/whisper-base")
    
    def transcribe(self, input_wav_file:str) -> None:
        transcription = self.transcriber(input_wav_file)
        return transcription["text"]

# file = "https://huggingface.co/datasets/Narsil/asr_dummy/resolve/main/1.flac"
# file = "./Data/wavs/recording1.wav"
# transcription = transcriber(file)
# print(transcription)

# Use a pipeline as a high-level helper
# from transformers import pipeline

# pipe = pipeline("translation", model="alirezamsh/small100")
# translation = pipe(transcription)
# print(translation)