#Question: write a function that returns an integer that's greater the N but not greater than 1000000000 and ends with 0. Assume N is between 1 and 999999999
import random
def solution(N):
    answer = random.randint(N,1000000000)
    multiple = answer % 10
    if multiple == 0:
        print(answer)
    else:
        print(answer * 10)

