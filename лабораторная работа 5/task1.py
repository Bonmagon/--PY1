from pprint import pprint


def shifting(n):
    return {'bin': bin(n), 'dec': n, 'hex': hex(n), 'oct': oct(n)}


pprint(list(shifting(n) for n in range(16)))
