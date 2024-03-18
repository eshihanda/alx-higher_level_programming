#!/usr/bin/python3
"""
lists all states from the database in ascending order
where name of state matches argument given using MySQLdb
"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("""SELECT id, name FROM states WHERE name LIKE BINARY '{}' \
                ORDER BY states.id ASC""".format(argv[4]))
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
