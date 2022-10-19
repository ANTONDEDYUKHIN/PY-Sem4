# найти корни квадратного уравнения 2мя способами.
# ax^2 + bx + c = 0, a=2, b=2, c=1


a=-2
b=2
c=1
disc=b**2-4*a*c
if a==0:
    x= -c /b
    print(x)
elif disc > 0:
    x1 = (-b - disc**0.5)/(2*a)
    x2 = (-b + disc**0.5)/(2*a)
    print(round(x1, 2), round(x2, 2))
elif not disc:
    x = -b/(2*a)
    print(round(x, 2))
else: print('нет вещественных корней')