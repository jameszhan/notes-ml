import sys
from rhea.codes.python import re


def edit_description(formfile, callback):
    def fetch_form_content():
        f = open(formfile, "rt")
        try:
            content = "".join(f.readlines())
            return content;
        finally:
            f.close()
        
    def save_formfile(content):
        with open(formfile, "wt") as f:
            f.writelines(content)

    def fetch_description(content):
        p = re.compile(r"^Description:\s*(.+)$", re.M)
        desc = None
        m = p.search(content)
        if(m <> None):
            desc = m.group(1)      
        return desc
    
    content = fetch_form_content()
    desc = fetch_description(content)
    expectedcomment = callback(desc) 
    if(expectedcomment <> None):
        accept = re.compile(r"^Mingle\s*#?\s*\d+\s*:.+$", re.M | re.S) 
        if(accept.match(desc) == None):
            content = content.replace(desc, expectedcomment)
            save_formfile(content)
        

def default_description(formfile):
    def default_comment(desc):
        defaultcomment = "<enter description here>"
        if(desc == defaultcomment):
            return "Mingle #id: comments"
        else:
            return None
    edit_description(formfile, default_comment)


def check_description(formfile):
    def default_comment(desc):
        promptmessage = """Your description must match the following format:
                Mingle {#} id: {comments}
                Example:
                Mingle 38: Finished writing the P4 trigger to prepopulate checkin comments.
            """
        if(desc <> None):
            return "Mingle #id: comments"
        else:
            return None
    edit_description(formfile, promptmessage)
   

#Triggers
#   default_desc form-out change "{PYTHON_HOME}/python.exe {SCRIPT_HOME}/p4comment.py %formfile% %formtype%"
#   check_desc form-out change "{PYTHON_HOME}/python.exe {SCRIPT_HOME}/p4comment.py %formfile%



if(__name__ == "__main__"):
    if(len(sys.argv) == 3):
        #this is trigger form-out.
        default_description(sys.argv[1])
    elif(len(sys.argv) == 2):
        #this is trigger form-in.
        edit_description(sys.argv[1]);

