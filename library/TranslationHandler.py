from transformers import pipeline


class TranslationHandler():
    """
    This class takes in English Text and returns the translation in the target language
    - Whisper handles the non-English to English translation in the ASR step

    Note: only Mandarin Chinese is supported at the current time
    """

    SUPPORTED_LANGUAGES = ["zh"]

    def __init__(self, language_iso: str = "zh") -> None:
        if language_iso not in TranslationHandler.SUPPORTED_LANGUAGES:
            print("language_iso should be the ISO 639 language code\nNote: Only Mandarin Chinese is supported at the current time")

        self.translator = pipeline(
            "translation", model="Helsinki-NLP/opus-mt-en-zh")

    def translate(self, text: str) -> str:
        output = self.translator(text)
        translation = output[0]["translation_text"] # We use 0 since we do not allow batched translation
        return translation
