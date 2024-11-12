import pickle
import os
import csv

with open("totalynormal.file", "rb") as data:
    interesting_data = pickle.load(data)

for grade in interesting_data:
    os.makedirs(grade, exist_ok=True)
    for language in interesting_data[grade]:
        with open(f"{grade}\\{language}.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(interesting_data[grade][language])
