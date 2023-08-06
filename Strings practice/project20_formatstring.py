names = ['John', 'Edy', 'Jane', 'Kane']
scores = [90, 95, 80, 75]

print('{0:<10} {1:<5}'.format('Name','Score'))
for i in range(len(names)):
    name = names[i]
    score = scores[i]
    print('{0:<10} {1:<5}'.format(name, score))