from .data import *
from jieba import lcut
import jieba

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

    def xdi8fenci(self, text):
        jieba.load_userdict('xdi8words.txt')
        text = text.replace(' ', '')
        ltext = lcut(text)
        segments = []
        for word in ltext:
            segments.append(word)
        return segments

    def xdi82hanzi(self, text, mode='fenci'):  # fenci：希顶语原文是否分词/字连写；chaos：原文空格是否混乱
        if mode == 'chaos':  # 混沌模式下，需先对混乱希顶文本去空格然后分词，接着对分词后的希顶文本进行“分字”
            text = text.replace(' ','')
            text = self.xdi8fenci(text)
            jieba.set_dictionary('charfreq.txt')
            res = []
            for word in text:
                lchar = lcut(word)
                l = []
                for xdi8 in lchar:
                    s = xdi8
                    for fro, to in hanzi2xdi8_dict.items():
                        if xdi8 == to:
                            s = fro
                            break
                    l.append(s)
                res.append(''.join(l))

        else:
            # if mode == 'fenci':
            jieba.load_userdict('charfreq.txt')
            ltext = lcut(text)
            # print(ltext)
            res = []
            for xdi8 in ltext:
                s = xdi8
                for fro, to in hanzi2xdi8_dict.items():
                    if xdi8 == to:
                        s = fro
                        break
                res.append(s)

        text = ''.join(res).replace(' ', '').replace('-','')
        text = text.replace('\n ', '\n')
        for punct in ['(', '[', '"', "'", '{']:
            text = text.replace(punct + ' ', ' ' + punct)
        return text
    
    def tidai2xdi8(self, text):
        for fro, to in tidai2xdi8_dict.items():
            text=text.replace(fro,to)
        return text

    def xdi82hanxie(self, text):
        for fro, to in xdi82hanxie_dict.items():
            text=text.replace(fro,to)
        return text

    def hanxie2xdi8(self, text):
        for fro, to in xdi82hanxie_dict.items():
            text=text.replace(to,fro)
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
