
def raise_to_the_dergees(naumber, max_dergees):
    i=0
    for _ in range( max_dergees):
        yield  naumber**i
        i+=1
res=raise_to_the_dergees(122345,500)
print(res)
for _ in res:
    print(_)