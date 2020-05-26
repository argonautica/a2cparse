import csv

temp = []
with open("out.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(temp) # name of list here
