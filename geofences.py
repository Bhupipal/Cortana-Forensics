from itertools import repeat
import csv
import datetime
filename= "C:\\Users\\John\\Downloads\\libesedb-20160622\\esedbtools\\10AugExport.export\\Geofences.14"
with open(filename,'r') as tsvin, open('new.csv', 'w') as csvout:
    tsvin = csv.reader(tsvin, delimiter='\t')
    firstline = True
    for row in tsvin:
        if firstline:
            firstline = False
            writer = csv.DictWriter(csvout, delimiter= ',', lineterminator='\n', fieldnames = ["ID", "Time", "State",
                                                          'Latitude', 'Longitude', 'Accuracy', 'Speed', 'Heading', 'PositionSource'])
            writer.writeheader() 
            continue
        datetimevalue = int(row[1])
        #print(datetimevalue)
        googlechromevalue = datetimevalue / 10 # omit the last digit
        value = datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=googlechromevalue)
        #print(value)
        writer.writerow({'ID': row[0],"Time":value, "State":row[2],'Latitude': row[3], 'Longitude':row[4],'Accuracy':row[5],
                        'Speed':row[6],'Heading':row[7],'PositionSource':row[8]})
  
