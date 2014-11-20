import re
import math
import pickle
<<<<<<< HEAD
<<<<<<< HEAD
from WriteLetters import *
=======
#from WriteLetters import *
>>>>>>> 4a5f9ec71f1b4aa82063b7c2a8f83fbbfcc12426
=======
>>>>>>> parent of d77e6ca... Imported WriteLetters to SynonymFind

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
	
	if word1 in wordList and word2 in wordList:
		l1 = len(wordList[word1])
		l2 = len(wordList[word2])
		
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
		total = -1
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
	words = sentence.split()
	
	for w in range(len(words)):
		# Remove non-alphabetic characters, all to lower case
		words[w] = words[w].lower()
		words[w] = re.sub(r'[^a-z-]+', '', words[w])

		addWordToList(words[w])
	
	for w in words:
		for x in words:
			addOccurence(x, w)
			
def main():
	global wordList
	
<<<<<<< HEAD
<<<<<<< HEAD
	print "Pickles ready to eat"
=======
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
>>>>>>> 4a5f9ec71f1b4aa82063b7c2a8f83fbbfcc12426
=======
	wordList = pickle.load(open("wordList2.p", "rb"))
	print "Loaded"
>>>>>>> parent of d77e6ca... Imported WriteLetters to SynonymFind
	
	#Print the list
	'''for x in wordList:
		print (x)
		print wordList[x]'''
	
	while True:
		input1 = raw_input()
<<<<<<< HEAD
		choices = findMostSimilar(input1)
		print choices
<<<<<<< HEAD
		drawWord(choices[0][0])#Just use the first entry

=======
		#drawWord(choices[0])
>>>>>>> 4a5f9ec71f1b4aa82063b7c2a8f83fbbfcc12426
=======
		input2 = raw_input()
		
		print checkSimilarity(input1, input2)
>>>>>>> parent of d77e6ca... Imported WriteLetters to SynonymFind
		
def reload():
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
	
	print 'Done loading'
	
	#Save the structure
	pickle.dump(wordList, open( "wordList2.p", "wb" ))
	
	print 'Saved and reloaded'
			
main()
raw_input()