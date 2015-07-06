import pymongo
import random

if __name__ == '__main__':
	conn = pymongo.Connection("127.0.0.1", 27017)
	db = conn.mydb
	data = db.testData.find()
	for i in data:
		print i
	conn.close()
