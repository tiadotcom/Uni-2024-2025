# This program uses the Zero Theorem to find an approximate zero of f(x) = x^3 - x - 1 

### INPUT VALUES ###
a = 0  # left endpoint
b = 2  # right endpoint
# Initial interval: [a, b]
precision = 1/32

### MAIN ###
interval_range = abs(a - b)
while interval_range > precision:
    middle = (a + b) / 2 
    if (middle**3 - middle - 1) == 0:
        print(f"{middle} is a zero of the function")
        break
    if (middle**3 - middle - 1) < 0:
        a = middle
    else:
        b = middle
    interval_range = abs(a - b)
print(f"The zero of f(x) is in the interval [{round(a, 5)}, {round(b, 5)}]")
# print(f"Final interval range: {interval_range}")


