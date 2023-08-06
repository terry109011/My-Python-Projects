unique   = {1 : 'one',
            2 : 'two',
            3 : 'three',
            4 : 'four',
            5 : 'five',
            6 : 'six',
            7 : 'seven',
            8 : 'eight',
            9 : 'nine',
            11 : 'eleven',
            12 : 'twelve',
            13 : 'thirteen',
            14 : 'fourteen',
            15 : 'fifteen',
            16 : 'sixteen',
            17 : 'seventeen',
            18 : 'eighteen',
            19 : 'nineteen'}

tenth = {10 : 'ten',
         20 : 'twenty',
         30 : 'thirty',
         40 : 'fouty',
         50 : 'fifty',
         60 : 'sixty',
         70 : 'seventy',
         80 : 'eighty',
         90 : 'ninety'}

length = 0
for i in range(1, 1001):
    char_i = str(i)
    num_len = len(char_i)
    suffix = ''
    if i in unique:
        name = unique[i]
    elif i in tenth:
        name = tenth[i]
    else:
        # check 2 digits
        if num_len == 2:
            prefix = tenth[int(char_i[0]) * 10]
            suffix = unique[int(char_i[1])]
            name = prefix + suffix
            
        # check 3 digits
        if num_len == 3:
            prefix = unique[int(char_i[0])] + 'hundred'
            if int(char_i[1:2]) in tenth:
                suffix = 'and' + tenth[int(char_i[1:2])]
            elif int(char_i[1:2]) in unique:
                suffix = 'and' + unique[int(char_i[1:2])]              
            name = prefix + suffix
            
        # check 4 digits
        if i == 1000:
            name =  unique[int(char_i[0])] + 'thousand'
            
        length += len(name)
            
print(length)