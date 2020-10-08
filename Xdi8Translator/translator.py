from .data import *

class Translator():
    def hanzi2xdi8(self, text):
        for fro, to in hanzi2xdi8_dict.items():
            if ord(to[0])>48:
                text=text.replace(fro,' '+to)
            else:
                text=text.replace(fro,to)
        text=text[1:]
        return text
    
    def tidai2xdi8(self, text):
        for fro, to in tidai2xdi8_dict.items():
                text=text.replace(fro,to)
        return text
    
t=Translator()
