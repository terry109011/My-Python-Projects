# find the highest score in a list

student_scores = [80, 60, 50, 65, 75, 55, 90]

maxscore = 0
for score in student_scores:
    if score > maxscore:
        maxscore = score

print(maxscore)