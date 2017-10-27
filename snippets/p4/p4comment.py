import sys
from rhea.codes.python import re


def fetch_description(formfile):
    def fetch_form_content():
        f = open(formfile, "rt")
        try:
            content = "".join(f.readlines())
            return content;
        finally:
            f.close()
            
    content = fetch_form_content()
    p = re.compile(r"^Description:\s*((?:.(?!Files))+)", re.M | re.S)
    desc = None
    m = p.search(content)
    if(m <> None):
        desc = m.group(1).strip()      
    return (desc, content)
        

def default_description(formfile):
    def save_formfile(content):
        with open(formfile, "wt") as f:
            f.writelines(content)
            
    desc, content = fetch_description(formfile)
    if(desc == "<enter description here>"):
        content = content.replace(desc, "AAAMingle #id: comments")
        save_formfile(content)

def check_description(formfile):
    promptmessage = """Your description must match the following format:
            Mingle {#} id: {comments}
            Example:
            Mingle 38: Finished writing the P4 trigger to prepopulate checkin comments.
        """
    acceptpattern = re.compile(r"^Mingle\s*#?\s*\d+\s*:.+$", re.M | re.S)
    desc, content = fetch_description(formfile)
    if(acceptpattern.match(desc) == None):
        sys.exit(promptmessage)   

#Triggers
#   default_desc form-out change "{PYTHON_HOME}/python.exe {SCRIPT_HOME}/p4comment.py %formfile% %formtype%"
#   check_desc form-out change "{PYTHON_HOME}/python.exe {SCRIPT_HOME}/p4comment.py %formfile%



if(__name__ == "__main__"):
    if(len(sys.argv) == 3):
        #this is trigger form-out.
        default_description(sys.argv[1])
    elif(len(sys.argv) == 2):
        #this is trigger form-in.
        check_description(sys.argv[1])

