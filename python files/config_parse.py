from configparser import ConfigParser
def getdbDict(file = "config.ini" , section = "mysql"):
	dbDict = {}
	parser = ConfigParser()
	parser.read(file)

	if parser.has_section(section):
		items = parser.items(section)
		for item in items:
			print(item)
			dbDict[item[0]] = item[1]
	print(dbDict)
getdbDict()