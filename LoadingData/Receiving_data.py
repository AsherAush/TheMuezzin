from pathlib import Path
import json
import os
# my_path = Path("C:\podcasts")


class send_info_data:
    def __init__(self, path):
        self.path = Path(path)
        self.files = [x for x in self.path.iterdir() if x.is_file()]

    def get_data(self):
        data = []
        for file in self.files:
            file_info = {
                "full_path": str(file.resolve()),
                "mathdata" : {
                "Name suffix": file.name,
                "name": file.stem,
                "file type": file.suffix,
                "size_MB": file.stat().st_size / (1024**2),
                "creation_time": file.stat().st_ctime,
                "is_file" : file.is_file()
                }

            }
            data.append(file_info)


        return json.dumps(data, indent=4)

# if __name__ == "__main__":
#     sender = send_info_data(my_path)
#     data = sender.get_data()
#     print(data)