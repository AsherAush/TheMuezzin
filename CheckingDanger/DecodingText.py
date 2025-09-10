import base64


class Decoding:
    def __init__(self):
        self.hostile = self.returnHostile()
        self.lassHostile = self.returnLessHostile()




    def returnHostile(self):
        with open('HostileList.txt', 'r') as file:
            encoded_text = file.read()
            return encoded_text

    def returnLessHostile(self):
        with open('LessHostileList.txt', 'r') as file:
            encoded_text = file.read()
            return encoded_text

    def decodingHostile(self):
        decoded_bytes = base64.b64decode(self.hostile)
        decoded_text = decoded_bytes.decode('utf-8')
        return decoded_text

    def decodingLassHostile(self):
        decoded_bytes = base64.b64decode(self.lassHostile)
        decoded_text = decoded_bytes.decode('utf-8')
        return decoded_text

# a= Decoding()
# print(a.decodingHostile())
# print(a.decodingLassHostile())




# a = "the new cycle moves  fast but Gaza doesn't Free Palestine disappear when cameras do the blockade is still there and so is the humanitarian crisis exactly I read a report yesterday it said malnutrition is spreading among children that's a"
# for word in decoded_text.lower().split(","):
#     if word in a.lower():
#         print(word)