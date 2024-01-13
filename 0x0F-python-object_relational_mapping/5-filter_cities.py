#!/usr/bin/python3
""" list all states order by id"""
import sys
import MySQLdb


if __name__ == "__main__" and len(sys.argv) == 5:
    user = sys.argv[1]
    passw = sys.argv[2]
    db = sys.argv[3]
    state = sys.argv[4]
    con = MySQLdb.connect(host='localhost',
                          port=3306, user=user,
                          passwd=passw, db=db)
    cur = con.cursor()
    qr = "SELECT cities.name FROM cities JOIN"
    qr += " states ON cities.state_id = states.id"
    qr += " WHERE states.name = %s ORDER BY cities.id;"
    cur.execute(qr, (state, ))

    print(", ".join(map(lambda x: x[0], cur.fetchall())))
    cur.close()
    con.close()
