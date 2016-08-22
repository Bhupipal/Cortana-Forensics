from itertools import repeat
import csv
import datetime
filename= "C:\\Users\\John\\Downloads\\libesedb-20160622\\esedbtools\\10AugExport.export\\ContactTriggers.23"
with open(filename,'r') as tsvin, open('new.csv', 'w') as csvout:
    tsvin = csv.reader(tsvin, delimiter='\t')
    firstline = True
    for row in tsvin:
        if firstline:
            firstline = False
            writer = csv.DictWriter(csvout, delimiter= ',', lineterminator='\n', fieldnames = ["Id", "RuleInstanceId","RuleStatus","RuleErrorCode",
                                                          "AggregateId","ContactHandle","ContactName", 'RuleErrorMessage'])
            writer.writeheader() 
            continue
        writer.writerow({'Id': row[0],"RuleInstanceId":row[1], "RuleStatus":row[2],'RuleErrorCode':row[3],
                         "AggregateId":row[4],"ContactHandle":row[5],"ContactName":row[6], 'RuleErrorMessage':row[7]})
  							
