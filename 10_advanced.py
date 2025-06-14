squares = [x*x for x in range(5)]
def gen():
    for i in range(3):
        yield i
g = gen()
print(next(g))
print(squares)