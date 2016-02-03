import urllib2
bar = 'beach'
page = 36
test = 'chicago.metromix.com/browse/restaurants/price-range:16-25?page='
while page > 0:
    test = 'chicago.metromix.com/browse/restaurants/price-range:16-25?page='+str(page)
    site = open("C:/Daniel/dev/Bars/" + test.split('.')[0]+'MidRest'+str(page)+".html", 'w')
    site.write(urllib2.urlopen("http://" + test).read())
    page = page - 1
site.close()
