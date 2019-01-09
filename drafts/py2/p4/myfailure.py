import sys
from P4 import P4, P4Exception


def show_error_message(msg):
    sys.exit(msg)
	
def visit_p4(callback):
    p4 = P4()
    p4.port = 'localhost:1666'
    try:
        p4.connect()       
        return callback(p4)
    except P4Exception, ex:
        errmsg = str(ex) + "\n"
        for err in p4.errors:
            errmsg += err
        show_error_message(errmsg)
    finally:
        p4.disconnect()


def fetch_description(id):
    def desc(p4):
        cl = p4.fetch_change(id)        
        return cl['Description']
    return visit_p4(desc)

if(__name__ == "__main__"):
    if(len(sys.argv) > 1):
        show_error_message("Must failure." + str(sys.argv))
        #show_error_message(fetch_description(sys.argv[1]))
    else:
        show_error_message("Must failure." + str(sys.argv))
