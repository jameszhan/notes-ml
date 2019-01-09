import sys
from P4 import P4, P4Exception
from rhea.codes.python import re

NEW_DESCRIPTION = '<enter description here>'
DESCRIPTION_TEMPLATE = 'Mingle #Num: Your comment'
GLOBAL_PATTERN = re.compile("(?<!#)\s*Description\s*:\s*([^\n]+)[\n|$]", re.M | re.S);

def show_error_message(msg):
    sys.exit(msg)
	
def visit_p4(callback):
    p4 = P4()
    p4.port = 'localhost:1666'
    p4.client = 'james'
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

def edit_description():
    def edit(p4):
        p4.run("change -f")
    visit_p4(edit)


if(__name__ == "__main__"):
    edit_description()
    try:
       # raise RuntimeError("abc")
       pass
    finally:
        #sys.exit(0)
        pass
