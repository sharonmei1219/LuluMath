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



def formatProblem(problem, tag, number, chapterName):
	tags = {'兴趣篇': 'A',
			'拓展篇': 'B',
			'超越篇': 'C'}
	patternPre = '<div class="problem problem" id="gaosidaoyin.{chapterName}.{tagRank}{number}">\n\
	<h4 class="sequence">{tag} {number}</h4>\n'
	patterProblem = '\t<p class="description">{problem}</p>\n'
	patternPost = '</div>'

	output = patternPre.format(tag=tag, number=number, tagRank=tags[tag], chapterName=chapterName.replace('/','.'))
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
		if tag not in categories: break
		problemCount = 0
		problems = re.split('^[0-9]*\. *|^[0-9]*．', categories[tag], flags=re.MULTILINE)
		for problem in problems:
			if problem != '':
				outputStrs.append(formatProblem(problem, tag, problemCount, chapterFileName[:-4]))
			problemCount += 1
	# return outputStrs.join('\n')
	return '<div class="problem-set">\n' + '\n'.join(outputStrs) + '\n</div>'

# print splitCh('sharon/ch1.txt')