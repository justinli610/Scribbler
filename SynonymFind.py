import re
import math
import pickle
#from WriteLetters import *

wordList = {} #Maps words to a frequency dictionary
# e.g. {'person' (word in list) : {'man' : 1 (word in sentence), 'woman' : 2}}

# New word encountered; put it into wordList
def addWordToList(word):
	global wordList
	
	if not(word in wordList):
		wordList[word] = {}

# New word encountered in the same sentence as wordInList; increment the counter
# Will not add a word to its own list
def addOccurence(wordInSentence, wordInList):
	global wordList
	
	if wordInSentence != wordInList:
		if not(wordInSentence in wordList[wordInList]):
			wordList[wordInList][wordInSentence] = 1
		elif wordInSentence:
			wordList[wordInList][wordInSentence] += 1
	
# Return the number of similar words in this
def checkSimilarity(word1, word2):
	global wordList
	total = 0
	
	#print (word1, word2)
	
	if wordList[word1] and wordList[word2] and word1 != word2:
		for w in wordList[word1]:
			if w in wordList[word2]:
				total += min(wordList[word1][w], wordList[word2][w])
				
		total = float(total)
		total /= getMagnitude(word1)
		total /= getMagnitude(word2)
	
		if total >= 1:
			total = 0
		else:
			total = math.acos(total) * 180 / math.pi
	else:
		total = 90
	return total
	
# Returns the number of other words that have appeared with this one
def getMagnitude(wordInList):
	total = 0
	global wordList
	
	for w in wordList[wordInList]:
		total += math.pow(wordList[wordInList][w], 2)
			
	return math.sqrt(total)

# Formats a sentence and updates the wordList with the new information	
def processSentence(sentence):
	# Remove non-alphabetic characters, all to lower case
	sentence = re.sub(r'--', ' ', sentence)
	sentence = sentence.lower()
	sentence = re.sub(r'[^\sa-z-]+', '', sentence)
	words = sentence.split()
	
	for w in words:
		addWordToList(w)
		for x in words:
			addOccurence(x, w)
			
def findMostSimilar(word):
	w1, w2, w3 = None, None, None
	p1, p2, p3 = 90, 90, 90
	
	if word in wordList:
		for w in wordList:
			similarity = checkSimilarity(word, w)
			
			if similarity < p3:
				if similarity < p2:
					if similarity < p1:
						w3 = w2
						w2 = w1
						w1 = w
						p3 = p2
						p2 = p1
						p1 = similarity
					else:
						w3 = w2
						w2 = w
						p3 = p2
						p2 = similarity
				else:
					w3 = w
					p3 = similarity
					
	return ((w1, w2, w3), (p1, p2, p3))
			
def main():
	global wordList
	
	wordList = pickle.load(open("wordList3.p", "rb"))
	
	'''for w in wordList:
		if wordList[w]:
			del wordList[w]
			count += 1'''
			
	del wordList['a']
	del wordList['the']
	del wordList['of']
	del wordList['weve']
	del wordList['anyway']
	del wordList['shes']
	del wordList['hers']
	del wordList['hed']
	del wordList['hes']
	del wordList['his']
	del wordList['him']
	del wordList['theyve']
	del wordList['they']
	del wordList['theyre']
	del wordList['i']
	del wordList['im']
	del wordList['id']
	del wordList['ive']
	del wordList['me']
	del wordList['my']
	del wordList['you']
	del wordList['your']
	del wordList['youre']
	del wordList['yours']
	del wordList['youve']
	del wordList['eh']
	del wordList['hm']
	del wordList['stiva']
	del wordList['dounias']
	del wordList['rodya']
	del wordList['properly']
	
	print "Loaded"
	
	#Print the list
	'''for x in wordList:
		print (x)
		print wordList[x]'''
	
	while True:
		input1 = raw_input()
		choices = findMostSimilar(input1)
		print choices
		#drawWord(choices[0])
		
def reload():
	global wordList
	
	file = open('a.txt', 'r')
	sentences = re.split('[,\?!;]', file.read())
	for s in sentences:
		processSentence(s)
		
	file = open('b.txt', 'r')
	sentences = re.split('[,\?!;]', file.read())
	for s in sentences:
		processSentence(s)
		
	file = open('c.txt', 'r')
	sentences = re.split('[,\?!;]', file.read())
	for s in sentences:
		processSentence(s)
		
	file = open('d.txt', 'r')
	sentences = re.split('[,\?!;]', file.read())
	for s in sentences:
		processSentence(s)
		
	file = open('e.txt', 'r')
	sentences = re.split('[,\?!;]', file.read())
	for s in sentences:
		processSentence(s)
	
	print 'Done loading'
	
	# Save the structure
	pickle.dump(wordList, open( "wordList.p", "wb" ))
	
	print 'Saved'
			
main()
raw_input()