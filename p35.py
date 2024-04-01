def digits(n):
    return [int(c) for c in reversed(str(n))]

def from_base(n,b):
    value=0
    for (idx,digit) in enumerate(digits(n)):
        value+=digit * b**idx
    return value
print(from_base(1234,8))

def to_base(n,b):
    digits=[]
    while n>b:
        digit=n%b
        n=n//2
        digits.append(digit)
    digits.append(n)
    value=0

    for digit in reversed(digits):
        value=10*value+digit
        

#print(digits(123))