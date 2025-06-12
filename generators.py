# generator
from sys import getsizeof
val = (x *2 for x in range(20000))
val2 = [x *2 for x in range(20000)]
print(getsizeof(val))
print(getsizeof(val2))