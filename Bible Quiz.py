
#Created by Atonio Hiko on the 14th/March/2023.
#This quiz is based on the Bible. It consists of 10 questions, each question having four options and only one correct answer.


# This is a function called check(). It requires 2 arguments. One list and one user input. It returns True if the user input is in the list. It returns False if the user input is not in the list.
def check(options, user_input):
    if user_input in options:
        return True
    else:
        return False


# The score variable will give a point/s to every question answered correctly, and at the end of the quiz it will add up your points to give your final score. 
# At the moment the score variable is set to 0 as the person engaging in the quiz has not answered any questions correctly yet.
score = 0

 
name = input("What is your name?\n\n")
print("Nice to meet you {}!\n".format(name))





# Options argument can store the answer in it. It doesnt necessarily hold's a single answer, because it can hold multiple variations of an answer and can also hold different answers. 

# But I will be using the options variable for one right answer and multiple variations of this right answer if necessary. 

# The reason being because the person playing this quiz may put in the right answer but maybe with all caps or all lowercase.
options = ["yes", "a", "b", "Yes", "Yes please".lower()]
want_to_play = input("Would you like to play? \na) Yes\nb) Yes please\n\n")


if check(options, want_to_play):
    print("\nGood luck man\n")
else:
    print("\nYour playing anyways\n") 


 
# The first question of the bible quiz!
   

# We have used the input() function to take the input of the user 
# Also used the conditional statements (if, elif, and else) to check if the user's input is one of the choices. 
user_input = ''

# A while True loop was included in order to iterate until the user's input is the correct answer.
while True:
    user_input = input("Question 1).\nWhat is the first book of the bible?\na) Genesis \nb) Exodus \nc) Numbers \nd) Leviticus\n\n>> ")

    if user_input == 'a':
        print("Correct, Genesis is the right answer!\n")
        # The score += 1 adds one to the score variable.
        score += 1
        break                                                        
        # The break statement breaks out of the while True loop... 
    elif user_input == 'b':
        print("Nope, wrong answer. Try again.\n")
        continue
        # ... As the continue statement continues the loop until the correct answer is entered.
    elif user_input == 'c':
        print("Nope, wrong answer. Try again.\n")
        continue
    elif user_input == 'd':
        print("Nope, wrong answer. Try again.\n")
        continue
    else:
        print("To choose your answer, please type either a, b, c or d (not in capitals, just lowercase).\n")
        continue




# The second question of the bible quiz!
   

# We have used the input() function to take the input of the user 
# and also used the conditional statements (if, elif, and else) to check if the user's input is one of the choices. 
user_input = ''

# A while True loop was included in order to iterate until the user's input is the correct answer.
while True:
    user_input = input("Question 2).\nWhere was Jesus Born?\na) Syria \nb) Egypt \nc) Canaan \nd) Bethelhem\n\n>> ")

    if user_input == 'a':
        print('Nope, wrong answer. Try again.\n')
        continue                                                        
    elif user_input == 'b':
        print("Nope, wrong answer. Try again.\n")
        continue
        # ... As the continue statement continues the loop until the correct answer is entered.
    elif user_input == 'c':
        print("Nope, wrong answer. Try again.\n")
        continue
    elif user_input == 'd':
        print("You got it right! Bethelhem is where Jesus Christ was born.\n")
        # The score += 1 adds one to the score variable.
        score += 1
        break
    # The break statement breaks out of the while True loop... 
    else:
        print("To choose your answer, please type either a, b, c or d (not in capitals, just lowercase).\n")
        continue




# The third question of the bible quiz!
   

# We have used the input() function to take the input of the user 
# and also used the conditional statements (if, elif, and else) to check if the user's input is one of the choices. 
user_input = ''

# A while True loop was included in order to iterate until the user's input is the correct answer.
while True:
    user_input = input("Question 3).\nHow many brothers did Joseph have?\na) 11 Brothers \nb) 9 Brothers \nc) 3 Brothers\nd) 13 Brothers\n\n>> ")

    if user_input == 'a':
        print("Good job! Joseph indeed had 11 Brothers.\n")
        # The score += 1 adds one to the score variable.
        score += 1
        break                                                        
        # The break statement breaks out of the while True loop... 
    elif user_input == 'b':
        print("Nope, wrong answer. Try again.\n")
        continue
        # ... As the continue statement continues the loop until the correct answer is entered.
    elif user_input == 'c':
        print("Nope, wrong answer. Try again.\n")
        continue
    elif user_input == 'd':
        print("Nope, wrong answer. Try again.\n")
        continue
    else:
        print("To choose your answer, please type either a, b, c or d (not in capitals, just lowercase).\n")
        continue




