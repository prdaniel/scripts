def recordStore(store, size, index):
    with open('E:/Endeca/Apps/GameStop/logs/recordStore.size','r') as record:
        with open('E:/Endeca/Apps/GameStop/logs/baseline_update.out', 'a') as log:
            records = []
            for line in record:
                line = line.split('Records read: ', 1)[-1].split('\n')[0]
                records.append(int(line))
            if records[index] > size:
                log.write(store+' '+str(records[index])+' PASSED\n')
                return True
            else:
                log.write('SEVERE '+store+' FAILED '+str(records[index])+' < '+str(size)+'\n')
                return False
				
recordStore('Trade-Recommerce',657,0)
recordStore('Trade-GamesConsolesAccessories',1235800,1)
recordStore('StoreLocations',4398,2)
				
