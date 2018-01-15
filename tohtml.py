from string import ascii_lowercase
import codecs

def createindex():
    alpha = ""
    for c in ascii_lowercase:
        alpha = alpha + '<a href="#' + c + '">' + c.upper() + '</a>&nbsp;&nbsp;'
    alpha = alpha + "<br><br>"
    return alpha

def createTitle(s):
    return '<a name="' + s.lower() + '"> <h2>'+ s.upper() + '</h2>'
        
def word(w):
    return w.strip() + "<br>"
    
def println(f,s):
    f.write(s + "\n")

f = codecs.open("translated.txt","r","utf-8")
h = codecs.open("dic.html","w","utf-8")

println(h,"<!DOCTYPE html>")
println(h,"<html>")
println(h,"<head>")
println(h,'<meta http-equiv="content-type" content="text/html; charset=UTF-8"/>')
println(h,"</head>")
println(h,"<body>")

lastchar=""
for line in f:
    lc = line[0:1].lower()
    if lc != lastchar:
        println(h,createTitle(lc))
        println(h,createindex())
    println(h,word(line))
    lastchar = lc
f.close()

println(h,"</body></html>")
h.close()
