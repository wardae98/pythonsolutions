#Question: write a function that returns the letter(s) in a string that are repeated twice
import collections
def solution(S):
    repeated = collections.Counter(S)
    for x in repeated:
        if repeated[x] == 2:
            print(x)
solution("amma")