# input age
while True:
  try:
    age = int(input("Enter age: ")) 
    if age>18 and age<51:
      print("Age entered successfully...")
      break;
    else:
      print("Age should be >18 and <51...")      
  except ValueError:
    print("Provide an integer value...")
    continue

# input gender
while True:
  try:
    gender = input("Enter gender: ")
    if gender == "Male" or gender == "Female":
      print("Gender entered successfully...")
      break;
    else:
      print("Gender should be either Male or Female")   
  except:
    continue

# print age and gender
print("Age is:", age)
print("Gender is:", gender)