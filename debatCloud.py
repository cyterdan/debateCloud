#!/usr/bin/env python
# -*- coding: utf-8 -*-

###############################################################################
###
### @Author : cyterdan
###
### This script generates a word cloud for both opponents in the 
### french election debate opposing Emmanuel Macron and Marine Le-Pen 
###
###
###############################################################################

#external dependencies
import numpy as np
from PIL import Image
from wordcloud import WordCloud

#internal dependencies
from debateCloudUtils import stopWordLoader,xmlTranscriptLoader

#load stop words
stopWords = stopWordLoader.loadStopWords('stopwords')

#load the content from the debate transcript
wordsBySpeaker = xmlTranscriptLoader.loadWordsFromTranscript("transcript.xml",stopWords)


def generateWordCloud(words,output,maskfile=None) : 
	""" 
	generate a word cloud from a text
	
	inputs :
		words(required) : long string containing the words
		output(required) : output image path
		maskfile(optional) : generate in the form of an image (see wordcloud doc for image specifications)

	"""
	mask = None
	if maskfile : 
		mask = np.array(Image.open(maskfile))
	wc = WordCloud(mask=mask).generate(words)
	wc.to_file(output)
	print("generated "+output)

generateWordCloud(wordsBySpeaker["EMacron"],"em-cloud.png","masks/EM-mask.png")
generateWordCloud(wordsBySpeaker["MLe Pen"],"mlp-cloud.png","masks/MLP-mask.png")
