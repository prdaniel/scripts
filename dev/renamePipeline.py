import os
oldTMI = raw_input('old tmi number? ')
newTMI = raw_input('new tmi number? ')
[os.rename(f, f.replace(oldTMI, newTMI)) for f in os.listdir('.') if not f.startswith('.')]