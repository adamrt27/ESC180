import urllib.request

text = urllib.parse.quote("https://ca.search.yahoo.com/search?p=engineering+science&fr=yfp-t&fp=1&toggle=1&cop=mss&ei=UTF-8")

f = urllib.request.urlopen(text)
page = f.read().decode("utf-8")
f.close()
print(page)