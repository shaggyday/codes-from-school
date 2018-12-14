import random
import sys
#1. Connection Data
def dictionary(corpus):
    '''build a dictionary containing an entry for each unique word in the text'''
    data = {}
    # find every unique word in the text and create dictionary key and value
    for item in corpus:
        if item not in data:
            data[item] = []
    # variables for future use
    wordIndex = 0
    # for every word that follows a key word, append it to dictionary value
    for word in corpus:
        wordIndex += 1
        nextWord = corpus[wordIndex]
        data[word].append(nextWord)
        if wordIndex == len(corpus) - 1:
            break
    return data
def startWords(corpus):
    ''' build a list of all unique words that start a sentence'''
    # finding every item in the file text with a period and add
    # the next word into a list
    wordIndex = 0
    startWords = []
    for word in corpus:
        wordIndex += 1
        nextWord = corpus[wordIndex]
        if nextWord not in startWords:
            if "." in word or "?" in word or "!" in word:
                if len(nextWord) == 1:
                    if nextWord[0].isupper():
                        startWords.append(nextWord)
                else:
                    if nextWord[0].isupper() or nextWord[1].isupper():
                        startWords.append(nextWord)
        if wordIndex == len(corpus) - 1:
            break
    startWords.append(corpus[0])
    return startWords
#2. Generating Sentences
def ranSen(corpus):
    '''select a random word from the start word list and add it to the sentence
    as the first word'''
    firstWord = random.choice(startWords(corpus))
    # find the dictionary entry that has this first word as the key,
    # and choose a random word from that value - list of words
    wordBank = dictionary(corpus)
    wordList = [firstWord]
    # while loop to create a list end if: the added word has . or ? or !
    # or if: the sentences reaches 50 words in length
    for i in range(49):
        lastWord = wordList[i]
        ranWord = random.choice(wordBank[lastWord])
        wordList.append(ranWord)
        if "." in ranWord or "?" in ranWord or "!" in ranWord:
            if i > 2:
                break
    # translate the list of words into a sentence
    sentence = ""
    for word in wordList:
        sentence += word + " "
    return sentence
#Final Program:    
def main():
    valid = "c"
    while valid == "c":
        # use commandline to open the given file and read the text
        File = open(sys.argv[1],"r")
        corpus = File.read()
        corpus.strip()
        # split the text so that every word is an individual item in a list
        corpus = corpus.split()
        print(ranSen(corpus))
        #continually ask the user to enter “c” to continue or “q” to quit
        #If they choose “c”, output another sentence using a new random start word
        valid = input('enter "c" to continue output another random sentence, or enter "q" to quit:')       
main()
#55 lines excluding comments

    
