import sys
import os

class Properties:
	fileName = ''

	def __init__(self, fileName):
		self.fileName = fileName
	def get(self, key):
		try:
			pro_file = open(self.fileName, 'r')
			properties = {}
			for line in pro_file:
				if line.find('=') > 0:
					str = line.replace('\n', '').split('=')
					properties[str[0]] = str[1]
		except Exception, e:
			raise e
		else:
			pro_file.close()
		return properties[key]


if __name__ == '__main__':
	path = sys.path[0] + os.sep + "test.properties"
	print path
	p = Properties(path)
	name = p.get('name')
	if name == 'yuanquan':
		print 'Yes'
	else:
		print 'No'