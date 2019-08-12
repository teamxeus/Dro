def square_root(number):
    Xnext = 0
    loops = 0
    length = len(str(number))
    if length > 0 and length <= 3:
        loops = 10
    else:
        if length > 3 and length <= 6:
            loops = 20
        if length > 6 and length <= 9:
            loops = 30
        if length > 9 and length <= 12:
            loops = 40
        if length > 12 and length <= 15:
            loops = 50
        if length > 15:
            raise ValueError(" Number Too Long!")
    
    for i in range(loops):
        if i == 0:
            Xn = number/2
            Fx = Xn**2 - number
            FPx = 2*Xn
            Xnext = Xn - (Fx/FPx)
    
        else:
            Xn = Xnext
            Fx = Xn**2 - number
            FPx = 2*Xn
            Xnext = Xn - (Fx/FPx)
            if i == (loops-1):
                print(Xnext)

def cube_root(number):
    Xnext = 0
    loops = 0
    length = len(str(number))
    if length > 0 and length <= 3:
        loops = 20
    else:
        if length > 3 and length <= 6:
            loops = 30
        if length > 6 and length <= 9:
            loops = 40
        if length > 9 and length <= 12:
            loops = 50
        if length > 12 and length <= 15:
            loops = 60
        if length > 15 and length <= 18:
            loops = 70
        if length > 18:
            raise ValueError(" Number Too Long!")
    
    for i in range(loops):
        if i == 0:
            Xn = number/2
            Fx = Xn**3 - number
            FPx = 3*(Xn**2)
            Xnext = Xn - (Fx/FPx)
           
        else:
            Xn = Xnext
            Fx = Xn**3 - number
            FPx = 3*(Xn**2)
            Xnext = Xn - (Fx/FPx)
            if i == (loops-1):
                print(Xnext)


square_root(55681444)
cube_root(719323136)