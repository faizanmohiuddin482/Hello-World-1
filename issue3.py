import ConfigParser
configParser = ConfigParser.RawConfigParser()
configFilePath = "/home/mohdfaizan/github_repositories/config/check.conf"
configParser.read(configFilePath)
num = configParser.get('userinput-config', 'num')
for i in range(0, int(num)):
	print("hello world")
	
