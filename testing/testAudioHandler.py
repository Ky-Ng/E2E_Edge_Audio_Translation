import sys
sys.path.append("./library")

from AudioHandler import AudioHandler
import os


print("Testing Audio Handling")
OUTPUT_DIR = "./testing/testing_outputs"
OUTPUT_FILE_NAME = "test_audio_handler.wav"

# Init Library
print("Initializing Class...", end="")
audio_handler = AudioHandler()
print("success!")

# Create output directory
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# Record for 2 seconds and playback audio
audio_handler.record_audio(
    output_wav_dir=os.path.join(
        OUTPUT_DIR, OUTPUT_FILE_NAME),
    record_time=2,
    freq=44100
)

# Playback the audio
audio_handler.playback_audio(os.path.join(
    OUTPUT_DIR, OUTPUT_FILE_NAME))
