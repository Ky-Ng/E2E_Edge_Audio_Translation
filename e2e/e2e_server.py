from utils.BluetoothHandler import BluetoothHandler
from utils.AudioHandler import AudioHandler
from utils.Transcriber import Transcriber

def main():
    print("Starting E2E Audio Pass Through")
    file_name = "test_audio_handler.wav"
    # Record Audio
    audio_handler = AudioHandler()
    audio_handler.record_audio(file_name)

    # Transcribe Audio
    transcriber = Transcriber()
    transcription = transcriber.transcribe(file_name)
    print(transcription)

    bluetooth_handler = BluetoothHandler()
    bluetooth_handler.send(transcription)
    print("Sent transcription", transcription)
    

if __name__ == "__main__":
    main()