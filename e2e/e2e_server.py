from utils.TtsHandler import TtsHanlder
from utils.BluetoothHandler import BluetoothHandler
from utils.AudioHandler import AudioHandler
from utils.Transcriber import Transcriber

SELF_LOOP_MODE = True

def main():
    print("Starting E2E Audio Pass Through")
    fname_in_audio = "test_audio_handler.wav"
    fname_out_audio = "playback.wav"

    # Record Audio
    audio_handler = AudioHandler()
    audio_handler.record_audio(fname_in_audio)

    # Transcribe Audio
    transcriber = Transcriber()
    transcription = transcriber.transcribe(fname_in_audio)
    print(transcription)

    # Echo back audio
    if SELF_LOOP_MODE:
        # Syntehsize Speech
        tts = TtsHanlder()
        tts.save_waveform(fname_out_audio, transcription)

        # Playback to audio
        audio_handler.playback_audio(fname_out_audio)

    # Bluetooth send
    bluetooth_handler = BluetoothHandler()
    bluetooth_handler.send(transcription)
    print("Sent transcription", transcription)
    

if __name__ == "__main__":
    main()