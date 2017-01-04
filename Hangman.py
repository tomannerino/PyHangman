import csv
import random

my_list = []
current_word = ""


def loadWordList(category):
    with open(category, "rb") as f:
        reader = csv.reader(f)
        temp_list = list(reader)
        return temp_list[0]


def checkForWinner():
    return


def checkForLetter(letter):
    return


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


def startHangman():
    global my_list
    global current_word
    my_list = loadWordList("library/animals.words")
    current_word = getCurrentWord()
    waitForUserInput()

startHangman()
