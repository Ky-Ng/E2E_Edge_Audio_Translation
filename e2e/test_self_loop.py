import argparse
import sys
sys.path.append("./library")

from AudioHandler import AudioHandler
from ASRHandler import ASRHandler
from TranslationHandler import TranslationHandler
from TTSHandler import TTSHandler

parser = argparse.ArgumentParser(prog="Test Self Loop End to End")
parser.add_argument("--language", "-l", type=str, required=True, help="ISO 639 code to output audio in")

args = parser.parse_args()

target_language = args.language
INSTRUCTIONS = "Self Loop Test Instructions: \n 1) Enter any key to record \n 2) [q] to quit \n"

print("Starting Self Loop Test")

# Initialize Pipelines
print("Initializing...", end="")
audio_handler = AudioHandler()
transcriber = ASRHandler()
translator = TranslationHandler(language_iso=target_language)
tts = TTSHandler()
print("done!")

fname_in_audio = "test_audio_handler.wav"
fname_out_audio = "playback.wav"

user_input = input(INSTRUCTIONS)
while (user_input != "q"):
    # Step 1) Record Audio
    audio_handler.record_audio(fname_in_audio)

    # Step 2) Transcribe Audio
    transcription = transcriber.transcribe(fname_in_audio)

    # Step 3) Translate Audio to target language if needed
    translated_transcription = translator.translate(transcription) if target_language != "en" else transcription

    # Step 4) Synthesize Speech
    tts.save_waveform(fname_out_audio, translated_transcription)

    # Display outputs
    print(f"Input Text: {transcription}")
    print(f"Output Text: {translated_transcription}")
    audio_handler.playback_audio(fname_out_audio)

    user_input = input(INSTRUCTIONS)
print("Pipeline closed")

