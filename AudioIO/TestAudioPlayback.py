from pydub import AudioSegment
from pydub.playback import play

sound = AudioSegment.from_file("recording0.wav", format="wav")
play(sound)