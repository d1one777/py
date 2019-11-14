# function

def welcome():
    """welcome"""
    print("---------------------")
    print("|----- WELCOME -----|")
    print("---------------------")


def designation(n):
    """output name"""
    print("To " + n + " !")


name = input("your name : ")
name = name.title()

welcome()
designation(name)
