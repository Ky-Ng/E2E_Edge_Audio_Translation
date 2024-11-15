import sounddevice as sd
from transformers import pipeline
import whisper

# Constants
SAMPLE_RATE = 16000
duration = 5

# Record Audio
recording = sd.rec(frames=int(SAMPLE_RATE*duration), samplerate=SAMPLE_RATE, channels=1)
sd.wait(duration)

# Transcribe Audio
# transcriber = pipeline(model="openai/whisper-base")
# transcription = transcriber(recording)

# print(transcription)

# Load the Whisper model
model = whisper.load_model("base")

# Transcribe audio
result = model.transcribe(recording)
print(result["text"])
