class Properties:
	fileName = ''

	def __init__(self, fileName):
		self.fileName = fileName
	def getProperties(self):
		try:
			pro_file = open(self.fileName, 'r')
			properties = {}
			for line in pro_file:
				if line.find('=') > 0:
					str = line.replace('\n', '').split('=')
					properties[str[0]] = str[1]
		expect Exception, e:
			raise e
		else:
			pro_file.close()
		return properties
