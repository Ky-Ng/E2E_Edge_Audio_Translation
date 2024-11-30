# E2E_Edge_Audio_Translation
# Jonathan and I passion project ...  :)

Names:
    - Jonathan Ong
    - Kyle Ng

Setup instructions:
    1. Ensure you have a 64 bit raspi OS running Python 3.???+
    2. run `sudo apt install build-essential libdbus-glib-1-dev libgirepository1.0-dev libpython3-dev libdbus-1-dev`
    3. run `sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0`
    4. run `pip install -r requirements.txt` 

Execution instructions:
    1. If beginning as a server run `python3 e2e/e2e_client_server.py -server -l en` replacing 'en' with native language 
    2. If beginning as a client run `python3 e2e/e2e_client_server.py --client MAC_ADDRESS -l en` replacing MAC_ADDRESS with the bluetooth MAC address of the server and 'en' with native langugage 

External libraries used (also see requirements.txt):
    - wavio
    - scipy
    - sounddevice
    - pydub
    - dbus-python
    - bluedot
    - torch
    - transformers
    - datasets
    - sentencepiece
    - ChatTTS
