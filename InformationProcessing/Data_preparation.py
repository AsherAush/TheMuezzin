
import json
class preparationData:
    def __init__(self, data):
        self.data = data
        self.data = dict(json.loads(self.data))

    def create_id(self):

        self.data['_id'] = (f"{self.data["mathdata"].get("name", "")}"
                            f"_{self.data["mathdata"].get("size_MB", "")}"
                            f"_{self.data["mathdata"].get("creation_time", "")}")

        return self.data

    def data_to_elastic(self):
        elastic_data = {
            "id" : self.data['_id'],
            "name": self.data["mathdata"].get("name"),
            "Name suffix": self.data["mathdata"].get("Name suffix"),
            "file type": self.data["mathdata"].get("file type"),
            "size_MB": self.data["mathdata"].get("size_MB"),
            "creation_time": self.data["mathdata"].get("creation_time"),
            "is_file": self.data["mathdata"].get("is_file"),
        }
        return elastic_data

    def data_to_mongo(self):
        mongo_data = {
            "_id": self.data['_id'],
            "full_path": self.data.get("full_path"),

        }
        return mongo_data


