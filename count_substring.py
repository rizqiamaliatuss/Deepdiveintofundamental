from itertools import count


def substring_count(string, substring):
    string = string.upper()
    substring = substring.upper()
    count = start = 0
    while True:
        start = string.find(substring, start) + 1
        if start > 0:
            count+=1
        else:
            return count

a = input('enter string :')
b = input('enter substring :')
print(substring_count(a, b))