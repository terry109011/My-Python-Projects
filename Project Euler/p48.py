import time

start = time.time()

my_sum = 0
for i in range(1, 1001):
    my_sum += i**i

my_sum = str(my_sum)
length = len(my_sum)
last_ten = my_sum[length - 10:length]


end  = time.time()
print(start - end)
print(last_ten)