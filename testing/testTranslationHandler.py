import argparse
import sys
sys.path.append("./library")

from TranslationHandler import TranslationHandler

# Add Command line arg for test audio file
parser = argparse.ArgumentParser(
    prog="TranslationHandler Unit Test",
    description="Tests the TranslationHandler class"
)
parser.add_argument("--text", "-t", required=True, type=str, help="Text to translate")
parser.add_argument("--language", "-l", required=True, type=str, help="ISO 639 code of language to translate to")
args = parser.parse_args()

text = args.text
output_language = args.language

print("Testing Translation Handling")

# Init Library
print("Initializing Class...", end="")
translator = TranslationHandler()
print("success!")

# Transcribe an audio file
translation = translator.translate(text)
print(f"Output Translation in {output_language}: {translation}")