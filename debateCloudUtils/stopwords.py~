#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sets import Set
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
	
	with codecs.open(filename,encoding='utf-8') as fileHandle:
		for line in fileHandle.readlines() : 
			lines.append(unicode(line))
	

	return Set(lines)

