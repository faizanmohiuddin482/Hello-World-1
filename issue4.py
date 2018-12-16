 f = open('helloworld.html', 'w' )

message = """<html><head>
</head><body><p>Hello world</p></body>
</html>"""
f.write(message)
f.close()
