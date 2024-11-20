from AudioHandler import AudioHandler


file_name = "test_audio_handler.wav"
audio_handler = AudioHandler()
audio_handler.record_audio(file_name)

audio_handler.playback_audio(file_name)