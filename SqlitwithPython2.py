import sqlite3

dbName = "QuizDb.db"
databaseSystemReference = sqlite3.connect(dbName)
cursor = databaseSystemReference.cursor()

cursor.execute('''
               create table
                if not exists
                MiniM
               (playerName text,
               score int)''')

cursor.execute('''delete from MiniM''')

# listOfTuples = [("A",100),("B",190),("C",87),("D",133),("E",25)]
listOfTuples= []
numberOfRecords = int(input("Enter number of records u want to enter: "))
for i in range(numberOfRecords):
    playerName = (input("Enter player name: "))
    score = int(input("Enter score: "))
    recordTuple = (playerName,score)
    listOfTuples.append(recordTuple)


try:
    for playerName,score in listOfTuples:
        cursor.execute('''select count(*) from MiniM where playerName=? and score = ?''',(playerName,score))
        if cursor.fetchone()[0]==0:
            cursor.execute('''insert into MiniM(playerName,score) values(?,?)''',(playerName,score))
            databaseSystemReference.commit()
except sqlite3.Error as e:
    print(f"the error is : {e}")

# fetching data
cursor.execute('''select * from MiniM''')
rows = cursor.fetchall()
for row in rows:
    print(row)



# releasing resources
cursor.close()
databaseSystemReference.close()
