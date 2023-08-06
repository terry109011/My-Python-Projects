def square_list(p_list):
    for index in range(len(p_list)):
        p_list[index] = p_list[index]**2
    return p_list

my_list = [10,20,30,40]
print(square_list(my_list))