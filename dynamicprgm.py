import random

mylist = ['A','C','G','T']


a=(random.choices(mylist, weights = [3,3,3,3], k = 16))

b=(random.choices(mylist, weights = [3,3,3,3], k = 16))


 
S1=listToStr = ''.join([str(elem) for i,elem in enumerate(a)])
S2=listToStr = ''.join([str(elem) for i,elem in enumerate(b)]) 
print(S1)
print(S2)