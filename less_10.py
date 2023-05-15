#my_list=[1,2,3,4,5,6]
#iterator=iter(my_list)
#for elem in iterator:
#    print(elem)

class counter:
    def __init__(self, max_naumber):
        self.i=0
        self. max_naumber= max_naumber
        def __iter__(self):
            self.i=0
            return
        def __next__(self):
            self.i=1
            if self.i>self. max_naumber:
                raise  StopIteration
            return self.i
count=counter(5)
for elem in count:
    print(elem)



