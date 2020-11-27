#Question: create a function that returns the middle character(s) of a word 

#1: 
def get_middle(str):
    return str[(len(str)-1)//2:(len(str)+2)//2]

#2:
def get_middle(str):
    if len(str) % 2 == 0:
        left = str[(len(str)-1)//2]
        right = str[len(str)//2]
        return left, right
    else:
        return str[len(str)//2]



