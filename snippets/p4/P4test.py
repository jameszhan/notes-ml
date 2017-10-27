import P4
import sys

print(P4.P4.identify());

cl = sys.argv[1]
user = sys.argv[2]
desc = sys.argv[3]

f = open("d:/p4test.txt", 'a')
f.write("Hello World! ");
f.write("cl=")
f.write(cl)
f.write(",user=")
f.write(user)
f.write(",desc=")
f.write(desc)
f.write("\n");