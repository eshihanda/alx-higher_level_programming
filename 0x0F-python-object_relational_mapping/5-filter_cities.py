#!/usr/bin/python3
"""
lists all cities from the database in ascending order
matching state name passed in as argument using MySQLdb
"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("SELECT cities.name\
              FROM cities INNER JOIN states\
              ON cities.state_id=states.id\
              WHERE states.name=%s\
              ORDER BY cities.id ASC",
              (argv[4],))
    rows = c.fetchall()
    print(", ".join(row[0] for row in rows))
    c.close()
    db.close()
