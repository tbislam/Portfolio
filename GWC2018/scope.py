

def say_hello(cool):
  print("Hi", cool)

def respond(nome):
    res = input("can I ask you some questions?")
    if res == "yes":
        print("Ok lets get started!")
        green = input("what is your favorite animal?")
        print ("No way!", green, "is my favorite animal as well!")
    else:
        print("Bye", nome)


def main():
  answer = input("what's your name?")
  say_hello(answer)
  respond(answer)


if __name__ == "__main__":
    main()
