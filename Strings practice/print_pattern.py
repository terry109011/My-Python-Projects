def print_pattern(n):
    # Print a '*' pattern 
    if n <= 0:
        quit
    elif n == 1:
        print('*')
    else:
        for i in range(1,n+1):
            print(i * '*')

        for j in range(n-1,0,-1):
            print(j*'*')
                
print_pattern(10)