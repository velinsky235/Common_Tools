from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan
import json


ELASTICSEARCH_URL = 'some_url'

with open("config.json") as ifh:
	config = json.load(ifh)


es = Elasitcsearch(
		ELASTICSEARCH_URL,
		timeout=120,
		use_ssl=True,
		maxsize=10+2,
		http_auth=(config["user"], config["password"])
	)


def query(term, field, file_id):
	for result in scan(
		client=es,
		size=500,
		query={
			"query": {
				"bool": {
					"must":[
						{"match": {field:term}},
						{"match": {"file_id":file_id}}
					]
				}	
			}
		}, index='some_index', doc_type="_doc"
		): info = [result["some_field"].get("another_field", "")]
		yield ",".join(info)


def main():
	for rv in query(term, field, file_id):
		print(rv)