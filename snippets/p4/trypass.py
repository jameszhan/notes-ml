import urllib.request
import urllib.parse

#req = urllib.request.Request('http://www.163.com/')
#req.add_header('Referer', 'http://www.python.org/')

#params = urllib.parse.urlencode({'wd': '诗经'})

#f = urllib.request.urlopen(req, params)
#result = f.read(8000).decode('utf-8')

opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent','Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0;)')]

print(opener)

params = urllib.parse.urlencode({'wd': '诗经'})
response = opener.open('http://www.baidu.com/', None)

#params = urllib.parse.urlencode({'wd': '诗经'})

#f = urllib.request.urlopen(req, params)

#result = f.read(8000).decode('utf-8')

print(response.read(8000).decode('gb2312'))
