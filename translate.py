
import codecs
from googletrans import Translator
import time
import sys



trans = Translator()

def transl(words,token):
    if not words or len(words) == 0:
        return []
    
    try:
        translated = []
        tlist = trans.translate(words,src='en',dest='de')
        for t in tlist:
            translated.append((t.origin,t.text))
        return translated
#json.decoder.JSONDecodeError
    except :
        print("Error at token: " + token)
        return []
    
def openfile(f,flags):
    return codecs.open(f,flags,"utf-8")

def trans_to_file(out,dic):
    translated =  transl(dic,"token")
    for origin, text in translated:
        line = origin + "  ::  " + text
        out.write(line + "\n")

def main():
    # TODO check which are already translated
    skip = -1
    
    #translated = already_translated_list(sys.argv[2])
    
    f = openfile(sys.argv[1],"r")    
    out = openfile(sys.argv[2],"a")
    
    # count of words to translate at once
    bucketsize = 70
    i = 0
    bucket = []
    for entry in f:
        i = i + 1
        entry = entry.strip()
        if  len(entry) == 0 or skip > i:
            continue
                
        # translate bucket
        if bucketsize == len(bucket):
            trans_to_file(out,bucket)
            bucket = []
        
        # gather all potential words into a bucket
        # to translate them in a bulk
        bucket.append(entry)

        if i % 10 == 0:
            print("Translated words: " + str(i))

    f.close()
    out.close()

if __name__ == "__main__":
    main()