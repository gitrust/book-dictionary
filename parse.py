import codecs
import sys

# strings to remove
rem = ['"','.',',','!','?',';',':','(',')']


def printwords(str):
    a = str.split(" ")
    for s in a:
        # replace charsmak
        for r in rem:
            s = s.replace(r,'')
        # take only words with at least 3 characters
        if s and len(s.strip()) > 2:
            # skip digits and not-alphanumeric 
            if s[0:1].isdigit() or not s[0:1].isalpha():
                continue
            print(s.encode("utf-8"))

def parsecontent(f):
    input = codecs.open(f,"r","utf-8")

    for line in input:
        printwords(line)

    input.close()


def main():
    parsecontent(sys.argv[1])
    
if __name__ == "__main__":
    main()

