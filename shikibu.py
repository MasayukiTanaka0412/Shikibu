import speech_recognition as sr
import os
import sys

#AUDIO_FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "english.wav")
#AUDIO_FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test.mp4")
AUDIO_FILE = sys.argv[1]
LANGUAGE = sys.argv[2]
print("AUDIOFILE = {}".format(AUDIO_FILE))
print("LANGUAGE = {}".format(LANGUAGE))

# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source) # read the entire audio file

# recognize speech using Microsoft Azure Speech
AZURE_SPEECH_KEY = os.environ['AZURE_SPEECH_KEY']
try:
    print("Microsoft Azure Speech thinks you said " + r.recognize_azure(audio, key=AZURE_SPEECH_KEY,location="japaneast",language=LANGUAGE))
except sr.UnknownValueError:
    print("Microsoft Azure Speech could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Microsoft Azure Speech service; {0}".format(e))

