#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re

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
	categories = splitChapterInCatagory(chapterFileName)
	tags = ['兴趣篇','拓展篇','超越篇']
	outputStrs = []

	for tag in tags:
		problemCount = 0
		problems = re.split('^[0-9]*\. ', categories[tag], flags=re.MULTILINE)
		for problem in problems:
			problemCount += 1
			outputStrs.append(formatProblem(problem, tag, problemCount))
			# print formatProblem(problem, tag, problemCount)	
	return outputStrs

# print splitCh('ch1.txt')