import sqlite3
user = input("Enter username: ")
print("Who is pm ")
print("1. MM 2. NM")
score = 0
ans = input("Enter answer: ")
if ans == '2':
    print("correct")
    score += 10
else:
    print("incorrect")
    score -=10
print("Who is pre")
print("1. DM 2. NM")
ans = input("Enter answer: ")
if ans == '1':
    print("correct")
    score += 10
else:
    print("incorrect")
    score -=10
    
dbName = "QuizDbPython.db"
databaseSystemReference = sqlite3.connect(dbName)
cursor = databaseSystemReference.cursor()

cursor.execute('''
               create table
                if not exists
                MiniM
               (playerName text,
               score int)''')

# cursor.execute('''delete from MiniM''')


# listOfTuples = [("A",100),("B",190),("C",87),("D",133),("E",25)]
listOfTuples= [(user,score)]

 
try:
    for playerName,score_ in listOfTuples:
        cursor.execute('''select count(*) from MiniM where playerName=?''',(playerName,))
        if cursor.fetchone()[0]==0:
            cursor.execute('''insert into MiniM(playerName,score) values(?,?)''',(playerName,score_))
        else:
            cursor.execute('''update MiniM set score = ? where playerName = ?''',(score_,playerName))
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
