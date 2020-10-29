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

    def xdi82hanzi(self,text):
        ltext = lcut(text)
        res = []
        for word in ltext:
            in_table = False
            for fro, to in hanzi2xdi8_dict.items():
                if word == to:
                    res.append(fro)
                    in_table = True
                    break
            if not in_table:
                res.append(word)
        text = ''.join(res).replace(' ','')
        text = text.replace('\n ', '\n')
        for punct in ['(', '[', '"', "'", '{']:
            text = text.replace(punct + ' ', ' ' + punct)
        return text
    
    def tidai2xdi8(self, text):
        for fro, to in tidai2xdi8_dict.items():
            text=text.replace(fro,to)
        return text
    
    def xdi82kana(self, text):
        text=text.replace('⇧','')
        start=0;end=2
        tmp=''
        while len(text) > 0:
            if text[start] in allxdi8:
                if text[start:end] in xdi82kana_dict  and not end>len(text):
                    end+=1
                    continue
                tmp+=xdi82kana_dict[text[start:end-1]]
                text=text[end-1:]
                start=0;end=2
            else:
                tmp+=text[start]
                text=text[1:]
        return tmp
    
    def xdi82tidai(self, text):
        text=text.replace('⇧','')
        for fro, to in xdi82tidai_dict.items():
            text=text.replace(fro,to)
        return text
    
    def xdi82IPA(self, text):
        text=text.replace('⇧','')
        start=0;end=2
        tmp=''
        while len(text) > 0:
            if text[start] in allxdi8zimu:
                if text[start:end] in xdi82IPA_dict  and not end>len(text):
                    end+=1
                    continue
                tmp+=xdi82IPA_dict[text[start:end-1]]
                text=text[end-1:]
                start=0;end=2
            else:
                tmp+=text[start]
                text=text[1:]
        return tmp
