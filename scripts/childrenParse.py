import fileinput
import sys
import os
import shutil

if os.path.exists('C:/Daniel/apps/wholesale/items.txt'):

    shutil.copy2('C:/Daniel/apps/wholesale/items.txt', 'C:/Daniel/apps/wholesale/itemsTemp.txt')
    shutil.copy2('C:/Daniel/apps/wholesale/items.txt', 'C:/Daniel/apps/wholesale/itemsParent.txt')
    os.remove('C:/Daniel/apps/wholesale/items.txt')
	    
    with open("C:/Daniel/apps/wholesale/itemsChild.txt", "w") as n:
        n.write("unique_id	date_added	name	url_detail	image	cost	price_retail	price_sale	price_sort	group_price_3	group_id	brand	description_short	sku	is_free_shipping	mpn\n")
    n.close()

    f = open('C:/Daniel/apps/wholesale/itemsParent.txt', 'r')
    n = open('C:/Daniel/apps/wholesale/itemsChild.txt', 'a')
    for line in f:
        if line[0:3] == 'SIE' or line[0:3] == '18-':
            n.write(line)
    n.close()
    f.close()

    for line_number, line in enumerate(fileinput.input('C:/Daniel/apps/wholesale/itemsParent.txt', inplace=1)):
        if line[0:3] == 'SIE' or line[0:3] == '18-':
            continue
        else:
            sys.stdout.write(line)

    num_lines = sum(1 for line in open('C:/Daniel/apps/wholesale/itemsChild.txt'))
    num_lines2 = sum(1 for line in open('C:/Daniel/apps/wholesale/itemsParent.txt'))
    num_lines3 = sum(1 for line in open('C:/Daniel/apps/wholesale/itemsTemp.txt'))
    totalLines = num_lines + num_lines2
	
    if totalLines >= num_lines3:
        print "Good Files"
    else:
        print 'bad files'
        os.remove('C:/Daniel/apps/wholesale/itemsParent.txt')
        os.remove('C:/Daniel/apps/wholesale/itemsChild.txt')
else:
    print "No new items file"
    
