import speech_recognition as sr
from RetrievalMongo import Retrieval_mongo
from pymongo import MongoClient
from gridfs import GridFS
import io
import os
from dotenv import load_dotenv
load_dotenv()

class Audio_transcription:
    def __init__(self, audio_file):
        self.audio_file = audio_file
        self.recognizer = sr.Recognizer()

    def transcribe(self, item) :
        # for item in self.audio_file.find():
            item = io.BytesIO(item.read())
            with sr.AudioFile(item) as source:
                audio_data = self.recognizer.record(source, duration=15)
                try:
                    text = self.recognizer.recognize_google(audio_data)
                    return  text
                except sr.UnknownValueError as e:
                    return f"Audio not clear enough to transcribe. {e}"
                except sr.RequestError as e:
                    return f"Could not request results; {e}"

