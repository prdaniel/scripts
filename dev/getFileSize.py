import urllib

site = urllib.urlopen("//DANIEL-THANX:80/C$/Users/status.txt")
meta = site.info()
print meta.getheaders("Content-Length")