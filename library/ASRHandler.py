from transformers import pipeline


class ASRHandler:
    def __init__(self) -> None:
        self.transcriber = pipeline(
            model="openai/whisper-base",
        )

    def transcribe(self, input_wav_file: str, output_english: bool = True) -> None:
        translation_args = {"task": "translate"} if output_english else None
        transcription = self.transcriber(
            input_wav_file, generate_kwargs=translation_args)
        return transcription["text"]
