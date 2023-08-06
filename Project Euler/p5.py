# import time
# start = time.time()
 
num = 20
j = 1
while j < 20:
    if num % j != 0:
        num += 20
        j = 1
        continue
    j += 1
print(num)

# end = time.time()
# print(end - start)

# BEST SOLUTION
# i = 1
# for k in (range(1, 21)):
#     if i % k > 0:
#         for j in range(1, 21):
#             if (i*j) % k == 0:
#                 i *= j
#                 break
# print(i)

# SOLUTION #2
# num = 20
# while True:
#     if all(num % n == 0 for n in range(2,20)):
#         print(num)
#         break
#     num += 20

