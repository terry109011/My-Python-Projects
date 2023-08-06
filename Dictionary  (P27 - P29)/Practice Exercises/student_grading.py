student_scores = {
  "John": 90,
  "Edy": 68,
  "Marry": 88, 
  "Ewan": 79,
  "Park": 62,
}

def convert_grades(p_list):
    for key in p_list:
        if p_list[key] >= 85:
            p_list[key] = 'Outstanding'
        elif p_list[key] >= 65:
            p_list[key] = 'Good'
        elif p_list[key] >= 50:
            p_list[key] = 'Acceptable'
        else:
            p_list[key] = 'Fail'
    return p_list

print(convert_grades(student_scores))

