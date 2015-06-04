#!/usr/bin/env python
#-*-coding:utf-8-*-
from __future__ import unicode_literals

import re
import sys
import json
import getopt
import requests

from termcolor import colored


key = "524951398"
keyfrom = "gavin-123"
url = "http://fanyi.youdao.com/openapi.do"

def get_response(words):
	try:
		response = requests.get(url + "?keyfrom=" + keyfrom + "&key=" + key + 
			"&type=data&doctype=json&version=1.1&q=" + words)
	except:
		print "哎哟,好像出错了"
		return
	return response

def show(response):
	json_data = json.loads(response.text)
	if json_data.has_key("basic"):
		print colored(json_data["query"],"green"),
		if json_data["basic"].has_key("phonetic"):
			print colored(json_data["basic"]["phonetic"],"green")
		print colored(",".join(json_data["basic"]["explains"]),"yellow")
		print ""
		print colored("网络释义","blue")
		for value in json_data["web"][0]["value"]:
			print colored(value,"cyan")
		print ""
		print colored("短语","blue")
		for phrase in json_data["web"][1:]:
			phrase["value"] = ",".join(phrase["value"])
			print colored(phrase["key"]+": ","yellow"),colored(phrase["value"],"cyan")
	else:
		print "然而并没有此单词"

def main():
	try:
		options, args = getopt.getopt(sys.argv[1:], ["help"])
	except getopt.GetoptError as e:
	    pass

	args = map(lambda x:x.decode("utf-8"),args)
	words = "".join(args)
	response = get_response(words)
	if not response:
		return
	show(response)


if __name__ == '__main__':
	main()




