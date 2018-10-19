#!/usr/bin/python
# -*- coding: UTF-8 -*-
import argparse
from splitFile import splitFile
from splitCh import splitCh

parser = argparse.ArgumentParser()
parser.add_argument('bookName', metavar='bookName', help='origin book in text format')
parser.add_argument('--to', metavar='to directory', default='./', help='where generated html locate')
args = parser.parse_args()

bookName = args.bookName
toDir = args.to


chapters = splitFile(bookName, toDir)

for chapter in chapters:
	with open(chapter.replace('.txt', '.html'), 'w') as output:
		output.write(splitCh(chapter))
