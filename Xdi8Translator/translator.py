from .data import *
from jieba import lcut

class Translator():
    def hanzi2xdi8(self, text, fenci=True):
        if fenci:
            ltext=lcut(text)
            text=' '.join(ltext)
            for fro, to in hanzi2xdi8_dict.items():
                if to[0] not in '''!"#$%&'()*+,-./:;<=>?@[\]^_`{¦}~､''':
                    text=text.replace(fro,to)
                else:
                    text=text.replace(fro,'\b'+to)
        else:
            for fro, to in hanzi2xdi8_dict.items():
                if to[0] not in '''!"#$%&'()*+,-./:;<=>?@[\]^_`{¦}~､''':
                    text=text.replace(fro,' '+to)
                else:
                    text=text.replace(fro,to)
            text=text[1:]
        text=text.replace('\n ','\n')
        for punct in ['(','[','"',"'",'{']:
            text=text.replace(punct+' ',' '+punct)
        return text
    
    def tidai2xdi8(self, text):
        for fro, to in tidai2xdi8_dict.items():
            text=text.replace(fro,to)
        return text
    
    def xdi82kana(self, text):
        start=end=0
        textlist=[]
        while end<=len(text):
            if text[start] not in allxdi8:
                textlist.append(text[start])
                start+=1
                end+=1
            else:
                while text[start:end+1] in xdi82kana_dict and end<len(text)+2:
                    end+=1
                textlist.append(xdi82kana_dict[text[start:end]])
                start=end
        return ''.join(textlist)