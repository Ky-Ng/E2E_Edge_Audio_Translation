import argparse
import os
import sys
sys.path.append("./library")

from TTSHandler import TTSHandler

# Add Command line arg for test audio file
parser = argparse.ArgumentParser(
    prog="TTSHandler Unit Test",
    description="Tests the TTSHandler class"
)
parser.add_argument("--text", "-t", required=True,
                    type=str, help="text to synthesize")
parser.add_argument("--playback", "-p", action="store_true",
                    help="text to synthesize")
args = parser.parse_args()

to_synthesize = args.text
play_audio = args.playback

OUTPUT_DIR = "./testing/testing_outputs"
OUTPUT_FILE_NAME = "test_tts.wav"

print("Testing TTS Handling")

# Init Library
print("Initializing Class...", end="")
tts = TTSHandler()
print("success!")

# Create output directory
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

for i in range(3):
    # Synthesize Audio
    wave_form = tts.save_waveform(fname=os.path.join(
        OUTPUT_DIR, OUTPUT_FILE_NAME),
        text=to_synthesize
    )

    # Play audio
    if play_audio:
        from AudioHandler import AudioHandler
        audio_handler = AudioHandler()
        audio_handler.playback_audio(os.path.join(
            OUTPUT_DIR, OUTPUT_FILE_NAME))
