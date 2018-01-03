#!/usr/bin/python
import os
import sys

for line in sys.stdin:
	#converts article to a list of the words in it (has duplicates)
	words = line.split()
	docId = words.pop(0)
	wordCount = {}
	#counts word freq within doc, eliminates dups
	for x in words:
		if x in wordCount:
			wordCount[x] += 1
		else:
			wordCount[x] = 1
	#prepares output for doc
	#key: docId value: word(i) \t current(nk) \t wordFreq(i)...n
	output = docId + '\t'
	for x in wordCount:
		output += x + '\t' + '1' + '\t' + str(wordCount[x]) + '\t'
	print output.rstrip()
