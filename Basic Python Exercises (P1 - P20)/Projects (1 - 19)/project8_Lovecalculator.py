# Project 8 - Love Calculator

name1 = input('Enter name 1: ').lower()
name2 = input('Enter name 2: ').lower()

combined_name = name1 + name2

t = combined_name.count("t") 
r = combined_name.count("r") 
u = combined_name.count('u')
e = combined_name.count('e')

l = combined_name.count('l')
o = combined_name.count('o') 
v = combined_name.count('v')

trueSum = t + r + u + e
loveSum = l + o + v + e
score = int(str(trueSum) + str(loveSum))
print(trueSum)
print(loveSum)
print(score)

if score <= 10 or score >= 85:
    print(f'Your score is {score}, you go together like coke and mentos.')
elif score <= 70 and score >= 40:
    print(f'Your score is {score}, you two are alright together.')
else:
    print(f'Your score is {score}.')
    