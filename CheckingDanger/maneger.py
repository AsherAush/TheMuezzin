from ElasticPull_out import Pull_elastic
from DecodingText import Decoding
import os
from dotenv import load_dotenv
load_dotenv()





a = Pull_elastic(os.getenv("ELASTICSEARCH_URL"), os.getenv("ELASTIC_INDEX"))
b= a.pull()
c = Decoding()
test = c.decodingHostile()
test1 = c.decodingLassHostile()
for key, value in b.items():
    print(key)
    count = 0
    count1 = 0
    for word in test.lower().split(","):
        counter = value.lower().count(word)
        if counter:
            count += 1
        # if word in value.lower():
    print("1", count / len(value))
    for word in test1.lower().split(","):
        counter = value.lower().count(word)
        if counter:
            count1 += 1
    print("2", count1 / len(value))

    #     if word in value.lower():
    #         print("2", word)
