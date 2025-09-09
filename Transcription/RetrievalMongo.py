from pymongo import MongoClient
from gridfs import GridFS
from bson.objectid import ObjectId
import os
from dotenv import load_dotenv
load_dotenv()

class Retrieval_mongo:
    def __init__(self, uri: str, db_name: str):
        try:
            self.client = MongoClient(uri)
            self.db = self.client[db_name]
            self.fs = GridFS(self.db)
        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")

    def retrieve_file(self):
        print(self.db.list_collection_names())
        return self.fs

        # for file in self.fs.find():
        #     fileid = file._id
        #     grid_out = self.fs.get(fileid)
        #     return grid_out

            # if grid_out:
            #     output_filepath = f"C:/ASD/{file.file_id}.wav"
            #     with open(output_filepath, "wb") as f:
            #         f.write(grid_out.read())
            #     print(f"WAV file extracted to {output_filepath}")
            # else:
            #     print("File not found in GridFS.")




# a = Retrieval_mongo(os.getenv("MONGO_URL"), os.getenv("DB_NAME"))
# asd = a.retrieve_file()
# for item in asd:
#     print(type(item))
