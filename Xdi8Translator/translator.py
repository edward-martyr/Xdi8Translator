from .data import *
from jieba import lcut
import re

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

    def xdi82hanzi(self, text):
        xdi8words = [(i.span(),i.group()) for i in re.finditer("[0-9a-zA-Z]{1,}",text)]
        hanzvalues = list(hanzi2xdi8_dict.values())
        hanzkeys = list(hanzi2xdi8_dict.keys())
        for result in xdi8words[::-1]:
            if result[1] in hanzvalues:
                char=hanzkeys[hanzvalues.index(result[1])]
                text=text[:result[0][0]]+char+text[result[0][1]:]
        return text
