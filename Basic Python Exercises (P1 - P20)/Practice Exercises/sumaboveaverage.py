student_scores = [80, 60, 50, 65, 75, 55]

def sum_score_above_average(p_student_scores):
    total_sum = 0
    sum_above_average = 0
    for element in p_student_scores:
        total_sum += element
    avg = total_sum / len(p_student_scores)
    print(f'Average score: {avg}')
    for item in p_student_scores:
        if item > avg:
            sum_above_average += item
            print('Above average score: ', item)
    return sum_above_average

output = sum_score_above_average(student_scores);
print(f'Sum of above average scores: {output}')
    
