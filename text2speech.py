# Import necessary libraries
'''
Sarah; EXAVITQu4vr4xnSDxMaL
Laura; FGY2WhTYpPnrIDTdsKH5
Charlie; IKne3meq5aSn9XLyUdCD
George; JBFqnCBsd6RMkjVDRZzb
Callum; N2lVS1w4EtoT3dr4eOWO
Liam; TX3LPaxmHKxFdv7VOQHJ
Charlotte; XB0fDUnXU5powFXDhCwa
Alice; Xb7hH8MSUJpSbSDYk0k2
Matilda; XrExE9yKIg1WjnnlVkGX
Will; bIHbv24MWmeRgasZH58o
Jessica; cgSgspJ2msm6clMCkdW9
Eric; cjVigY5qzO86Huf0OWal
Chris; iP95p4xoKVk53GoZ742B
Brian; nPczCjzI2devNBz1zQrb
Daniel; onwK4e9ZLuTAKqWW03F9
Lily; pFZP5JQG7iQjIQuC4Bku
Bill; pqHfZKP75CvOlQylNhV4
Mimosa; OWjggqpCvWzAsZNNJz2n
JanLam; UEErRqOd5JCyZ5NDkOSk
JackyLin; iw8Dn5ZPGer2OlEEunx9


'''

import requests  # Used for making HTTP requests
import json  # Used for working with JSON data

Mimosa_VoiceID="OWjggqpCvWzAsZNNJz2n"

# Define constants for the script
CHUNK_SIZE = 1024  # Size of chunks to read/write at a time
XI_API_KEY = "sk_a5c26beacec538c8992dd375b9961ac260b9125d2c0de550"  # Your API key for authentication
VOICE_ID = Mimosa_VoiceID  # ID of the voice model to use

file1 = open('news.txt','r')
lines = file1.readline()
#TEXT_TO_SPEAK = "CrowdStrike has published a post incident review (PIR) of the buggy update it published that took down 8.5 million Windows machines last week. The detailed post blames a bug in test software for not properly validating the content update that was pushed out to millions of machines on Friday. CrowdStrike is promising to more thoroughly test its content updates, improve its error handling, and implement a staggered deployment to avoid a repeat of this disaster."  # Text you want to convert to speech

TEXT_TO_SPEAK = lines
#"CrowdStrike has published a post incident review (PIR) of the buggy update it published that took down 8.5 million Windows machines last week. The detailed post blames a bug in test software for not properly validating the content update that was pushed out to millions of machines on Friday. CrowdStrike is promising to more thoroughly test its content updates, improve its error handling, and implement a staggered deployment to avoid a repeat of this disaster."  # Text you want to convert to speech
OUTPUT_PATH = "output3.mp3"  # Path to save the output audio file

# Construct the URL for the Text-to-Speech API request
tts_url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/stream"

# Set up headers for the API request, including the API key for authentication
headers = {
    "Accept": "application/json",
    "xi-api-key": XI_API_KEY
}

# Set up the data payload for the API request, including the text and voice settings
data = {
    "text": TEXT_TO_SPEAK,
    "model_id": "eleven_multilingual_v2",
    "voice_settings": {
        "stability": 0.3,
        "similarity_boost": 0.7,
        "style": 0.0,
        "use_speaker_boost": True
    }
}

# Make the POST request to the TTS API with headers and data, enabling streaming response
response = requests.post(tts_url, headers=headers, json=data, stream=True)

# Check if the request was successful
if response.ok:
    # Open the output file in write-binary mode
    with open(OUTPUT_PATH, "wb") as f:
        # Read the response in chunks and write to the file
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            f.write(chunk)
    # Inform the user of success
    print("Audio stream saved successfully.")
else:
    # Print the error message if the request was not successful
    print(response.text)