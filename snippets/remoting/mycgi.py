import cgitb
cgitb.enable()

print("Content-Type: text/html")
print()

print('<html>')
print('<head>')
print('<title>CGI script output</title>')
print('</head>')
print('<body>')
print('<h1>This is my first CGI script.</h1>')
print('Hello World!')
print('</body>')
print('</html>')
