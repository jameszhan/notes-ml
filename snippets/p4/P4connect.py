from P4 import P4, P4Exception

p4 = P4();
p4.port = "1666"
p4.user = "james"
p4.client = "james"

try:
	p4.connect()
	print('version', p4.version)
	print('api_level', p4.api_level)
	print('charset', p4.charset)
	print('client', p4.client)
	print('cwd', p4.cwd)
	print('exception_level', p4.exception_level)
	print('host', p4.host)
	print('input', p4.input)
	print('maxlocktime', p4.maxlocktime)
	print('maxresults', p4.maxresults)
	print('maxscanrows', p4.maxscanrows)
	print('messages', p4.messages)
	print('p4config_file', p4.p4config_file)
	print('password', p4.password)
	print('port', p4.port)
	print('prog', p4.prog)
	print('server_case_insensitive', p4.server_case_insensitive)
	print('server_level', p4.server_level)
	print('server_unicode', p4.server_unicode)
	print('tagged', p4.tagged)
	print('track', p4.track)
	print('track_output', p4.track_output)
	print('ticket_file', p4.ticket_file)
	print('user', p4.user)
        print('version', p4.version)
	print('warnings', p4.warnings)

	print('connected()', p4.connected())
	print('identify()', p4.identify())

        print("----------run_info--------------")
        p4.track = 1
	p4.run_info()
	print(p4.track_output)
        print("----------run_info--------------")
        
	info = p4.run("info")
	
	for i in info:
		for key in i:
			print(key, "=", i[key])
	p4.run("edit", "file.txt")	
except P4Exception:
	print("Errors: ", p4.errors)
	for e in p4.errors:
		print(e)
finally:
        p4.disconnect()
		
