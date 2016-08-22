from itertools import repeat
import csv
import datetime
filename= "C:\\Users\\John\\Downloads\\libesedb-20160622\\esedbtools\\10AugExport.export\\TimeTriggers.21"
with open(filename,'r') as tsvin, open('new.csv', 'w') as csvout:
    tsvin = csv.reader(tsvin, delimiter='\t')
    firstline = True
    for row in tsvin:
        if firstline:
            firstline = False
            writer = csv.DictWriter(csvout, delimiter= ',', lineterminator='\n', fieldnames = ["Id", "DateTime", "RecurrenceUnit",
                                                          'RuleInstanceId', 'RuleStatus', 'RuleErrorCode', 'AppointmentId', 'RuleErrorMessage', 'LastTriggerTime'])
            writer.writeheader() 
            continue
        datetimevalue = row[1]
        googlechromevalue = int(datetimevalue[:-1]) # omit the last digit
        value = datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=googlechromevalue)
        #print(value)
        writer.writerow({'Id': row[0],"DateTime":value, "RecurrenceUnit":row[2],'RuleInstanceId': row[3], 'RuleStatus':row[4],'RuleErrorCode':row[5],
                        'AppointmentId':row[6],'RuleErrorMessage':row[7],'LastTriggerTime':row[8]})
  
