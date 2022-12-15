from collections import defaultdict
def nearlySimilarRectangles(sides):
    gcd = lambda a, b: gcd(b, a % b) if b > 0 else a
    d = defaultdict(int)
    for w, h in sides:
        z = gcd(w, h)
        d[(w // z, h // z)] += 1
    return sum((x * (x - 1)) // 2 for x in d.values())