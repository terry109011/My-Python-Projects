# Project 10 - Score checker
while True:
    try:
        score = float(input('Enter score between 0.0 and 1.0: '))
        if score >= 0.0 and score <= 1.0:
            if score < 0.5:
                print('F')
            elif score < 0.6:
                print('E')
            elif score < 0.7:
                print('D')
            elif score < 0.8:
                print('C')
            elif score < 0.9:
                print('B')
            else:
                print('A')
            break;
        else: 
            print('Bad score. Please try again.')
    except ValueError:
        print('Invalid input. Please try again.')
        continue
    
    