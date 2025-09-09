from RetrievalMongo import Retrieval_mongo
from AudioTranscription import Audio_transcription
from SendElastic import Send_elastic
import os
from dotenv import load_dotenv
load_dotenv()

class main:
    def __init__(self):
        self.Retrieval = Retrieval_mongo(os.getenv("MONGO_URL"), os.getenv("DB_NAME"))
        self.fileDb = self.Retrieval.retrieve_file()
        self.transcription = Audio_transcription(self.fileDb)
        self.elastic = Send_elastic(os.getenv("ELASTICSEARCH_URL"), os.getenv("ELASTIC_INDEX"))

    def run(self):
        for audio in self.transcription.audio_file.find():
            text = self.transcription.transcribe(audio)
            id = audio.file_id
            try:
                self.elastic.update_document(id, text)
                print(f"Document {id} updated successfully.")
            except Exception as e:
                print(f"Failed to update document {id}. Error: {e}")
if __name__ == "__main__":
    main().run()

