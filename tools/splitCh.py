#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re

def showOutput(output):
	print('\n-----------' + '兴趣篇' + '================ \n')
	print(output['兴趣篇'])
	print('\n-----------' + '拓展篇' + '================ \n')
	print(output['拓展篇'])
	print('\n-----------' + '超越篇' + '================ \n')
	print(output['超越篇'])

def splitChapterInCatagory(chapter):
	tag = 'init'
	output = {}
	with open(chapter) as fs:
		line = fs.readline()
		while line != '':
			line = fs.readline()
			match = re.search(r"(?P<tag>兴趣篇|拓展篇|超越篇)", line)
			if match:
				tag = match.group('tag')
				output[tag] = ''
			else:
				if tag != 'init':
					output[tag] = output[tag]+ line
	return output


def formatProblem(problem, tag, number):
	patternPre = '<div class="problem problem-min-margin" id="gaosidaoyin.grade3.ch1.A2">\n\
	<h4 class="sequence">{tag} {number}</h4>\n'
	patterProblem = '\t<p class="description">{problem}</p>\n'
	patternPost = '</div>'

	output = patternPre.format(tag=tag, number=number)
	for line in re.split('\n', problem):
		if len(line.strip()) != 0:
			output = output + patterProblem.format(problem=line)
	output = output + patternPost
	return output


def splitCh(chapterFileName):
	output = splitChapterInCatagory(chapterFileName)
	tags = ['兴趣篇','拓展篇','超越篇']

	for tag in tags:
		problemCount = 0
		problems = re.split('^[0-9]*\. ', output[tag], flags=re.MULTILINE)
		for problem in problems:
			problemCount += 1
			print formatProblem(problem, tag, problemCount)	

# splitCh('ch1.txt')