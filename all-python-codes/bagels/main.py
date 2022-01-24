from random import shuffle

NUM_DIGIT = 3
MAX_GUESSES = 10


def main(): # main game
    print(
        f"""
        Bagels, a detective logic game.
        By Ibrahim raimi

        I am thinking of a number {NUM_DIGIT} number with no repeted digits.
        Try to guess what it is. Here re some clues:
        When i say:     That means:
            Pico        One digit is correct but in the wrong position.
            Fermi       One digit is correct and in the right position.
            Bagels      No digit is correct.

            For example, if the secret number was 248 and your guess was 843, the clues would be Fermi Pico
        """
    )

    while True: # main game loop
        secret_num = get_secret_num()
        print("I have though of a number")
        print(f"You have {MAX_GUESSES} guesses to get it.")

        num_guesses = 1
        while num_guesses <= MAX_GUESSES:
            guess = ""

            # keep looping until they enter a valid guess:
            while len(guess) != NUM_DIGIT or not guess.isdecimal():
                print(f"Guess {num_guesses}")
                guess = input("> ")

                clues = get_clues(guess, secret_num)
                print(clues)
                num_guesses += 1

                if guess == secret_num:
                    break

                if num_guesses > MAX_GUESSES:
                    print("You ran out of guesses.")
                    print(f"The nswer was {secret_num}")
                    break

        print("Do you want to play again? (yes or no)")
        if not input("> ").lower().startswith("y"):
            break
    print("Thanks for playing")


def get_secret_num():
    """ returns a string made up of {NUM_DIGITS} uniqe random digits """
    numbers = list("0123456789") # create a list of digits 0 - 9
    shuffle(numbers) # shuffle them into random order

    """ get the first {NUM_DIGITS} digits in the list for the secret number """
    secret_num = ""
    for i in range(NUM_DIGIT):
        secret_num += str(numbers[i])
    return secret_num


def get_clues(guess, secret_num):
    """ returns a string with the pico, fermi, bagels clues for a guess and secret number pair """
    if guess == secret_num:
        return "You got it!"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            # a correct digit is in the correct place
            clues.append("Fermi")
        elif guess[i] in secret_num:
            # a correct digit is in the incorrect place
            clues.append("Pico")

    if len(clues) == 0:
        return "Bagels" # there are no correct digit at all
    else:
        # sort the clues into alphabetical order so their original order does not give information away
        clues.sort()
        return " ".join(clues)


if __name__ == "__main__":
    main()
