import sqlite3

conn = sqlite3.connect("dataset/organization.sqlite")
cur = conn.cursor()

cur.execute("CREATE TABLE Counts(org TEXT, count INTEGER)")

fh = open("dataset/mbox-short.txt")

for line in fh:
    if not line.startswith("From: "): continue
    words = line.split()
    email = words[1]
    org = email[email.find("@") + 1:]

    cur.execute("SELECT count FROM Counts WHERE org = ?", (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute("""INSERT INTO Counts (org, count)
        VALUES(?, 1)""", (org,))
    else:
        cur.execute("UPDATE Counts SET count = count + 1 WHERE org = ?", (org,))

    conn.commit()

query = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(query):
    print(str(row[0]), row[1])

cur.close()