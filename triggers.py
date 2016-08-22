from itertools import repeat
import csv
import datetime
filename= "C:\\Users\\John\\Downloads\\libesedb-20160622\\esedbtools\\10AugExport.export\\Triggers.22"
with open(filename,'r') as tsvin, open('new.csv', 'w') as csvout:
    tsvin = csv.reader(tsvin, delimiter='\t')
    firstline = True
    for row in tsvin:
        if firstline:
            firstline = False
            writer = csv.DictWriter(csvout, delimiter= ',', lineterminator='\n', fieldnames = ["Id", "ReminderId", "Kind",
                                                          'CreationTime'])
            writer.writeheader() 
            continue
        datetimevalue = row[3]
        googlechromevalue = int(datetimevalue[:-1]) # omit the last digit
        value = datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=googlechromevalue)
        #print(value)
        writer.writerow({'Id': row[0],"ReminderId":row[1], "Kind":row[2],'CreationTime':value})
  
