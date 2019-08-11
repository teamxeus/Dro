def square_root(number):
    if  number > 0:
        return pow(number,1/2)
    else:
        return "The input must be a number above 0"
    

print(round(square_root(2),2))