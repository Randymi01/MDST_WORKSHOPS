"""
MDST Workshop 1 - Python Basics Starter Code
"""

# Add any imports you need here:
import random
import base64

def part1(num):
    """
    Ask the user for a number. Depending on whether the number is even or odd,
    print out an appropriate (i.e. "even" or "odd") message to the user.
    """
    if num%2 != 0:
        print("odd!")
    else:
        print("even!")


def part2():
    """
    Generate a random number between 1 and 9 (including 1 and 9). Ask the user
    to guess the number, then tell them whether they guessed too low, too high,
    or exactly right.
    (Hint: remember to use the user input lessons from the very first
    exercise).
    Keep the game going until the user types "exit".
    [ try checking the random module in python on google. Concepts: Infinite
    loops, if, else, loops and user/input].
    """
    random.seed(1092)
    number = random.randint(1,9)
    while(True):
        user_input = input("Guess: ")
        if user_input == "exit":
            break
        user_input = int(user_input)
        if user_input == number:
            print("You got it!")
            break
        elif user_input > number:
            print("Too high")
        else:
            print("Too low")

def part3(string):
    """
    Ask the user for a string and print out whether this string is a palindrome
    or not. (A palindrome is a string that reads the same forwards and
    backwards.)
    """
    if string[::-1] == string:
        print("True")
    else:
        print("False")


def part4a(filename, username, password):
    """
    Encrypt your username and password using base64 module
    Store your encrypted username on the first line and your encrypted password
    on the second line.
    """
    user = base64.b64encode(username.encode("utf-8"))
    pw = base64.b64encode(password.encode("utf-8"))
    f = open(filename, 'a')
    f.write(str(user, "utf-8"))
    f.write('\n')
    f.write(str(pw, "utf-8"))


def part4b(filename, password=None):
    """
    Create a function to read the file with your login information.
    Print out the decrypted username and password.
    If a password is specified, update the file with the new password.
    """

    f = open(filename, 'r')
    lines = f.readlines()
    eny_username = lines[0]
    eny_password = lines[1]

    username = str(base64.b64decode(eny_username), "utf-8")
    pw = str(base64.b64decode(eny_password), "utf-8")

    if password != None:
        part4a(filename, username, password)
        print("Password: {}\nUsername: {}".format(password, username))
    else:
        print("Password: {}\nUsername: {}".format(pw, username))


if __name__ == "__main__":
    part1(3)  # odd!
    part1(4)  # even!
    part2()
    part3("ratrace")  # False
    part3("racecar")  # True
    part4a("secret.txt", "naitian", "p4ssw0rd")
    part4b("secret.txt")
    part4b("secret.txt", password="p4ssw0rd!")
    part4b("secret.txt")
