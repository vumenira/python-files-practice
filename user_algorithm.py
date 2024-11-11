import pickle

with open("totalynormal.file", "rb") as data:
    interesting_data = pickle.load(data)

for grade in interesting_data:
    print(grade)
    for language in interesting_data[grade]:
        print("   ", language)
        for student in interesting_data[grade][language]:
            print("       ", student)