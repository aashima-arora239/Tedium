inp = "lexicon.txt"
data = open(inp)
dat = data.read()
lst = dat.splitlines()
final_list =[]
templist = []
for l in lst :
    d = l.split(" ")
    d[0] = d[0].replace("\'","")
    d[0] = d[0].replace("-","")
    d[0] = d[0].replace("_","")
    d[0] = d[0].replace("<","")
    d[0] = d[0].replace(">","")
    d[0] = d[0].decode('ascii','ignore')
    templist.append(d[0])

for w in list(sorted(set(templist))):
    word = list(w)
    k = ' '.join(i.upper() for i in word)
    element = w + " " + k
    final_list.append(element)

final_list
f = open('lexicon_words','w')
for element in final_list:
    f.write(element)
    f.write('\n')
f.close()
