# parsing file for config --> dict
from configparser import ConfigParser

def retDict(filename = "configKp.ini" , section = "abcd"):
	dbDict = {}
	parser = ConfigParser()
	# print(parser)
	# print(dir(parser))
	# reading the config file 
	file = parser.read(filename)
	# checking the section 
	if parser.has_section(section):
	# extracting the section items 
		items = parser.items(section)
		for item in items:
			# print(item)
			dbDict[item[0]] = item[1]
	# print(dbDict)
	return dbDict

# retDict()