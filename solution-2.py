#Question: An ATM has only 100, 50, and 20 dollar bills available. Given an ammount between 40 and 10,000 dollars and
#assuming that the ATM wants to use as few bills as possible, determine the minimum number of bills that the ATM needs to dispense


def withdraw(amount):
    notes = [0, 0, 0]
    string = str(amount)
    even = amount % 20
    if amount <= 80 and even == 0:
        notes[2] += amount / 20
    else:
        while string[-2] != "0" and string[-2] != "5":
            string = str(amount)
            amount -= 20
            notes[2] +=1
        if string[-2] == "5":
            amount -= 50
            notes[1] += 1
        notes[0] += int(amount / 100)
    return notes
