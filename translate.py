
import codecs
from googletrans import Translator
import time

skip = 7893

trans = Translator()

def transl(word):
    if not word or len(word.strip()) == 0:
        return ""
    try:
        s = trans.translate(word.strip(),src='en',dest='de').text.strip()
        return s
#json.decoder.JSONDecodeError
    except :
        print("Error at word: " + word)
        return ""

def openfile(f,flags):
    return codecs.open(f,flags,"utf-8")
    
f = openfile("sorted.txt","r")
out = openfile("translated.txt","a")

i = 0
for l in f:
    i = i + 1
    if not l or len(l.strip()) == 0 or skip > i:
        continue
    if i % 100 == 0:
        print("sleep 5s")
        time.sleep(5)
    line = l.strip() + "  ::  " + transl(l)
    out.write(line + "\n")

    if i % 10 == 0:
        print("Translated words: " + str(i))

f.close()
out.close()