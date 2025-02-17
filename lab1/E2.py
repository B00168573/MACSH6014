
def linearNumGenerator(a, seed, c, m, count):
    vals = []
    for n in range(0, count):
        result = (a * seed + c) % m
        vals.append(result)
        seed = result
    return vals

print("The generated sequence numbers are: \t", linearNumGenerator(22, 35, 31, 100, 4))