import MySQLdb

db = MySQLdb.connect(host='localhost',
                     user='root',
                     passwd='root123',
                     db='sam_new')
cur = db.cursor()

#create( (:Person {name: 'Baby'})-[:DRIVE]->(:Car {name: 'Honda'}) )
def create_relationship():
    cur.execute('SELECT * FROM NODELINK')

    outf = open('nodelink.cyp', 'w')
    for row in cur.fetchall():
        #its important to leave a blank between CREATE and (
        cql = 'CREATE ( (:Node {NODEID: \'' + str(row[0]) + '\'})-[:' + str(row[2]) + ']->(:Node {NODEID:\'' + str(row[1]) + '\'}) )' 
        outf.write(cql + ';' + '\n')
    
    outf.close()


def main():

    #create relationship
    create_relationship()


if __name__ == '__main__':
      main()
