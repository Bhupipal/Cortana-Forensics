from itertools import repeat
import csv
import datetime
filename= "C:\\Users\\John\\Downloads\\libesedb-20160622\\esedbtools\\10AugExport.export\\Reminders.19"
with open(filename,'r') as tsvin, open('new.csv', 'w') as csvout:
    tsvin = csv.reader(tsvin, delimiter='\t')
    firstline = True
    for row in tsvin:
        if firstline:
            firstline = False
            writer = csv.DictWriter(csvout, delimiter= ',', lineterminator='\n', fieldnames = ["Id", "Status", "SyncStatus",
                                                          'CreationTime', 'LastUpdateTime', 'LastAccessTime', 'CompletionTime', 'Title', 'Text'])
            writer.writeheader() 
            continue
        creationtimevalue, lastupdatetimevalue, lastaccesstimevalue, completiontime  = row[3], row[4], row[5], row[6]   
        creationtimevalue, lastupdatetimevalue, lastaccesstimevalue = int(creationtimevalue[:-1]),int(lastupdatetimevalue[:-1]), int(lastaccesstimevalue[:-1]) # omit the last digit
        value1 = datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=creationtimevalue)
        value2 = datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=lastupdatetimevalue)
        value3 = datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=lastaccesstimevalue)
        if completiontime != '-1':
            completiontimevalue = int(completiontime[:-1])
            value4 = datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=completiontimevalue)
        else:
            value4 = row[6]
        
        #print(value)
        writer.writerow({'Id': row[0],"Status":row[1], "SyncStatus":row[2],'CreationTime': value1, 'LastUpdateTime':value2,'LastAccessTime':value3,
                        'CompletionTime':value4,'Title':row[7],'Text':row[8]})
  

