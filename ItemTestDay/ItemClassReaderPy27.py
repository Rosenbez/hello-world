import csv

itemNum = []
UPC = []
group = []
testDay = []
UPCsearch= ''


def Readcsv():
    with open('ItemClassifications.csv') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            itemNum.append(row[0])
            UPC.append(row[1])
            group.append(row[2])
            testDay.append(row[7])


## to search for num use UPC.index(scannedupc)
## then return the group use group[upcindex]

Readcsv()
print('type stop to end')
print('')

while UPCsearch != 'stop':
    
    UPCsearch = raw_input('Input UPC: ') #take UPC input
    if UPCsearch == 'stop':
        break
    
    if UPCsearch[0] == '0':
        UPCsearch = UPCsearch[1:]

    
    ##print(UPCsearch)

    try:
        UPCindex = UPC.index(UPCsearch) #search for value in UPC codes

        ##print(UPCindex)

        groupNum = group[UPCindex]
        dayNum = testDay[UPCindex]

        print("Group: %s , Day: %s" % (groupNum, dayNum))

    except ValueError:
        print("value not in list \n")
    
