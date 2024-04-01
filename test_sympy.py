from sympy import symbols, expand, diff
x,a,b,c=symbols("x a b c")
p=a*x**2 + b*x + c
print(p)
print(diff(p,x))
print(diff(p,a))
expand(p*p)