# Real-Time End-to-End  IoT Edge Translation (REIET)
___
## Table of Contents
1. [Introduction](#introduction)
   - [Motivation](#motivation)
2. [Pipeline and Tech Stack](#pipeline-and-tech-stack)
   - [Tech Stack](#tech-stack)
   - [Pipeline](#pipeline)
3. [Instructions](#instructions)
   - [Prerequisites](#prerequisites)
   - [Installing](#installing)
     - [Linux Dependencies](#linux-dependencies)
     - [Mac/Windows Dependencies](#macwindows-dependencies)
4. [Running the Server](#running-the-server)
5. [Running the Client](#running-the-client)
6. [Running the Transcript](#running-the-transcript)
7. [How to Contribute](#how-to-contribute)

## Introduction
Real-Time End-to-End  IoT Edge Translation (`REIET`) is an IoT Edge translation pipeline designed to allow speakers of different languages communicate seamlessly in real time.

What makes `REIET` special?
1. Deploying on IoT Edge
	1. Rather than relying on Cloud APIs, we use small Language Models to run the entire Automatic Speech Recognition (ASR), Translation, and Text to Speech (TTS) pipeline **on device**
	2. Rather than choosing general purpose large models, we use <small>smol</small> domain specific models (i.e. Whisper-Base/Seq2Seq Translation model) to meet RAM and latency requirements
2. Wifi No More
	1. Most conversations happen spontaneously and face to face where a strong wifi connection may not be possible
	2. In combination with on device ML inference, we utilize bluetooth as our data link to provide a **Wifi-less mode** so `REIET` can translate where you communicate
3. Distributed Topology (Hardware Agnostic)
	1. `REIET` was originally designed to run on Linux devices but requires knowing MAC addresses before hand for bluetooth data link
	2. To allow `REIET` to support an arbitrary number of nodes across different localities (places), we also support an experimental [MQTT (OSI Application Layer) Pub/Sub Architecture](https://aws.amazon.com/what-is/mqtt/) mode
### Motivation
With the innovation in Natural Language Processing (NLP), we seek to bridge the multilingual communication gap with a simple mission:

**Help people have natural, meaningful conversations in their [Native Language](https://www.brainyquote.com/quotes/nelson_mandela_121685)**

## Pipeline and Tech Stack
### Tech Stack
1. Machine Learning Stack 
	1. Pytorch (Inference)
	2. HuggingFace (Inference)
	3. ChatTTS (Text to Speech)
	4. OpenAI Whisper-Base
2. Audio Processing Stack
	1. Wavio
	2. Pydub
3. Communication Protocol Stack
	1. Bluedot
	2. Paho-MQTT
	3. Wavio + Sounddevice
### Pipeline
![REIET E2E Pipeline Image](assets/E2E_Translation_Flowchart.png)
For full writeup checkout: [tinyurl.com/REIET-writeup](https://tinyurl.com/REIET-writeup)

<small>The flowchart above shows the pipeline from Listener RPi to Speaker RPi. Since both RPi's are both Listeners and Speakers, the pipeline is replicated symmetrically and bidirectionally</small>

| Step | Task                               | IoT Device              | Protocol       | Processing Technique                                         |
| ---- | ---------------------------------- | ----------------------- | -------------- | ------------------------------------------------------------ |
| 1    | Record Audio                       | Microphone              | USB            | SoundDevice + Wavio                                          |
| 2    | Automatic Speech Recognition (ASR) | Raspberry Pi (Speaker)  | Bluetooth/MQTT | OpenAI Whisper, Deep Learning Transformer Architecture model |
| 3    | Translation + Text to Speech (TTS) | Raspberry Pi (Listener) | ~              | Helsinki-NLP for translation and ChatTTS for text to speech  |
| 4    | Play Audio                         | Headphones              | Audio Jack     | Pydub audio playback library                                 |
| 5    | Visualize Transcription            | Raspberry Pi or Laptop  | HTTPS          | FlaskAPI from JSON log file to a Web Server                  |

## Instructions
___
### Prerequisites
1. 64-bit Operating System
	1. The RPi default image has a 32-bit OS, a 64-bit OS can be found under [Raspberry Pi OS with desktop and recommended software](https://www.raspberrypi.com/software/operating-systems/#raspberry-pi-os-64-bit)
2. `Python 3.10` (Pytorch and ChatTTS)
	1. Note: `Python3.12` comes with the RPi image linked above
___
### Installing
1. Clone Repository
```zsh 
git clone git@github.com:Ky-Ng/REIET.git
cd REIET
```
#### Linux Dependencies
- Install script 
```zsh
source install.sh
```

#### Mac/Windows Dependencies
```
pip3 install -r requirements-local.txt
```
___
## Running the Server
- Run the server device by specifying the `-c` flag
```
python3 e2e/e2e_client_server.py -s -l <LANGUAGE_ISO_639_CODE>
```
## Running the Client
- Run the client device by specifying the `-c` flag
- The `MAC_ADDRESS` is the MAC address of your Server node
```
python3 e2e/e2e_client_server.py -c <MAC_ADDRESS> -l <LANGUAGE_ISO_639_CODE>
```

## Running the Transcript
- View the transcript on either the Server or Client through a flask server
	- Note: you will need to refresh the web browser when the new audio message is received
```
python3 gui/flask-server.py
```

- Note: the `-l` language options are `en` for English and `zh` for Chinese
## How to Contribute
If you're interested in contributing to this repository, feel free to make a [Pull Request](https://github.com/Ky-Ng/REIET/pulls) or contact Jonathan Ong (ongjd \[at] usc \[dot] edu) and Kyle Ng (kgng \[at] usc \[dot] edu)