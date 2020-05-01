def is_perfect_square(b: int)-> int :
    root = b**(0.5)
    return int(root)**2== b

print(is_perfect_square(225))
