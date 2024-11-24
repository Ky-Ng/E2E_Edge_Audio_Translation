import argparse
import sys
sys.path.append("./library")

from ASRHandler import ASRHandler

# Add Command line arg for test audio file
parser = argparse.ArgumentParser(
    prog="ASRHandler Unit Test",
    description="Tests the ASRHandler class"
)
parser.add_argument("--audio", "-a", required=True, type=str, help="Audio file to transcribe")
args = parser.parse_args()

audio_path = args.audio

print("Testing ASR Handling")

# Init Library
print("Initializing Class...", end="")
asr = ASRHandler()
print("success!")

# Transcribe an audio file
transcription = asr.transcribe(audio_path, output_english=False)
print(f"Transcribing into original language: {transcription}")

transcription = asr.transcribe(audio_path)# Default to English
print(f"Transcribing into English: {transcription}")