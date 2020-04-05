import webbrowser
message = """<<html><head>
</head><body><p>Hello world</p></body>
</html>"""
f = open('helloworld.html', 'w')
f.write(message)
f.close()
webbrowser.open("file:///home/mohdfaizan/.config/spyder-py3/helloworld.html")
