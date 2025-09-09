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

# a = Retrieval_mongo(os.getenv("MONGO_URL"), os.getenv("DB_NAME"))
# asd = a.retrieve_file()
# # b = AudioTranscription("C:\ASD\download (16)_4.058160781860352_1757232713.3307304.wav")
# b = Audio_transcription(asd)
# for audu in b.audio_file.find():
#     print(b.transcribe(audu))
#     print(audu.file_id)