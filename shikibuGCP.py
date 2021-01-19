import speech_recognition as sr
import os
import sys
import datetime

AUDIO_FILE = sys.argv[1]
LANGUAGE = sys.argv[2]

print("AUDIOFILE = {}".format(AUDIO_FILE))
print("LANGUAGE = {}".format(LANGUAGE))
# recognize speech using Microsoft Azure Speech
GOOGLE_SPEECH_RECOGNITION_API_KEY = os.environ['GOOGLE_SPEECH_RECOGNITION_API_KEY']
# use the audio file as the audio source
r = sr.Recognizer()
offset =0
print("Recognition Result")
with sr.AudioFile(AUDIO_FILE) as source:
    while offset < source.DURATION:
        audio = r.record(source,duration=60) # read the entire audio file
        print("{} - {} ".format(datetime.timedelta(seconds=offset), datetime.timedelta(seconds=offset +60)))
        offset = offset + 60
        try:
            result = r.recognize_google(audio, key=GOOGLE_SPEECH_RECOGNITION_API_KEY,language=LANGUAGE)
            print(result)
        except sr.UnknownValueError:
            print("Google Speech could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech service; {0}".format(e))

print("End of Recognition")