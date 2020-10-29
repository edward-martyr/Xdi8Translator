from Xdi8Translator import Translator
import sys
if __name__ == '__main__':
    t = Translator()
    while True:
        text = sys.stdin.readline().strip()
        if text:
            print(t.xdi82hanzi(text))
        else:
            break