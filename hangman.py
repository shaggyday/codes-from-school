#Harry Tian and Star Song
#Hangman: player 1 input a word to be guessed. Player will input a letter each time to check whether it is in the input word. If not, player 1 inputs another letter. Those letters that have been guessed will be showed.
#Once the player finished the game, he will be asked whether they want to play again or not. If he says yes then the game restart,or his total times of winning and losing will be showed as he quit. 

#To define main() program
def main():
    launch_game = True
    win_times=int(0)
    lose_times = int(0)
    while launch_game == True:
#initial input
        phrase = str(input("please enter the phrase to be guessed:"))
        requirements = str("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz- ' ")
#To fit the input requirement
        valid = False
        while valid is False: 
            for words in phrase:
                if words not in requirements:
                    print("The phases is invalid, please create a new phase.")
                    phrase = str(input("please enter the phrase to be guessed:"))
                else:
                    valid = True
                    break
    #To create _ _ _ _blanks            
        alphabet = str('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
        word = phrase
        printword = str()
        for a in word:
            if a in alphabet:
                printword += "_ "
            else:
                printword += a
        shift = False
    #Start the game loop
        num_wrong_guess = int(0)
        lettersguessed = str()
        while shift is False:
            for a in word:
                word_guess = False
                print()
                print(printword)
                print()
    #Test if game is finished and won
                if "_" not in printword:
                    shift = True
                    win_times += 1
                    print()
                    print("Good Game! you won!")
                    break
    #Start the guess
                space = " "
                index = int(0)
                print("letters guessed so far:",lettersguessed)
                print("num guesses remaining:",int(6-num_wrong_guess))
                print()
                letter = str(input("enter the letter you wish to guess:"))
    #Repeated guess
                if letter.upper() in lettersguessed or letter.lower() in lettersguessed:
                    print()
                    print("***you already guessed that letter, please try again")
                    break
    #Guessed right,replace the _ with word
                for b in word:
                    if letter.lower() == b and letter not in lettersguessed:
                        printword = printword[:index:]+letter.lower()+printword[index+1::]
                        word_guess = True
                    elif letter.upper() == b  and letter not in lettersguessed:
                        printword = printword[:index:]+letter.upper()+printword[index+1::]
                        word_guess = True
                    if b == space:
                        index += 1
                    else:
                        index += 2
    #To show the plaword_guesser their guess is right
                if word_guess == True:
                    print()
                    print("Good Guess!")
    #To show the plaword_guesser their guess is wrong
                if word_guess == False and letter not in lettersguessed:
                    num_wrong_guess += 1
                    print()
                    print("Sorry, that letter is not in the phase:(")
    #To end game because of chances depleted
                if num_wrong_guess == 6:
                    shift = True
                    lose_times += 1
                    print()
                    print("Game Over")
                    break
    #To accumulate guessed word
                if letter.lower() not in lettersguessed and letter.upper() not in lettersguessed:
                    lettersguessed += letter

    
#To continue the game if the player want to or not
        print()
        q = str(input("Do you want to play again? 'Y' for yes, 'N' for no."))
        if q == "N":
            launch_game == False
            print()
            print("Your wins:", win_times)
            print("Your loses:", lose_times)
            break
   
        
if __name__ == '__main__': 
    main()
