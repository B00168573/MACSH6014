
def linearNumGenerator(a, seed, c, m, count):
    vals = []
    for n in range(0, count):
        result = (a * seed + c) % m
        vals.append(result)
        seed = result
    return vals

print("The generated sequence numbers are: \t", linearNumGenerator(2175143, 3553, 10653, 1000000, 4))