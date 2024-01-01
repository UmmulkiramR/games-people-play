import random
import re
import hangman_art
import hangman_dictionary
import os


print(hangman_art.logo)
print(hangman_art.hangman_start)


# G A M E S
# 0 1 2 3 4
word_chosen = str(random.choice(hangman_dictionary.word_list))


# def create_blank_word(word_chosen):
#     for i in range(0, len(word_chosen)):
#         word = word[:i]+'_'+word[i+1:]  #colon after 'i' returns the word inclusive of the letter at 'i'. Hence add 1 to ignore the letter at 'i'
#     return word

def create_blank_word(word_chosen):
    word = ''
    for i in range(0, len(word_chosen)):
        word = word + '_'
    return word


def replace_word_with_letter(letter, word, word_chosen):
    for i in re.finditer(letter, word_chosen): #finditer returns all the indices of letter in word_chosen
        word = word[:(i.start())] + letter + word[(i.start() + 1):]
    return word


def complete_hangman_figure(index, list_all_hangman):
    return list_all_hangman[index]


def play_the_game(word_chosen):
    word = create_blank_word(word_chosen)
    hangman_index = 0;
    hangman = ""
    while not hangman.__eq__(hangman_art.hangman_orig) and not word.__eq__(word_chosen):
        #os.system('clear')
        print(hangman)
        print(word)
        letter = input("guess a letter - ")
        if(not letter):
            continue
        if word_chosen.__contains__(letter):
            word = replace_word_with_letter(letter, word, word_chosen)
            if(word.__eq__(word_chosen)):
                print(word)
                print("YOU WIN!")
        else:
            hangman = complete_hangman_figure(hangman_index, hangman_art.list_all_hangman)
            hangman_index += 1
            if hangman.__eq__(hangman_art.hangman_orig):
                print(hangman)
                print("YOU KILLED HIM!")


play_the_game(word_chosen)


# while(not word.__eq__(word_chosen)):
#     letter = input("guess a letter - ")
#     if(word_chosen.__contains__(letter)):
#         word=replace_word_with_letter(letter,word,word_chosen)
#         print(word)
#     else:
#         hangman.replace('0',24)
#         print(hangman)


# name="ummulkiram"
# namex="____lkiram"
# for i in re.finditer("m",name):
#     #indice=[i.start()]
#     namex=namex[:(i.start())]+'m'+namex[(i.start()+1):]
# print(namex)



