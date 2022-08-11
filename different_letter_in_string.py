### Write your code here ###
def diff_letters(a):
    list_letter = []
    
    for x in a:
        list_letter.append(x)
    list_letter = list(dict.fromkeys(list_letter))

    total_letter = len(list_letter)
    
    return 'Since there are ' + str(total_letter) + ' in that string ' + str(list_letter)

print(diff_letters('ABCDAAAABBCCCE'))