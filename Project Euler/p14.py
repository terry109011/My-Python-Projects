# import math
# import time

start_time = time.time()
count = 0
largest = 0

# stored_value = {}

for i in range(1, 1000000):
    num = i
    final = 0
    count = 1
    # if isPowerOfTwo(num) == True:
    #     continue
    while final != 1:
        if final in stored_value:
            count += stored_value
            stored_value.setdefault(num, count)
            
            break
        if num % 2 == 0:
            num = int(num / 2)
        else:
            num = int(3 * num + 1)
            
        final = num
        count += 1
        
        if count > largest:
            largest = count
            start_num = i
    stored_value.setdefault(num, count)

    dic - # add key as the starting number and value as the length of the number
end_time = time.time()

print(largest)
print(start_num)
print(f'Time = {end_time - start_time} s')

# Python - managed to optimize my initial brute force solution that took approx. 10 seconds to complete and got under 2 seconds with this one using a dictionary to memorize lengths of already calculated chains based on their starting points.

# def collatz_memo(k, memo_chains):    
#     memo_chains[k] = 1
#     n = k
#     while n > 1:
#         if n % 2 == 0:
#             n //= 2
#         else:
#             n = 3 * n + 1
#         if n in memo_chains:
#             memo_chains[k] += memo_chains[n]
#             return memo_chains
#         else:
#             memo_chains[k] += 1
#     return memo_chains

# def get_longest_chain():
#     memo_chains = {}
#     longest_chain = 0
#     i = 3

#     while i < 1e6:
#         memo_chains = collatz_memo(i, memo_chains)
#         if memo_chains[i] > longest_chain:
#             longest_chain = memo_chains[i]
#             best_start = i
#         i += 2

#     print(best_start)

# get_longest_chain()
        
