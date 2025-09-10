import os
from pymongo import MongoClient
import gridfs
from LoggerFile import Logger

logger = Logger.get_logger()


class Mongo:
    def __init__(self, uri, db_name):
        try:
            self.client = MongoClient(uri)
            self.db = self.client[db_name]
            self.fs = gridfs.GridFS(self.db)
            logger.info("Connected to MongoDB ")
        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")
            logger.error(f"Error connecting to MongoDB:")

    def upload_wav(self, file_path, fileId):
        with open(file_path, 'rb') as audio_file:
            file_id = self.fs.put(audio_file, _id=fileId, content_type='audio/wav')
        return str(file_id)

