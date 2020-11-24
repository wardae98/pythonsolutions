# Question: You are asked to square every digit of a number and concatenate them.
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
# Note: The function accepts an integer and returns an integer

def sq(num):
    x = ''.join(str(int(i)**2) for i in str(num)) #results in x being a string
    q = int(x) #x needs to be made back into an integer for the output
    print(q)
sq(9119)