import MySQLdb

db = MySQLdb.connect(host='localhost',
                     user='root',
                     passwd='root123',
                     db='ptd_mg')
cur = db.cursor()

#create( (:Person {name: 'Baby'})-[:DRIVE]->(:Car {name: 'Honda'}) )
def create_relationship():
    cur.execute('SELECT * FROM NODELINK')

    outf = open('nodelink.cyp', 'w')
    for row in cur.fetchall():
    
        cql = 'MATCH (n1:Node {NODEID: \'' + str(row[0]) + '\'}), (n2:Node {NODEID: \'' + str(row[1]) + '\'}) '
        #its important to leave a blank between CREATE and (
        cql = cql + 'CREATE ((n1)-[:' + str(row[2]) + ']->(n2))' 
        outf.write(cql + ';' + '\n')
    
    outf.close()


def main():

    #create relationship
    create_relationship()


if __name__ == '__main__':
      main()
