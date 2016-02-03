with open("C:/Daniel/Scripts/new.txt", "wt") as fout:
    with open("C:/Daniel/Scripts/test.txt", "rt") as fin:
        for line in fin:
            fout.write(line.replace('/80/', '/200/'))