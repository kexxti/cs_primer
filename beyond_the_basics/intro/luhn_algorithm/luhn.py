"""
# get seq.
# reverse seq.
# apply T() for nums
## T() = if x >= 0 and x <= 4 : 2x
##       if x >= 5 and : 2x - 9

"""

 

# next sum all digits
# check if sum mod10 = 0

def transform(d: int) -> str:
    if d >= 0 and d <= 4:
        return str(2*d)
    elif d >= 5 and d <= 9:
        return str(2*d - 9)
    else:
        raise ValueError


def luhn_check(seq: str) -> bool:
    digits = [i for i in reversed(seq)]
    
    for i in range(1,len(digits), 2):
        digits[i] = transform(int(digits[i]))
    
    return sum(map(int, digits)) % 10 == 0
