from collections import Counter
import csv
z = 0


list = ["Princeton", "Harvard", "Columbia", "MIT", "Yale", "Stanford", "UChicago", "UPenn", "Northwestern", "Duke", "JHU", "CalTech", "Dartmouth", "Brown", "Notre Dame", "Vanderbilt", "Cornell", "Rice", "Wustl", "UCLA", "Emory", "UC Berkeley", "USC", "Georgetown", "CMU", "UMich", "UVA", "Georgia Tech", "NYU", "Tufts", "UNC", "UCSD", "UCD", "UCSB", "UF", "URoch", "Williams", "Amherst", "Swarthmore", "Wellesley", "Pomona", "Bowdoin", "Barnard", "Harvey Mudd"]
spellings = [["Princeton", "Pton"], ["Harvard", "Big H"], ["Columbia"], [" MIT ", "Massachusetts Institute of Technology", "Masstech"], ["Yale"],
             ["Stanford", "St. Anford", "St Anford", "CSU Palo Alto"], ["UChicago", "University of Chicago", "UC Hicago"],
             ["UPenn", "University of Pennsylvania"], ["Northwestern", " NU "], ["Duke"], ["JHU", "John Hopkins"],
             ["Caltech", "California Institute of Technology", " Cit " ], ["Dartmouth"], ["Brown"], ["Notre Dame"], ["Vanderbilt"],
             ["Cornell", "Suny Ithaca"], ["Rice"], ["Wustl", "Washu"], ["UCLA", "UC Los Angeles"], ["Emory"],
             ["UCB", " Cal ", "UC Berkeley", "University of California Berkeley"],
             ["University of Southern California", "USC", "University of Spoiled Children"], ["Georgetown"],
             ["Carnegie Mellon University", "CMU" ], ["University of Michigan", "UMich"], ["UVA", "University of Virginia"],
             ["Georgia Tech", " GT ", "GaTech", "Gtech"], ["New York University", "NYU"], ['Tufts'], [" UNC ", "Chapel Hill"], ["UCSD", "UC San Diego", "University of California San Diego"],
             ["UC Davis", " UCD", "University of California Davis"], ["UCSB", "University of California Santa Barbara", "UC Santa Barbara"], [" UF ", "University of Florida"],
             ["URoch", "University of Rochester"], ["Williams", "Williams College"], ["Amherst College"], ["Swarthmore"], ["Wellesley"], ["Pomona"], ["Bowdoin"], ["Barnard"], ["Harvey Mudd", "HMC"]


]


names = dict(zip(list, spellings))
count = {name:z for name in list}
text = open("results.txt").read().lower()



for key in count.keys():
    for name in names[key]:
        count[key] = count[key] + text.count(name.lower())


print(count)


c = Counter(count)
ordered = c.most_common()
print(type(ordered[1]))
final = []
for i in range( len(ordered) ):
    temp = []
    temp.append(i + 1)
    temp.append(ordered[i][0])
    temp.append(ordered[i][1])
    final.append(temp)
    temp = []

t20s = []
for i in range(20 ):
    temp = []
    temp.append(i + 1)
    temp.append(ordered[i][0])
    temp.append(ordered[i][1])
    t20s.append(temp)
    temp = []

with open("t20.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(t20s)
