from P4 import P4, P4Exception
import sys

f = open("d:/p4test.txt", 'a')

def getDescription(id):
    p4 = P4()
    #p4.port = "1666"
    #p4.user = "james"
    #p4.client = "james"
    #p4.password = "122988"

    try:
        p4.connect()
        cl = p4.fetch_change(id)
        return cl['Description']
    except P4Exception, ex:
        print(ex)
    finally:
        p4.disconnect()


cl = sys.argv[1]
user = sys.argv[2]
desc = getDescription(cl)


f.write("\nHello World! ");
f.write("cl=")
f.write(cl)
f.write(",user=")
f.write(user)
f.write(",desc=")

f.write(desc)
f.write("\n");



