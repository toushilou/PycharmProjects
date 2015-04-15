import json
import sys
import requests
url = "http://hqd-cassandra-01.mypna.com:8080/logshedcollector/api/logs/upload/JSON/tweets"
# assuming tweets is a collection of json tweets
tweets = {'b':789,'c':456}
headers = {'content-type': 'application/json'}
r = requests.post(url, data=tweets, headers=headers)
