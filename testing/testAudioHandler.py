import argparse
import sys
sys.path.append("./library")

from AudioHandler import AudioHandler
import os

# Add Command line arg for test audio file
parser = argparse.ArgumentParser(
    prog="AudioHandler Unit Test",
    description="Tests the AudioHandler class"
)
parser.add_argument("--seconds", "-s", default=2, required=False, type=int, help="Record time in seconds")
args = parser.parse_args()

record_time = args.seconds


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
    record_time=record_time,
    freq=44100
)

# Playback the audio
audio_handler.playback_audio(os.path.join(
    OUTPUT_DIR, OUTPUT_FILE_NAME))
