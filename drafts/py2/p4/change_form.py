from P4 import P4, P4Exception
import sys
import os
from rhea.codes.python import re


def show_error_message(msg):
	sys.exit(msg)
#    raise RuntimeError(msg)

def visit_p4(callback):
    p4 = P4()
    log = open("d:/p4_trigger.log", 'a')
    p4.port = 'localhost:1666'
    try:
        p4.connect()       
        return callback(p4, log)
    except P4Exception, ex:
        for err in p4.errors:
            log.writelines(err)
        log.write(str(ex) + "\n")
    finally:
        log.close()
        p4.disconnect()


def change_desc(id):
    def desc(p4, log):
        cl = p4.fetch_change(id)
        log.writelines(str(cl) + "\n")
        return cl['Description']
    return visit_p4(desc)


def check_desc(cl):
    description = change_desc(cl)
    if(description == None):
        show_error_message("Can't get description for change list " + str(cl) + ", please check the log.\n"
            + "Please check the p4 script file configuration.")
    else:
        #example: Mingle Create a P4 trigger to prepopulate checkins to a branch.#38: Any comments.
        regex = "^Mingle\s+[^#]+#\d+\s*:\s*.+$"
        if(re.match(regex, description) == None):
            def edit(p4, log):
                change = p4.fetch_change(cl)
                change._description = "Mingle {mingle functionality card # from domain project}: {comments}"

            visit_p4(edit)
            show_error_message("""Your description must match the following format: \n
                Mingle {mingle functionality card # from domain project}: {comments}\n\n
                Example:\n
                Mingle Create a P4 trigger to prepopulate checkins to a branch.#38: Any comments.
            """)
			
def default_desc():
    def edit(p4, log):
        change = p4.fetch_change()
        change._description = "Mingle {mingle functionality card # from domain project}: {comments}"
        p4.run_sync()
    visit_p4(edit)

        

if(__name__ == "__main__"):
    default_desc()




