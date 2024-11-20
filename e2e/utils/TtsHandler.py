import ChatTTS
import numpy as np
import wavio as wv


class TtsHanlder:
    # Default for ChatTTS Library
    FREQ = 24000

    def __init__(self) -> None:
        self.chat = ChatTTS.Chat()
        self.chat.load(compile=True)  # Set to True for better performance

    def get_waveform(self, text: str) -> np.ndarray:
        # Apply TTS and get the waveform
        wav = self.chat.infer(text)

        # Reshape into the format needed for wavio
        wav = wav.reshape(-1, 1)
        return wav

    def save_waveform(self, fname: str, text: str) -> np.ndarray:
        wav = self.get_waveform(text)
        wv.write("recording1.wav", wav, TtsHanlder.FREQ, sampwidth=2)
        return wav
        
