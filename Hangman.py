import csv
import random

my_list = []
current_word = ""
correct_letters = []

def loadWordList(category):
    with open(category, "rb") as f:
        reader = csv.reader(f)
        temp_list = list(reader)
        return temp_list[0]


def checkForWinner():
    return


def checkForLetter(letter):
    if current_word.count(letter) == 0:
        print ""
        print "The letter " + letter + " was not found.  Try Again!"
        print ""
    else:
        correct_letters.append(letter)

    generateWordUI()


def getCurrentWord():
    array_count = len(my_list)
    random_num = random.randrange(0, array_count)
    return my_list[random_num]


def waitForUserInput():
    answer = raw_input("Select a letter:  ")
    if len(answer) > 1:
        print "You must select only one letter."
        waitForUserInput()
    if not answer.isalpha():
        print "You must enter only letters."
        waitForUserInput()
    checkForLetter(answer)


def generateWordUI():
    wordUI = ""
    print ""
    print "Your Hangman Word Is Below.  Can You Guess The Word?"
    print ""
    wordLen = len(current_word)
    for w in current_word:
        if correct_letters.count(w) > 0:
            wordUI = wordUI + w.upper() + " "
        else:
            wordUI = wordUI + "_" + " "
    print wordUI
    print ""
    if wordUI.count("_") == 0:
        print ""
        print "Congratulations!  You Solved The Word!"
        print ""
        resetHangman()
    waitForUserInput()


def resetHangman():
    del correct_letters[:]
    del my_list[:]
    startHangman()


def startHangman():
    global my_list
    global current_word
    my_list = loadWordList("library/misc.words")
    current_word = getCurrentWord()
    generateWordUI()

startHangman()
