import os
from pymongo import MongoClient
import gridfs

# # Connect to MongoDB
# client = MongoClient('mongodb://localhost:27017/')  # Replace with your MongoDB connection string
# db = client["test"]  # Replace with your database name
# fs = gridfs.GridFS(db)
#
# wav_file_path ="C:\podcasts\download (1).wav"  # Replace with the actual path to your WAV file
#
# with open(wav_file_path, 'rb') as audio_file:
#     file_id = fs.put(audio_file, filename='DWFF', asd= "154", content_type='audio/wav')
#     print(f"WAV file uploaded with file_id: {file_id}")

class Mongo:
    def __init__(self, uri, db_name):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.fs = gridfs.GridFS(self.db)

    def upload_wav(self, file_path, fileId):
        with open(file_path, 'rb') as audio_file:
            file_id = self.fs.put(audio_file, file_id=fileId, content_type='audio/wav')
        return str(file_id)

    # def insert_one(self, data):
    #     result = self.collection.insert_one(data)
    #     return str(result.inserted_id)
