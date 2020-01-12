import json


def storeContact():
    name = input("Please enter the name of the contact")
    address = input("Please enter the address of the contact")
    phoneNumber = input("Please inter the phone number of the contact")


def storeInJSON(name, address, phoneNumber):
    data["contacts"] = []
    data["contacts"].append({
        "name": name,
        "address": address,
        "phoneNumber": phoneNumber
    })
    with open("data.txt", "w") as outfile:
        json.dump(data, outfile)
