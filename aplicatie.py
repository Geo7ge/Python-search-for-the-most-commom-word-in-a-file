fname = input("Enter File : ")
if len(fname) < 1 : fname = "clown.txt"
hand = open(fname)

di = dict()

for line in hand:
    line = line.rstrip()
    wds = line.split()
    for w in wds:
        #idiom : retrieve/create/update counter
        di[w] = di.get(w, 0) + 1

#print(di)

#now we want to find the most common word
largest = -1
theword = None
for k, v in di.items():
      if v > largest:
        theword = k
        largest = v
        
print("Done : ", theword, largest)
    