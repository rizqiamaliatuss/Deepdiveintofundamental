import math

def distance(string):
  #Write your code here
    string = string.replace('(', '' )
    string = string.replace(')', '' )
    list_coordinate = string.split(',')

    x1 = int(list_coordinate[0])
    y1 = int(list_coordinate[1])
    x2 = int(list_coordinate[2])
    y2 = int(list_coordinate[3])

    d = math.sqrt(((x1 - x2)**2) + ((y1 - y2)**2))

    return 'The distance is ' + str(d)

a = '(0,-1), (-3,2)'

distance(a) 