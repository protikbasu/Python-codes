from collections import Counter
import pprint 
counts = Counter('''hi there how are you hi i am fine'''.lower().split())
print (counts)
pprint.pprint(counts)
