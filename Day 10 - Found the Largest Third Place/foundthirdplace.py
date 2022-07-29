names = ['Ali', 'Budi', 'Caca', 'Dika', 'Ezha', 'Fika']
score = [80, 90, 90, 100, 100, 80]

def third_place(nama, score):
    ### Your code starts here ###
    
    score_not_duplicate = []
    result = []
   
    for i in score:
        if i not in score_not_duplicate:
            score_not_duplicate.append(i)
    
    score_not_duplicate.sort(reverse = True)
    
    ketiga = score_not_duplicate[2]
    
    for sc,nm in zip(score, names):
        if sc == ketiga:
            result.append(nm)
            
    print("The Third winner is :" + " " + str(result)[1:-1])

third_place(names, score)