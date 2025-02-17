
def linearNumGenerator(a, seed, c, m, count):
    vals = []
    for n in range(0, count):
        result = (a * seed + c) % m
        vals.append(result)
        seed = result
    return vals

print("The generated sequence numbers are: \t", linearNumGenerator(954365343, 436241, 55119927, 1000000, 4))