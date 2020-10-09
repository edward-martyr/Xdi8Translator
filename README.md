# Xdi8Translator

A multiway Xdi8 Translator.

## Installation

```bash
pip install Xdi8Translator
```

## Usage

```python
from Xdi8Translator import Translator

translator=Translator()

tidai='''Xdi8 oㄜθ
ㄣiзk ∀y z 刀zz7ia ヲi 6卜 N人Bi8h ，
gi∀人vci з v εε loεy 卜ε卜 ㄜu8 ㄣз，
s2hieε q8q8 yu 1 bpi 刀6li8，
rue no c зq w刀卜 hie 人 r 8卜 4i 8人？
hi θ卜que卜 εt 2 bie f εo ヲwi θヲi 人，
x εrdi 8 s 2rdi8 isu 人 x εx x di8，
r 8卜su з t 1g ∀ su 人i n 8卜 iz ε，
li 6xa fa 7人i bxz 刀 B θmi з。'''

hanzi='''我一个人，在轻轻闲着，一个没有名字的光棍，杳杳深深，默默无闻，在陌生的桥头，遇见雨中散心的丽人，心里刹那，我爱丽人，拥抱我吧！煞去我的光棍，让我和甜蜜的你，偶然相吻。'''

print(translator.tidai2xdi8(tidai))
print(translator.hanzi2xdi8(hanzi))
print(translator.hanzi2xdi8(hanzi, fenci=False))
```
