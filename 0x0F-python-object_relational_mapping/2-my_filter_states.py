"""List states base on user input"""

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY\
                name='{}'".format(sys.argv[4]))
    [print(row) for row in cur.fetchall()]
    cur.close()
    db.close()
