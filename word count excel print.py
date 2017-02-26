from collections import Counter
import pprint
import csv

#mydic = {'number of storage arrays': 45,'number of ports':100}

counts = Counter('''hi there how are you how are you
'''.lower().split())
print (counts)
pprint.pprint(counts)

with open('output.csv', 'w') as output:
    writer = csv.writer(output)
    for key, value in counts.items():
        writer.writerow([key, value])
    #writer.writerows(mydic.items())

 
