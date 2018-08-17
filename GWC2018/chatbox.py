# --- Define your functions below! ---
def intro():
    print ("Hello, welcome to Alexandra's Chatbox!")
    print("I am here if you are feeling nervous, happy or excited")
    print("Now, talk to me!")
def response(name):
    i = 0
    if name == "hi":
        print("Hello, how are you?")
        i += 1
        print (i)
    else:
        print("Ok, thats interesting")z\
# --- Put your main program below! ---
def main():
    intro()
    while True:
        answer = input("(What do you want to talk about?) ")
        response(answer)



# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
