import speech_recognition as sr
import os
import sys

AUDIO_FILE = sys.argv[1]
LANGUAGE = sys.argv[2]
#AUDIO_FILE = "out001.wav"
#LANGUAGE = "ja-JP"

print("AUDIOFILE = {}".format(AUDIO_FILE))
print("LANGUAGE = {}".format(LANGUAGE))
# recognize speech using Microsoft Azure Speech
AZURE_SPEECH_KEY = os.environ['AZURE_SPEECH_KEY']

# use the audio file as the audio source
r = sr.Recognizer()
offset =0
print("Recognition Result")
with sr.AudioFile(AUDIO_FILE) as source:
    while offset < source.DURATION:
        audio = r.record(source,duration=60) # read the entire audio file
        print("from {} sec to {} sec".format(offset, offset +60))
        offset = offset + 60
        try:
            result = r.recognize_azure(audio, key=AZURE_SPEECH_KEY,location="japaneast",language=LANGUAGE,show_all=False,result_format="simple",profanity="raw")
            print(result)
        except sr.UnknownValueError:
            print("Microsoft Azure Speech could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Microsoft Azure Speech service; {0}".format(e))

print("End of Recognition")