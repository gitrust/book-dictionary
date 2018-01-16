from string import ascii_lowercase
import codecs
import sys

# minified version, without line breaks
minified = True

def createindex():
    alpha = ""
    alpha += '<div class="index">'
    i = 0
    for c in ascii_lowercase:
        i += 1
        alpha = alpha + '<a href="#' + c + '">' + c.upper() + '</a>&nbsp;&nbsp;&nbsp;'
        if i % 13 == 0:
            alpha += "<br><br>"
    alpha = alpha + "</div><br><br>"
    return alpha

def createCapitalLetter(s):
    # create anchor and capital letter
    return '<a name="' + s.lower() + '"> <h2>'+ s.upper() + '</h2>'
        
def word(w):
    return "<p>" +w.strip() + "</p>"
    
def println(f,s):
    f.write(s)
    if not minified:
        f.write("\n")

def writehtml(input,output,title):    
    f = codecs.open(input,"r","utf-8")
    h = codecs.open(output,"w","utf-8")

    println(h,"<!DOCTYPE html>\n")
    println(h,"<html>")
    println(h,"<head>")
    println(h,'<meta http-equiv="content-type" content="text/html; charset=UTF-8"/>')
    println(h,'<style type="text/css">');
    println(h,' div.index {margin-left: 15px}')
    println(h,' p {margin: 2px; padding: 2px;}')
    println(h,' div.dic {font-size: 1.6em; margin-left: 15px;}')
    println(h,' a {font-size: 1.6em;}')
    println(h,' h2 {text-align: center;} ')
    println(h,'</style>');
    println(h,'<title>'+title+'</title>')
    println(h,"</head>")
    println(h,"<body>")
    println(h,"<h1>"+title+"</h1>")

    lastchar = ""
    opendiv = False
    
    # write dictionary and navigation index
    for line in f:
        lc = line[0:1].lower()
        
        if lc != lastchar:
            # close open div
            if opendiv:
                println(h,'</div>')
                opendiv = False
            println(h,createCapitalLetter(lc))
            println(h,createindex())
            
            # mark a dictionary block
            println(h,'<div class="dic">')
            opendiv = True
        println(h,word(line))
        lastchar = lc
    
    # close dictionary block
    if opendiv:
        println(h,'</div>')
        opendiv = False
    f.close()

    println(h,"</body></html>")
    h.close()

def main():
    writehtml(sys.argv[1],sys.argv[2],sys.argv[3])

if __name__ == "__main__":
    main()