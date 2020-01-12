from Lookup import lookupContact
from Store import storeContact

def main():
    response = actionSpinner()
    if response == "l":
        lookupContact()
    elif response == "s":
        storeContact()


def actionSpinner():
    while True:
        response = input("Press s to save a new contact or press l to lookup a contact")
        if response == "s" or response == "l":
            return response
        else:
            print("That is not a valid response")


main()
