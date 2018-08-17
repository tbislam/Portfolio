questions = ["How old are you?", "What's your favorite color?", "What's your favorite animal?", "What's your favorite sport?", "What's your favorite show?"]

def say_hello(name):
    print("Hi " + name)


def main():
    print("Hi there! I'm ChatBot! What's your name?")
    user = input()
    say_hello(user)
    print("How are you today?")
    user_input = input()
    print("Awesome! Ask me a question or type A for a joke!")
    user_input = input()
    i = 0
    if user_input == "A":
        print("I totally understand how batteries feel because I'm rarely ever included in things either!")
        print("Now lets really chat!")
        print("Ask me a question!")
        user_input = input()
        while i <= 2:
            response()
            quest()
            i += 1
            print("Awesome! Ask me another question")
            user_input = input()
            print("That was fun",user, "goodbye" )

    else:
        while i <= 2:
            response()
            quest()
            i += 1
            print("Awesome! Ask me another question")
            user_input = input()
            print("That was fun",user, "goodbye" )


from random import *


def response():
    responses = ["Hmm, I don't think I can answer that", "That's an interesting question...I'm not sure", "Try again later", "You should try asking Google", "Let me think about that; I'll get back to you later...", "The signs point to yes", "The signs point to no" ]
    x = randint(0, len(responses)-1)
    print(responses[x])

def quest():
    x = randint(0, len(questions)-1)
    print(questions[x])
    user_input = input()
    if x == 0:
        print ("I'm also", user_input, "years old too!")
    if x == 1:
        print ("I like", user_input, "too!")
    if x == 2:
        print ("I love", user_input,"!")
    if x == 3:
        print ("I love playing", user_input,"!")
    if x == 4:
        print ("I love watching", user_input,"!")
    questions.remove(questions[x])
    print (len(questions))
