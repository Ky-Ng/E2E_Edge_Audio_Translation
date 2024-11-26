import sys
sys.path.append("./library")

import os
from datetime import datetime
from AudioHandler import AudioHandler
from ASRHandler import ASRHandler
from TranslationHandler import TranslationHandler
from TTSHandler import TTSHandler
import json

log = []

# Initialize Models
audio_handler = AudioHandler()
transcriber = ASRHandler()

# TranslationHandler(language_iso="zh") # Initialize handlers only if needed
translator = None
tts = TTSHandler()

# Create Temporary Audio Buffers
OUTPUT_DIR = "conversation_buffer"  # Added to gitignore
AUDIO_IN_BUFFER_NAME = "{}audio_in_buffer.wav"
AUDIO_OUT_BUFFER_NAME = "{}audio_out_buffer.wav"

AUDIO_IN_PATH_TEMPLATE = os.path.join(OUTPUT_DIR, AUDIO_IN_BUFFER_NAME)
AUDIO_OUT_PATH_TEMPLATE = os.path.join(OUTPUT_DIR, AUDIO_OUT_BUFFER_NAME)

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def get_timestamp():
    formatted_datetime = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    return formatted_datetime

# Input callbacks


def get_input_to_english(str_in=None) -> str:
    """
    Record audio and output English

    Input: Any language supported by whisper
    Output: English
    """
    input("Type enter to begin 5 second recording: ")
    timestamp = get_timestamp()
    audio_handler.record_audio(AUDIO_IN_PATH_TEMPLATE.format(timestamp), record_time=5)
    transcription = transcriber.transcribe(
        input_wav_file=AUDIO_IN_PATH_TEMPLATE.format(timestamp), output_english=True)
    return transcription


def getInputFromChinese(str_in=None) -> str:
    """
    Record audio and output English

    Input: Any language supported by whisper
    Output: Mandarin Chinese
    """
    english_transcription = get_input_to_english()
    if not translator:
        translator = TranslationHandler(language_iso="zh")
    translated_transcription = translator.translate(english_transcription)
    return translated_transcription


def getInputFromTerminal(str_in=None) -> str:
    """
    Debug mode
    """
    text = input("Enter English Text:\n\t")
    return text

# Output callbacks
def log_to_transcript(str_in: str) -> None:
    global log
    log.append(str_in)
    with open("transcript.json", 'w') as ofile:
        json.dump(log, ofile)

def print_input(str_in: str) -> None:
    """
    Prints out transcription to terminal
    """
    print(str_in)


def synthesize_speech(str_in: str) -> None:
    """
    Synthesize speech using ChatTTS, generically support any languge ChatTTS supports
    """
    timestamp = get_timestamp()
    tts.save_waveform(fname=AUDIO_OUT_PATH_TEMPLATE.format(timestamp), text=str_in)
    audio_handler.playback_audio(AUDIO_OUT_PATH_TEMPLATE.format(timestamp))


def synthesize_speech_english(str_in: str) -> None:
    """
    Synthesizes English Speech
    """
    synthesize_speech(str_in=str_in)


def outputInputChinese(str_in: str) -> None:
    """
    Synthesizes Mandarin Chinese Speech
    """
    synthesize_speech(str_in=str_in)
