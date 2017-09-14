import pickle

dbfilename = 'Assignment3.dat'


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
    while (True):
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ")
        if parse[0] == 'add':
            try:
                if parse[2].isdigit() and parse[3].isdigit():
                    record = {'Name': parse[1], 'Age': parse[2], 'Score': parse[3]}
                    scdb += [record]
                else:
                    print("Please input correct key.")
            except:
                print("Please input correct key.")
        elif parse[0] == 'find':
            try:
                for n in scdb:
                    if n['Name'] == parse[1]:
                        print("Age=" + n['Age'] + " Name=" + n['Name'] + " Score=" + n['Score'])
            except:
                print("Please input correct key.")
        elif parse[0] == 'inc':
            try:
                amount = int(parse[2])
                for i in scdb:
                    i['Score'] = int(i['Score'])
                    if i['Name'] == parse[1]:
                        i['Score'] += amount
                    i['Score'] = str(i['Score'])
            except:
                print("Please input correct key.")
        elif parse[0] == 'del':
            try:
                for m in range(len(scdb)):
                    for p in scdb:
                        if p['Name'] == parse[1]:
                            scdb.remove(p)
                            break
            except:
                print("Please input correct key.")
        elif parse[0] == 'show':
                sortKey = 'Name' if len(parse) == 1 else parse[1]
                showScoreDB(scdb, sortKey)
        elif parse[0] == 'quit':
            break
        else:
            print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):
    try:
        for p in sorted(scdb, key=lambda person: person[keyname]):
            for attr in sorted(p):
                print(attr + "=" + p[attr], end=' ')
            print()
    except:
        print("Please input correct key.")

if __name__ == "__main__":
    scoredb = readScoreDB()
    doScoreDB(scoredb)
    writeScoreDB(scoredb)

