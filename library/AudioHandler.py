# Record imports
import sounddevice as sd
import wavio as wv

# Playback imports
from pydub import AudioSegment
from pydub.playback import play

class AudioHandler():
    def record_audio(self, output_wav_dir: str, record_time: int = 5, freq: int = 44100) -> None:
        recording = sd.rec(int(record_time * freq),
                           samplerate=freq, channels=1)
        sd.wait(record_time)
        wv.write(output_wav_dir, recording, freq, sampwidth=2)
    
    def playback_audio(self, wav_dir: str) -> None:
        sound = AudioSegment.from_file(wav_dir, format="wav")
        play(sound)
