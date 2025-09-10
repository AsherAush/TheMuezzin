import speech_recognition as sr
from RetrievalMongo import Retrieval_mongo
from pymongo import MongoClient
from gridfs import GridFS
import io
import os
from dotenv import load_dotenv
load_dotenv()
import LoggerFile
logger = LoggerFile.Logger.get_logger()

class Audio_transcription:
    def __init__(self, audio_file):
        self.audio_file = audio_file
        self.recognizer = sr.Recognizer()

    def transcribe(self, item) :
            item = io.BytesIO(item.read())
            with sr.AudioFile(item) as source:
                audio_data = self.recognizer.record(source)
                try:
                    text = self.recognizer.recognize_google(audio_data)
                    logger.info("Transcription successful")
                    return  text
                except sr.UnknownValueError as e:
                    logger.error(f"Audio not clear enough to transcribe: {e}")
                    return f"Audio not clear enough to transcribe. {e}"
                except sr.RequestError as e:
                    logger.error(f"Could not request results; {e}")
                    return f"Could not request results; {e}"

