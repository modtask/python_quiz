def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct answer!")
            score = score + 25
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry, wrong answer. Try again. ")
            attempt = attempt + 1
    if attempt == 3:
        print("The correct answer is " + answer)
score = 0
print('Guess the Harry Potter Characters!')
guess1 = input("Who is the house elf that Harry first meets and frees? ")
check_guess(guess1, 'Dobby')
guess2 = input("Who helps Harry learn to create a patronus? ")
check_guess(guess2, 'Lupin')
guess3 = input("What is Voldemort's original name? ")
check_guess(guess3, 'Tom Riddle')
guess4 = input("What's the name of Hermione's cat? ")
check_guess(guess4, 'Crookshanks')
print("Your score is " + str(score) + "%")