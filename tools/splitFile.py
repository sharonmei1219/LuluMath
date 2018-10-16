#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re

def splitFile(fileName):

	chapterName = "initChapter.txt"
	chCount = 0
	with open(fileName, 'r')  as fs:
		while chapterName is not None:
			with open('ch' + str(chCount) + '.txt', 'w') as newChapter: 
				line = fs.readline()
				match = re.search(r"(?P<pre>.*?)(?P<chapterName>第[0-9]+讲)(?P<after>.*)", line)
				while line != '' and not match:
					newChapter.write(line)
					line = fs.readline()
					match = re.search(r"(?P<pre>.*?)(?P<chapterName>第[0-9]+讲)(?P<after>.*)", line)
				if line != '' and match:
					chapterName = match.group('chapterName') + '_' + match.group('after').lstrip().strip('\t') + '.txt'
					chCount += 1
				else:
					chapterName = None

splitFile('Gaosi.txt')