# The fourth question of the bible quiz!
   

# We have used the input() function to take the input of the user 
# and also used the conditional statements (if, elif, and else) to check if the user's input is one of the choices. 
user_input = ''

# A while True loop was included in order to iterate until the user's input is the correct answer.
while True:
    user_input = input("Question 4).\nHow many plagues did God send to Egype during Moses' time?\na) 7 \nb) 10 \nc) 23\nd) 9\n\n>> ")

    if user_input == 'a':
        print("Nope, wrong answer. Try again.\n")
        continue                                                        
    elif user_input == 'b':
        print("Great job. God sent 10 plagues onto Egypt because the Phaoroh of Moses' time was not willing to let God's people (which is Israel) go.\n")
        # The score += 1 adds one to the score variable.
        score += 1
        break
        # The break statement breaks out of the while True loop... 
    elif user_input == 'c':
        print("Nope, wrong answer. Try again.\n")
        continue
    # ... As the continue statement continues the loop until the correct answer is entered.
    elif user_input == 'd':
        print("Nope, wrong answer. Try again.\n")
        continue
    else:
        print("To choose your answer, please type either a, b, c or d (not in capitals, just lowercase).\n")
        continue




# The fifth question of the bible quiz!
   

# We have used the input() function to take the input of the user 
# and also used the conditional statements (if, elif, and else) to check if the user's input is one of the choices. 
user_input = ''

# A while True loop was included in order to iterate until the user's input is the correct answer.
while True:
    user_input = input("Question 5).\nWhat is the last book of the Bible?\na) John \nb) Genesis \nc) Revelation\nd) Daniel\n\n>> ")

    if user_input == 'a':
        print("Nope, wrong answer. Try again.\n")
        continue                                                        
    elif user_input == 'b':
        print("Nope, wrong answer. Try again.\n")
        continue
        # ... As the continue statement continues the loop until the correct answer is entered.
    elif user_input == 'c':
        print("Amazing work. Revelation is the last book of the Bible.\n")
        # The score += 1 adds one to the score variable.
        score += 1
        break
    # The break statement breaks out of the while True loop... 
    elif user_input == 'd':
        print("Nope, wrong answer. Try again.\n")
        continue
    else:
        print("To choose your answer, please type either a, b, c or d (not in capitals, just lowercase).\n")
        continue




# The sixth question of the bible quiz!
   

# We have used the input() function to take the input of the user 
# and also used the conditional statements (if, elif, and else) to check if the user's input is one of the choices. 
user_input = ''

# A while True loop was included in order to iterate until the user's input is the correct answer.
while True:
    user_input = input("Question 6).\nWhat is the 3rd commandment?\na) Do not use the Lord's name in vain\nb) Thou shall not have any gods before me\nc) You should not commit adultery\nd) Thou shall not kill\n\n>> ")

    if user_input == 'a':
        print("Correct.\n")
        # The score += 1 adds one to the score variable.
        score += 1
        break                                                        
        # The break statement breaks out of the while True loop... 
    elif user_input == 'b':
        print("Nope, wrong answer. Try again.\n")
        continue
        # ... As the continue statement continues the loop until the correct answer is entered.
    elif user_input == 'c':
        print("Nope, wrong answer. Try again.\n")
        continue
    elif user_input == 'd':
        print("Nope, wrong answer. Try again.\n")
        continue
    else:
        print("To choose your answer, please type either a, b, c or d (not in capitals, just lowercase).\n")
        continue




# The seventh question of the bible quiz!
   

# We have used the input() function to take the input of the user 
# and also used the conditional statements (if, elif, and else) to check if the user's input is one of the choices. 
user_input = ''

