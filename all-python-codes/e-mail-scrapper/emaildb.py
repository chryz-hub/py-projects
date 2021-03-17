# download sqlite browser to really run this program
import sqlite3
# create an sqlite database called 'emailc' and a database handle = cur
conn = sqlite3.connect('emailc.sqlite')
cur = conn.cursor()

# make a table
cur.execute('DROP TABLE IF EXISTS Counts')

# making column in the table
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')
# file input for users
fname = input('Enter file name: ')
# if the enter key is pressed 'emailfile.txt' is the file automatically
if (len(fname) < 1): fname = 'mbox.txt'
#file handle
fh = open(fname)
# a loop that prints out the email org
for line in fh:
    # parsing through
    if not line.startswith('From '): continue
    pieces = line.split()
    email = pieces[1]
    info1 = email.find('@')
    info2 = email.find(' ', info1)
    org = email[info1 + 1:info2]

#inserting the email org into the sql database
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    # updating the count if same org is present in the database
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
    conn.commit()


# https://www.sqlite.org/lang_select.html
#the top ten email org avialable
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

#looping to print them out
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
