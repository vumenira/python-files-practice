import pickle

students_table = []

with open("data.csv") as data:
    next(data)
    for row in data:
        students_table.append([int(i) if i.isnumeric() else i for i in row[:-1].split(", ")]) #А нащо тут квадратні дужки? без них не працює

students_dict = {}

for student in students_table:
    if f"grade {student[3]}" in students_dict:
        if student[5] in students_dict[f"grade {student[3]}"]:
            students_dict[f"grade {student[3]}"][student[5]].append(student)
        else:
            students_dict[f"grade {student[3]}"][student[5]] = [student]
    else:
        students_dict[f"grade {student[3]}"] = {}
        students_dict[f"grade {student[3]}"][student[5]] = [student]

#for grade in students_dict:
 #   print(grade)
  #  for language in students_dict[grade]:
   #     print("   ", language)
    #    for student in students_dict[grade][language]:
     #       print("       ", student)

with open("gay.sex", "wb") as file:
    pickle.dump(students_dict, file)

with open("gay.sex", "rb") as data:
    interesting_data = pickle.load(data)

for grade in interesting_data:
    print(grade)
    for language in interesting_data[grade]:
        print("   ", language)
        for student in interesting_data[grade][language]:
            print("       ", student)