from string import ascii_lowercase
import codecs
import sys
import os.path

# minified version, without line breaks
minified = False

def createindex():
    alpha = ""
    alpha += '<div id="overlay">'
    alpha += '<div class="masonry-container">'
    i = 0
    for c in ascii_lowercase:
        i += 1
        alpha += '<a class="button1" href="#' + c + '">' + c.upper() + '</a>'
        
        # line break
        if i % 3 == 0:
            alpha += ""
    alpha += "</div>" # /index
    alpha += "</div>" # /overlay
    # javascript for the mask
    alpha += """<div id='mask' onclick="document.location='#';"></div>"""
    return alpha

def file2text(f):
    with codecs.open(f, 'r','utf-8') as myfile:
        return myfile.read().replace('\n', ' ')

def template(tname,vars=[]):
    with codecs.open('templ/' + tname + '.html', 'r','utf-8') as myfile:
        t = myfile.read()
        if len(vars) > 0:
            for name,value in vars:
                t = t.replace('${{'+name+'}}',value)
        return t
    
def createCapitalLetter(s):
    # create anchor and capital letter
    return '<a name="' + s.lower() + '"><br><h2>'+ s.upper() + '</h2>'
        
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
    println(h,file2text("style.css"))
    println(h,'</style>');
    println(h,'<title>' + title + '</title>')
    println(h,"</head>")
    println(h,"<body>")
    println(h,'<h1>' + title + '</h1>')
    println(h,createindex())
    println(h,'<section id="content">')
    println(h,template('slider'))
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

    println(h,"</section>")
    println(h,template('footer',[('title',title)]))
    println(h,"</body></html>")
    h.close()

def checkfile(fname):
    if not os.path.isfile(fname):
        print("Missing file " + fname)
        sys.exit(1)
        
def main():
    if len(sys.argv) < 4:
        print("Usage: python tohtml.py <input> <output> <title>")
    
    checkfile(sys.argv[1])
    
    writehtml(sys.argv[1],sys.argv[2],sys.argv[3])

if __name__ == "__main__":
    main()