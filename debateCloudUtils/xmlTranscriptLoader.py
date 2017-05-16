#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
from bs4 import BeautifulSoup
import re



def replaceAll(original,removables) :
	"""
	replaces all instances of each string in the removable list in the original string 
	"""
	for target in removables :
 		original = original.replace(target,"")
	return original

def loadWordsFromTranscript(filename,stopWords) : 
	"""loads transcrit from xml file 
	and separate into different speakers 
	(expected format is timed texted format https://www.w3.org/ns/ttml/)

        Returns
        -------
        wordsBySpeaker : dict (string, string)
            words for each speaker.
	"""

	#characters in this string will be removed from content	
	removables = [":","-",".",","]
	
	currentSpeaker = None

	stopWordsSet = set(stopWords)

	wordsBySpeaker = {}
	#using codecs.open (https://github.com/amueller/word_cloud/issues/148)
	with codecs.open(filename,encoding='utf-8') as debatFile :
		soup = BeautifulSoup(debatFile.read(),"lxml")
		for span in  soup.findAll('span') :
			color = span['tts:color'] 
			# actual speech has color == 'white'
			if color == 'white':
				text = span.text
				speakerMatch = re.search('\-[A-Z]\.[A-Z a-z\-]+:',text)
				if speakerMatch: 
					#clean the speaker's name
					currentSpeaker = replaceAll(speakerMatch.group(0),removables).strip()
				if currentSpeaker : 
					if currentSpeaker not in wordsBySpeaker : 
						wordsBySpeaker[currentSpeaker] = []
					#clean the content
					words = replaceAll(text,removables).replace(currentSpeaker,'').strip()
					#remove stop words					
					for word in words.split(" ") :
						if (word.strip().lower().encode('utf-8')) not in stopWordsSet :
							wordsBySpeaker[currentSpeaker].append(word)


	#join words to make a long text
	for speaker in wordsBySpeaker : 
		wordsBySpeaker[speaker] = " ".join(wordsBySpeaker[speaker])

	return wordsBySpeaker

