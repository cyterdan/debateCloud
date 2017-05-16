#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
def loadStopWords(filename) :
	"""
		loads a Set of stopwords from a standard file
			
		input : 
			file path containing stop words (format expected is one word per line)
		return : 
			lines : a set of words	
	"""
	

	lines = []	
	
	with open(filename,"r") as fileHandle:
		for line in fileHandle.readlines() :
			lines.append(line.strip())
	

	return set(lines)

