#!/usr/bin/python
# -*- coding: UTF-8 -*-
import argparse
from splitFile import splitFile
from splitCh import splitCh 

parser = argparse.ArgumentParser()
parser.add_argument('bookName', metavar='bookName', help='origin book in text format')
parser.add_argument('--to', metavar='to directory', help='where generated html locate')
args = parser.parse_args()









print args.bookName
print args.to