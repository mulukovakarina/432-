def discriminant(a, b, c): 
    D = b**2 - 4*a*c 
    if D < 0:
        return ("действительных корней нет")  
    elif D == 0:
        x = -b / (2*a)
        return (x)
    else:
        d = D**0.5
        x1 = (-b + d) / (2*a)
        x2 = (-b - d) / (2*a)
        return (x1, x2)

def vieta(a, b, c):
    p = b / a
    q = c / a
    r = abs(int(q))
    for d in range(1, r + 1):
        if r % d != 0:         
            continue
        for x1 in (d, -d):          
            x2 = q / x1
            if x1 + x2 == -p:
                return (x1, x2)
    return ("целых корней неn")   

