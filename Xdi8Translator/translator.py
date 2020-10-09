from .data import *
from jieba import lcut

class Translator():
    def hanzi2xdi8(self, text, fenci=True):
        if fenci:
            ltext=lcut(text)
            text=' '.join(ltext)
            for fro, to in hanzi2xdi8_dict.items():
                if ord(to[0])>48:
                    text=text.replace(fro,to)
                else:
                    text=text.replace(fro,'\b'+to)
        else:
            for fro, to in hanzi2xdi8_dict.items():
                if ord(to[0])>48:
                    text=text.replace(fro,' '+to)
                else:
                    text=text.replace(fro,to)
            text=text[1:]
        text=text.replace('\n ','\n')
        text=text.replace('( ',' (')
        return text
    
    def tidai2xdi8(self, text):
        for fro, to in tidai2xdi8_dict.items():
                text=text.replace(fro,to)
        return text
