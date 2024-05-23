#!/usr/bin/python3
"""
lists all cities from the database in ascending order
with state name using MySQLdb
"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("SELECT cities.id, cities.name, states.name\
              FROM cities INNER JOIN states\
              ON cities.state_id=states.id\
              ORDER BY cities.id ASC")
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
