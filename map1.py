#!/usr/bin/python
import os
import sys
import re
import string

stopWordFile = open('mapreduce/stop_words.txt', 'r')
stopWordList = {}

#reads in all the stop words, removes non alpha num chars
alphnum = re.compile('^[a-zA-Z0-9]')
for word in stopWordFile:
	temp = word.rstrip()
	tempTwo = ""
	for y in temp:
		if re.match('^[\w_]', y):
			tempTwo += y
	stopWordList[tempTwo] = 1
for line in sys.stdin:
	docId = line.rstrip()
	docName = next(sys.stdin)
	data = next(sys.stdin)
	printList = docId + '\t'
	#removes stop words, to lower
	#removes strings with non alphanum chars
	data = data.lower()
	wordList = data.split()
	for x in wordList:
		temp = x
		tempTwo = ""
		for y in temp:
			if re.match('^[\w_]', y):
				tempTwo += y
		temp = tempTwo
		if temp != "":
			if temp not in stopWordList:
				printList += temp + '\t'
	print(printList)
