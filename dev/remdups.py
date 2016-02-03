def _remMMID_(rawFile,mmidFile):
    with open(rawFile) as result:
        unique = set(result.readlines())
        with open(mmidFile, 'w') as rmdump:
            rmdump.writelines(set(unique))

_remMMID_('barOwners.csv','barOwnersNoDup.csv')