# A while True loop was included in order to iterate until the user's input is the correct answer.
while True:
    user_input = input("Question 7).\nHow many men did Jesus' feed with only five loaves of bread and two fish?\na) 2525\nb) 6000\nc) 1100\nd) 5000\n\n>> ")

    if user_input == 'a':
        print("Nope, wrong answer. Try again.\n")
        continue                                                        
    elif user_input == 'b':
        print("Nope, wrong answer. Try again.\n")
        continue
        # ... As the continue statement continues the loop until the correct answer is entered.
    elif user_input == 'c':
        print("Nope, wrong answer. Try again.\n")
        continue
    elif user_input == 'd':
        print("Correct.\n")
        # The score += 1 adds one to the score variable.
        score += 1
        break
    # The break statement breaks out of the while True loop... 
    else:
        print("To choose your answer, please type either a, b, c or d (not in capitals, just lowercase).\n")
        continue




# The eighth question of the bible quiz!
   

# We have used the input() function to take the input of the user 
# and also used the conditional statements (if, elif, and else) to check if the user's input is one of the choices. 
user_input = ''

# A while True loop was included in order to iterate until the user's input is the correct answer.
while True:
    user_input = input("Question 8).\nHow many disciples did Jesus have?\na) 13\nb) 11\nc) 12\nd) 14\n\n>> ")

    if user_input == 'a':
        print("Nope, wrong answer. Try again.\n")
        continue                                                        
    elif user_input == 'b':
        print("Nope, wrong answer. Try again.\n")
        continue
        # ... As the continue statement continues the loop until the correct answer is entered.
    elif user_input == 'c':
        print("Correct\n")
        # The score += 1 adds one to the score variable.
        score += 1
        break
    # The break statement breaks out of the while True loop... 
    elif user_input == 'd':
        print("Nope, wrong answer. Try again.\n")
        continue
    else:
        print("To choose your answer, please type either a, b, c or d (not in capitals, just lowercase).\n")
        continue




# The ninth question of the bible quiz!
   

# We have used the input() function to take the input of the user 
# and also used the conditional statements (if, elif, and else) to check if the user's input is one of the choices. 
user_input = ''

# A while True loop was included in order to iterate until the user's input is the correct answer.
while True:
    user_input = input("Question 9).\nHow many books are there in the Bible?\na) 58\nb) 66\nc) 39\nd) 27\n\n>> ")

    if user_input == 'a':
        print("Nope, wrong answer. Try again.\n")
        continue                                                        
        # ... As the continue statement continues the loop until the correct answer is entered.
    elif user_input == 'b':
        print("Correct.\n")
        # The score += 1 adds one to the score variable.
        score += 1
        break
        # The break statement breaks out of the while True loop... 
    elif user_input == 'c':
        print("Nope, wrong answer. Try again.\n")
        continue
    elif user_input == 'd':
        print("Nope, wrong answer. Try again.\n")
        continue
    else:
        print("To choose your answer, please type either a, b, c or d (not in capitals, just lowercase).\n")
        continue




# The tenth and final question of the bible quiz!
   

# We have used the input() function to take the input of the user 
# and also used the conditional statements (if, elif, and else) to check if the user's input is one of the choices. 
user_input = ''

# A while True loop was included in order to iterate until the user's input is the correct answer.
while True:
    user_input = input("Final Question).\nWhat is the greatest commandment?\na)Love your neighbor's as yourself\nb) Do not worship idols\nc) Love the Lord your God with all your heart and with all your soul and with all your mind\nd) Do not murder\n\n>> ")

    if user_input == 'a':
        print("Nope, wrong answer. Try again.\n")
        continue                                                        
    elif user_input == 'b':
        print("Nope, wrong answer. Try again.\n")
        continue
        # ... As the continue statement continues the loop until the correct answer is entered.
    elif user_input == 'c':
        print("Congratulations, you got the final question right.\n")
        # The score += 1 adds one to the score variable.
        score += 1
        break
        # The break statement breaks out of the while True loop... 
    elif user_input == 'd':
        print("Nope, wrong answer. Try again.\n")
        continue
    else:
        print("To choose your answer, please type either a, b, c or d (not in capitals, just lowercase).\n")
        continue




print("wow good job {} on getting {} correct. Thank you for play my Bible quiz, hopefully you were able to learn something new.".format(name, score))



