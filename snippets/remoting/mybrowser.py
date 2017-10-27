import webbrowser

url = 'http://www.python.org/'

# Open URL in a new tab, if a browser window is already open.
webbrowser.open_new_tab(url + 'doc/')
webbrowser.open_new_tab('http://www.google.com/')
webbrowser.open_new_tab('http://news.google.com/')

# Open URL in new window, raising the window if possible.
webbrowser.open_new(url)
