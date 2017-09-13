import pickle

dbfilename = 'assignment3.dat'


def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb = pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()


def doScoreDB(scdb):
    while(True):
        inputstr = (input("Score DB > "))
        if inputstr == "": continue

        parse = inputstr.split(" ")
        if parse[0] == 'add':
            scdb = addRecord(scdb, parse)
        elif parse[0] == 'del':
            scdb = deleteRecord(scdb, parse)
        elif parse[0] == 'show':
            sortKey = 'Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)
        elif parse[0] == 'find':
            findRecord(scdb,parse)
        elif parse[0] == 'inc':
            scdb = increaseRecord(scdb,parse)
        elif parse[0] == 'quit':
            break
        else:
            print("Invalid command: " + parse[0])


def searchRecord(scdb, parse):
    indexList = []
    for index in range(len(scdb)):
        if scdb[index]['Name'] == parse[1]:
            indexList += [index]
    return indexList


def showScoreDB(scdb, keyname):
    try:
        for record in sorted(scdb, key=lambda person: person[keyname]):
            printRecord(record)
    except:
        print("Unexpected key")


def printRecord(record):
    for attr in sorted(record):
        print(str(attr) + '=' + str(record[attr]), end=' ')
    print()


def addRecord(scdb, parse):
    record = {'Name': parse[1], 'Age': int(parse[2]), 'Score': int(parse[3])}
    scdb += [record]
    return scdb


def deleteRecord(scdb, parse):
    reversedIndexList = searchRecord(scdb,parse)[-1::-1]
    for index in reversedIndexList:
        scdb.pop(index)
    return scdb


def findRecord(scdb, parse):
    for index in searchRecord(scdb,parse):
        printRecord(scdb[index])


def increaseRecord(scdb, parse):
    for index in searchRecord(scdb,parse):
        scdb[index]['Score'] += parse[2]
    return scdb


if __name__ == "__main__":
    scoredb = readScoreDB()
    doScoreDB(scoredb)
    writeScoreDB(scoredb)
