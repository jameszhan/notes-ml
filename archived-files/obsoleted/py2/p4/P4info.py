from P4 import P4, P4Exception

p4 = P4();
#p4.port = "1666"
#p4.user = "james"
#p4.client = "james"

print(p4.env('P4PORT'))
print(p4.env('P4CONFIG'))
print(p4.env('P4CLIENT'))
print(p4.env('P4USER'))

print(p4.user)
print(p4.port)
print(p4.p4config_file)

def getDescription(id):
    p4 = P4()
    try:
        p4.connect()
        cl = p4.fetch_change(id)
        return cl['Description']
    except P4Exception, ex:
        print(ex)
    finally:
        p4.disconnect()

print(getDescription('20'))


p4.connect()
print("\n-----------------------change------------------------------")
change = p4.fetch_change(20)
print(change)

print("\n-----------------------label owner------------------------------")
label = p4.fetch_label('Owner')
print(label)

print("\n-----------------------label description------------------------------")
label = p4.fetch_label('description')
print(label)

print("\n-----------------------label revision------------------------------")
label = p4.fetch_label('revision')
print(label)

print("\n-----------------------label View------------------------------")
label = p4.fetch_label('view')
print(label)

print("\n-----------------------label Update------------------------------")
label = p4.fetch_label('Update')
print(label)

print("\n-----------------------client------------------------------")
clientspec = p4.fetch_client("james")
print(clientspec)
