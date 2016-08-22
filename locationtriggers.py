from itertools import repeat
import csv
import datetime
filename= "C:\\Users\\John\\Downloads\\libesedb-20160622\\esedbtools\\10AugExport.export\\LocationTriggers.15"
with open(filename,'r') as tsvin, open('new.csv', 'w') as csvout:
    tsvin = csv.reader(tsvin, delimiter='\t')
    firstline = True
    for row in tsvin:
        if firstline:
            firstline = False
            writer = csv.DictWriter(csvout, delimiter= ',', lineterminator='\n', fieldnames = ["Id", "Latitude", "Longitude","Radius",
                                     "GeofenceState","RuleInstanceId", "RuleStatus","RuleErrorCode","StartDate", "RecurrenceUnit","Name",
                                      "AddressQuery","EntityId","EntityInfoUrl","EntityType","RuleErrorMessage"])
            writer.writeheader() 
            continue
        #print(value)
        writer.writerow({'Id': row[0],"Latitude":row[1], "Longitude":row[2],'Radius':row[3], "GeofenceState":row[4],
                         "RuleInstanceId": row[5], "RuleStatus": row[6],"RuleErrorCode": row[7],"StartDate": row[8],
                         "RecurrenceUnit": row[9],"Name": row[10],"AddressQuery": row[11],"EntityId": row[12],"EntityInfoUrl": row[13],
                         "EntityType": row[14],"RuleErrorMessage": row[15]})
