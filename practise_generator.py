def hundred_numbers():
    nums=[]
    i=0
    while i < 100:
        yield i
        i+=1

g=hundred_numbers()
print(next(g))

print([x*2 for x in hundred_numbers()])