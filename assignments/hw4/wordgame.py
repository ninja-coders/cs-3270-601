'''
Robert Robinson
CS3270_002
project_4
due: 16 Mar 2018
'''



from itertools import permutations, groupby
from random import *
import sys
import re
import math

# Seed for the random function
if __name__ =="__main__":
    if len(sys.argv)>1:
        seeds = int(sys.argv[1])
    else:
        seeds = None
    seed(seeds)

def main():
    # reads from a file obj
    file = open("words.txt","r")
    # read in all words and strips out the white space for every line in file
    AllWords = list(line.strip() for line in file)  # strip out the \n new line chars and make a list of all words in  the file
    file.close()

    print("Welcome to my Guessing Game")
    print("Please enter a 'lo' and a 'hi' separated by a space")
    print("Enter 'q' to quit")

# the Outer game flag the the 'will begin agian' loop
    beginAgain = True
    while (beginAgain):

        rangeFlag = True
        while (rangeFlag):
            try:
                lo, hi = input("Please give a lo and a hi: ").split()
                lo = int(lo)
                hi = int(hi)
                rangeFlag = False
            except ValueError:
                print("invalid range, try again.")


        # choice() pulls a random word from the list of AllWords read from the file
        someWord = choice(AllWords)
        print(someWord)
        print()

        # used the sample funtion to pull one letter at a time without repeats for the lenths of the word and join it to an empty string. in the the words letters are shuffled and rejoined into one string of the same length as the original word
        scrambledWord = ''.join(sample(someWord, len(someWord)))
        print("Your scrambled word is:  ", scrambledWord)

        print("please be patient, this could take several minutes, if the word is long...")
        possible_words = list(set([words for words in ["".join(p) for i in range(1, len(someWord)+1) for p in permutations(someWord, i)] if len(words) >= 2 and words in AllWords]))
        possible_words.sort() # sort first alphabetically
        possible_words.sort(key=len) # next resort by length
        print()
        print()

        # C style code that works to get me lists to work with
        li1 = []
        li2 = []
        for word_length in range(lo, (hi + 1)):
            temp = list()
            tempGuess = list()
            for word in possible_words: ### --> --> -->
                if word_length == len(word):
                    temp.append(word)
                    tempGuess.append("_ " * len(word))
                    temp.sort()
            li1.append(temp)
            li2.append(tempGuess)
        # a new list of just the proper range of entries so as to later compare as a value
        li3 = []
        for i in li1:
            for j in i:
                li3.append(j)
        print(li3)

    # Inner Game loop to play once until all guesses have been  made
        while(len(li3)):
            userGuess = input("Enter a guess: ")
            if userGuess in li3: ### --> --> -->
                ind = li1[len(userGuess) - lo].index(userGuess)
                li2[len(userGuess) - lo][ind]= userGuess  # li2[len(userGuess) - lo].__setitem__(ind, userGuess)
                li3.remove(userGuess)
                #print(li3)
                print("Correct!")
                print(li2)
            elif userGuess == "q":
                break
            elif len(userGuess) > hi:
                print("incorrect word size")
                print("The guess does not fit within the range of (low, high)")
                continue
            else: # (userGuess not in possible_words)
                print("guess again...")

        if not len(li3):
            print("Congrats on winning!")
            y = input("Play again? press y: ")
            beginAgain = True if y == 'y' else False
main()